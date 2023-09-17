#include <iostream>
#include <btBulletDynamicsCommon.h>

int main() {
    std::cout << "Hello World!" << std::endl;

    // Create a new Bullet physics world
    btDefaultCollisionConfiguration* collisionConfiguration = new btDefaultCollisionConfiguration();
    btCollisionDispatcher* dispatcher = new btCollisionDispatcher(collisionConfiguration);
    btBroadphaseInterface* overlappingPairCache = new btDbvtBroadphase();
    btSequentialImpulseConstraintSolver* solver = new btSequentialImpulseConstraintSolver();
    btDiscreteDynamicsWorld* dynamicsWorld = new btDiscreteDynamicsWorld(dispatcher, overlappingPairCache, solver, collisionConfiguration);

    // Set gravity
    dynamicsWorld->setGravity(btVector3(0, -9.81, 0));

    // Simulate physics here...

    // Clean up
    delete dynamicsWorld;
    delete solver;
    delete overlappingPairCache;
    delete dispatcher;
    delete collisionConfiguration;

    return 0;
}
