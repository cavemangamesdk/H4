#include <raylib.h>
#include <btBulletDynamicsCommon.h>
#include <rlgl.h>
#include <raymath.h>

int main(int argc, char** argv) {

    // Initialize bullet physics
	///collision configuration contains default setup for memory, collision setup. Advanced users can create their own configuration.
	btDefaultCollisionConfiguration* collisionConfiguration = new btDefaultCollisionConfiguration();
	///use the default collision dispatcher. For parallel processing you can use a diffent dispatcher (see Extras/BulletMultiThreaded)
	btCollisionDispatcher* dispatcher = new btCollisionDispatcher(collisionConfiguration);
	///btDbvtBroadphase is a good general purpose broadphase. You can also try out btAxis3Sweep.
	btBroadphaseInterface* overlappingPairCache = new btDbvtBroadphase();
	///the default constraint solver. For parallel processing you can use a different solver (see Extras/BulletMultiThreaded)
	btSequentialImpulseConstraintSolver* solver = new btSequentialImpulseConstraintSolver;
	btDiscreteDynamicsWorld* dynamicsWorld = new btDiscreteDynamicsWorld(dispatcher, overlappingPairCache, solver, collisionConfiguration);
	dynamicsWorld->setGravity(btVector3(0, -10, 0));

    // Create tile physics body
    btCollisionShape* tileShape = new btBoxShape(btVector3(10, 1, 10)); // Change the size to make it a wide, square, tile shape
    btDefaultMotionState* tileMotionState = new btDefaultMotionState(btTransform(btQuaternion(0, 0, 0, 1), btVector3(0, 0, 0)));
    btScalar tileMass = 0; // Set the mass to 0 to make it a static rigid body
    btVector3 tileInertia(0, 0, 0);
    tileShape->calculateLocalInertia(tileMass, tileInertia);
    btRigidBody::btRigidBodyConstructionInfo tileRigidBodyCI(tileMass, tileMotionState, tileShape, tileInertia);
    btRigidBody* tileRigidBody = new btRigidBody(tileRigidBodyCI);
    dynamicsWorld->addRigidBody(tileRigidBody);

    // Create sphere physics body
    btCollisionShape* sphereShape = new btSphereShape(1);
    btDefaultMotionState* sphereMotionState = new btDefaultMotionState(btTransform(btQuaternion(0, 0, 0, 1), btVector3(0, 10, 0))); // Set the initial position to be right above the tile
    btScalar sphereMass = 1;
    btVector3 sphereInertia(0, 0, 0);
    sphereShape->calculateLocalInertia(sphereMass, sphereInertia);
    btRigidBody::btRigidBodyConstructionInfo sphereRigidBodyCI(sphereMass, sphereMotionState, sphereShape, sphereInertia);
    btRigidBody* sphereRigidBody = new btRigidBody(sphereRigidBodyCI);
    dynamicsWorld->addRigidBody(sphereRigidBody);


    // Initialize raylib window
    //InitWindow(800, 600, "raylib [models] example - skybox loading and drawing");
    InitWindow(800, 600, "UDP Receiver");

    // Define the camera to look into our 3d world
    Camera camera = { 0 };
    camera.position = (Vector3){ 0.0f, 10.0f, 10.0f };  // Camera position
    btTransform tileTransform;
    tileRigidBody->getMotionState()->getWorldTransform(tileTransform);
    btVector3 tileOrigin = tileTransform.getOrigin();
    camera.target = (Vector3){tileOrigin.getX(), tileOrigin.getY(), tileOrigin.getZ()};  // Camera looking at point
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };          // Camera up vector (rotation towards target)
    camera.fovy = 45.0f;                                // Camera field-of-view Y
    camera.projection = CAMERA_PERSPECTIVE;                   // Camera mode type


    //SetCameraMode(camera, CAMERA_FREE); // Set a free camera mode

    SetTargetFPS(60);                   // Set our game to run at 60 frames-per-second

    btScalar rotationAngleX = 0.0f; // Set this to the desired rotation angle around the x axis, in radians
    btVector3 rotationAxisX(1, 0, 0); // x axis
    btQuaternion rotationX(rotationAxisX, rotationAngleX);

    btScalar rotationAngleZ = 0.05f; // Set this to the desired rotation angle around the z axis, in radians
    btVector3 rotationAxisZ(0, 0, 1); // z axis
    btQuaternion rotationZ(rotationAxisZ, rotationAngleZ);

    btQuaternion rotation = rotationX * rotationZ;

    //btTransform tileTransform;
    tileRigidBody->getMotionState()->getWorldTransform(tileTransform);
    tileTransform.setRotation(rotation);
    tileRigidBody->setWorldTransform(tileTransform);

    // Game loop
    while (!WindowShouldClose())
    {

        // Update
        dynamicsWorld->stepSimulation(1 / 60.f, 10);

        // Update camera target
        //tileRigidBody->getMotionState()->getWorldTransform(tileTransform);
        btTransform sphereTransform;
        sphereRigidBody->getMotionState()->getWorldTransform(sphereTransform);
        //tileOrigin = tileTransform.getOrigin();
        btVector3 sphereOrigin = sphereTransform.getOrigin();
        sphereOrigin = sphereTransform.getOrigin();
        camera.target = (Vector3){sphereOrigin.getX(), sphereOrigin.getY(), sphereOrigin.getZ()};

        // Draw
        BeginDrawing();
        ClearBackground(RAYWHITE);

        BeginMode3D(camera);

        // Render cube
        DrawCube((Vector3){tileOrigin.getX(), tileOrigin.getY(), tileOrigin.getZ()}, 20.0f, 2.0f, 20.0f, RED); // Adjust 

        // Draw sphere
        //btTransform sphereTransform;
        sphereRigidBody->getMotionState()->getWorldTransform(sphereTransform);
        //btVector3 sphereOrigin = sphereTransform.getOrigin();
        DrawSphere((Vector3){sphereOrigin.getX(), sphereOrigin.getY(), sphereOrigin.getZ()}, 1.0f, BLUE);

        EndMode3D();

        EndDrawing();
    }


    // Cleanup
    dynamicsWorld->removeRigidBody(tileRigidBody);
    delete tileRigidBody->getMotionState();
    delete tileRigidBody;
    delete tileShape;

    dynamicsWorld->removeRigidBody(sphereRigidBody);
    delete sphereRigidBody->getMotionState();
    delete sphereRigidBody;
    delete sphereShape;

    delete dynamicsWorld;
    delete solver;
    delete overlappingPairCache;
    delete dispatcher;
    delete collisionConfiguration;

    CloseWindow();

}
