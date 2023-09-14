#include <raylib.h>
#include <btBulletDynamicsCommon.h>
#include <rlgl.h>
#include <raymath.h>
#include <iostream>
#include <string>
#include <fstream>
#include <boost/asio.hpp>  // required for UDP
#include <ctime>

// for string delimiter
std::vector<std::string> split(std::string s, std::string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    std::string token;
    std::vector<std::string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
    }

    res.push_back (s.substr (pos_start));
    return res;
}

int main(int argc, char** argv) {

    // UDP  
    const std::string IP_ADDR = "192.168.109.243";

    // String delimiter
    std::string delimiter = ",";

    boost::asio::io_context io_context;
    boost::asio::ip::udp::socket socket1(io_context);

    // Bind the first socket to port 5100
    boost::asio::ip::udp::endpoint receiver_endpoint1(boost::asio::ip::make_address(IP_ADDR), 5100);
    socket1.open(boost::asio::ip::udp::v4());
    socket1.bind(receiver_endpoint1);

    std::array<char, 1024> buffer;

    float pitch = 0.0f;
    float roll = 0.0f;
    float yaw = 0.0f;

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
	dynamicsWorld->setGravity(btVector3(0, -100, 0));

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
    btCollisionShape* sphereShape = new btSphereShape(0.5);
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
    camera.up = (Vector3){ 0.0f, 2.0f, 0.0f };          // Camera up vector (rotation towards target)
    camera.fovy = 45.0f;                                // Camera field-of-view Y
    camera.projection = CAMERA_PERSPECTIVE;                   // Camera mode type

    Mesh cubeMesh = GenMeshCube(20.0f, 1.0f, 20.0f);
    Model cubeModel = LoadModelFromMesh(cubeMesh);

    //SetCameraMode(camera, CAMERA_FREE); // Set a free camera mode

    SetTargetFPS(60);                   // Set our game to run at 60 frames-per-second



    // Game loop
    while (!WindowShouldClose())
    {

        // UDP

        // Receive UDP data from game controller
        boost::asio::ip::udp::endpoint sender_endpoint;
        size_t length;

        // Receive from socket1
        length = socket1.receive_from(boost::asio::buffer(buffer), sender_endpoint);
        std::string orientation_data(buffer.data(), length);

        // Split string
        std::vector<std::string> orientation = split(orientation_data, delimiter);
        std::string orientation_x = orientation[0];
        std::string orientation_y = orientation[1];

        pitch = std::stof(orientation_x)*DEG2RAD;
        roll = -std::stof(orientation_y)*DEG2RAD;

        btScalar rotationAngleX = pitch; // Set this to the desired rotation angle around the x axis, in radians
        btVector3 rotationAxisX(1, 0, 0); // x axis
        btQuaternion rotationX(rotationAxisX, rotationAngleX);

        btScalar rotationAngleZ = roll; // Set this to the desired rotation angle around the z axis, in radians
        btVector3 rotationAxisZ(0, 0, 1); // z axis
        btQuaternion rotationZ(rotationAxisZ, rotationAngleZ);

        btQuaternion rotation = rotationX * rotationZ;

        //btTransform tileTransform;
        tileRigidBody->getMotionState()->getWorldTransform(tileTransform);
        tileTransform.setRotation(rotation);
        tileRigidBody->setWorldTransform(tileTransform);

        // Update
        dynamicsWorld->stepSimulation(1 / 60.f, 100);

        // Update camera target
        //tileRigidBody->getMotionState()->getWorldTransform(tileTransform);
        btTransform sphereTransform;
        sphereRigidBody->getMotionState()->getWorldTransform(sphereTransform);
        //tileOrigin = tileTransform.getOrigin();
        btVector3 sphereOrigin = sphereTransform.getOrigin();
        sphereOrigin = sphereTransform.getOrigin();
        camera.target = (Vector3){sphereOrigin.getX(), sphereOrigin.getY(), sphereOrigin.getZ()};
        camera.position = (Vector3){sphereOrigin.getX() + 5.0f, sphereOrigin.getY() + 20.0f, sphereOrigin.getZ() + 20.0f};;  // Camera position

        // Tranformation matrix for rotations
        cubeModel.transform = MatrixRotateXYZ((Vector3){ rotationAngleX, 0.0f, rotationAngleZ });

        // Draw
        BeginDrawing();
        ClearBackground(RAYWHITE);

        BeginMode3D(camera);

        // Render cube
        //DrawCube((Vector3){tileOrigin.getX(), tileOrigin.getY(), tileOrigin.getZ()}, 20.0f, 2.0f, 20.0f, RED); // Adjust 
        DrawModel(cubeModel, (Vector3){tileOrigin.getX(), tileOrigin.getY(), tileOrigin.getZ()}, 1.0f, RED);   // Draw 3d model with texture

        // Draw sphere
        //btTransform sphereTransform;
        sphereRigidBody->getMotionState()->getWorldTransform(sphereTransform);
        //btVector3 sphereOrigin = sphereTransform.getOrigin();
        DrawSphere((Vector3){sphereOrigin.getX(), sphereOrigin.getY(), sphereOrigin.getZ()}, 1.0f, BLUE);

        EndMode3D();

        EndDrawing();
    }

    UnloadModel(cubeModel);     // Unload model data


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
