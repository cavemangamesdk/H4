// raylib
#include <raylib.h>
#include <rlgl.h>
#include <raymath.h>
#include <raygui.h>

// bullet physics
#include <btBulletDynamicsCommon.h>

//
#include <iostream>
#include <string>
#include <fstream>
#include <boost/asio.hpp>  // required for UDP
#include <ctime>
#include <cstdint>
#include <cstdio>
#include <functional>
#include <vector>


#define RAYGUI_IMPLEMENTATION
#define WINDOW_WIDTH 1366
#define WINDOW_HEIGHT 768


// Raygui setup
constexpr int32_t textPadding = 8;

constexpr float padding = 4.0f;
constexpr float topbarHeight = 38.0f;
constexpr float buttonHeight = topbarHeight - (padding * 2.0f);

constexpr float startGamePanelWidth = 1024.0f;
constexpr float startGamePanelHeight = 512.0f;

constexpr float buttonWidth = 90.0f;

bool showAboutPanel = false;

static char rayguiBuffer[256] = { 0 };

enum class GameState{
    StartMenu,
    Gameplay
};

GameState state = GameState::StartMenu;

struct TopPanelButton {
    std::string Label;
    std::function<void()> Callback;
};

// for string splitting by delimiter
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

void DrawTopPanel(float windowWidth, float height, const std::vector<TopPanelButton>& buttons);
void DrawStartGamePanel(Vector2 windowSize, Vector2 panelSize);
void DrawAboutPanel(Vector2 windowSize, Vector2 panelSize, bool* showAboutPanel);
void ChangeState(GameState newState);

int main(int argc, char** argv) {

    std::string IP_ADDR = "192.168.109.243";

    switch (argc)
    {
        case 1:
            std::cout << "Using default IP address: " << IP_ADDR << std::endl;
            break;

        case 2:
            IP_ADDR = argv[1];
            std::cout << "Using IP address: " << IP_ADDR << std::endl;
            break;
        
        default:
            break;
    }


    // CSV file logging
    std::ofstream outputFile;
    outputFile.open("ball-in-a-maze-03.csv");
    outputFile << "timestamp, orientation_x, orientation_y, joystick_action, joystick_state, ball_x, ball_y, ball_z" << std::endl;
    
    // UDP  
    std::string delimiter = ",";

    boost::asio::io_context io_context;
    boost::asio::ip::udp::socket socket1(io_context);
    boost::asio::ip::udp::socket socket2(io_context);

    boost::asio::ip::udp::endpoint sender_endpoint;
    size_t length;

    std::vector<std::string> orientation = {"0", "0"};
    std::string orientation_x = "0";
    std::string orientation_y = "0";

    std::vector<std::string> joystick = {"0", "0"};
    std::string joystick_action = "null";
    std::string joystick_state = "null";

    // Bind the first socket to port 5100
    boost::asio::ip::udp::endpoint receiver_endpoint1(boost::asio::ip::make_address(IP_ADDR), 5100);
    socket1.open(boost::asio::ip::udp::v4());
    socket1.bind(receiver_endpoint1);

    // Bind the second socket to port 5101
    boost::asio::ip::udp::endpoint receiver_endpoint2(boost::asio::ip::make_address(IP_ADDR), 5101);
    socket2.open(boost::asio::ip::udp::v4());
    socket2.bind(receiver_endpoint2);

    std::array<char, 1024> buffer;


    // bullet physics setup
	///collision configuration contains default setup for memory, collision setup. Advanced users can create their own configuration.
	btDefaultCollisionConfiguration* collisionConfiguration = new btDefaultCollisionConfiguration();
	///use the default collision dispatcher. For parallel processing you can use a diffent dispatcher (see Extras/BulletMultiThreaded)
	btCollisionDispatcher* dispatcher = new btCollisionDispatcher(collisionConfiguration);
	///btDbvtBroadphase is a good general purpose broadphase. You can also try out btAxis3Sweep.
	btBroadphaseInterface* broadphase = new btDbvtBroadphase();
	///the default constraint solver. For parallel processing you can use a different solver (see Extras/BulletMultiThreaded)
	btSequentialImpulseConstraintSolver* solver = new btSequentialImpulseConstraintSolver;
	btDiscreteDynamicsWorld* dynamicsWorld = new btDiscreteDynamicsWorld(dispatcher, broadphase, solver, collisionConfiguration);
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
    btDefaultMotionState* sphereMotionState = new btDefaultMotionState(btTransform(btQuaternion(0, 0, 0, 1), btVector3(0, 10, 0)));
    btScalar sphereMass = 1;
    btVector3 sphereInertia(0, 0, 0);
    sphereShape->calculateLocalInertia(sphereMass, sphereInertia);
    btRigidBody::btRigidBodyConstructionInfo sphereRigidBodyCI(sphereMass, sphereMotionState, sphereShape, sphereInertia);
    btRigidBody* sphereRigidBody = new btRigidBody(sphereRigidBodyCI);
    dynamicsWorld->addRigidBody(sphereRigidBody);



    std::vector<TopPanelButton> topPanelButtons = {
        (TopPanelButton){
            GuiIconText(ICON_FILE_SAVE, "Save CSV"),
            [&]() {}
        },
        (TopPanelButton){
           GuiIconText(ICON_FILE_OPEN, "Open CSV"),
            [&]() {}
        }, 
        (TopPanelButton){
            "About",
            [&]() { showAboutPanel = !showAboutPanel; }
        }
    };

    // raylib setup
    // Initialize raylib window
    InitWindow(1200, 800, "Ball-in-a-Maze demo made with raylib, raygui and Bullet physics");
    SetWindowState(FLAG_WINDOW_RESIZABLE);

    // Define the camera to look into our 3d world
    Camera camera = { 0 };
    camera.position = (Vector3){ 0.0f, 10.0f, 10.0f };
    btTransform tileTransform;
    tileRigidBody->getMotionState()->getWorldTransform(tileTransform);
    btVector3 tileOrigin = tileTransform.getOrigin();
    camera.target = (Vector3){tileOrigin.getX(), tileOrigin.getY(), tileOrigin.getZ()};
    camera.up = (Vector3){ 0.0f, 2.0f, 0.0f };          // Camera up vector (rotation towards target)
    camera.fovy = 45.0f;                                // Camera field-of-view Y
    camera.projection = CAMERA_PERSPECTIVE;                   // Camera mode type

    Mesh cubeMesh = GenMeshCube(20.0f, 2.0f, 20.0f);
    Model cubeModel = LoadModelFromMesh(cubeMesh);

    Mesh sphereMesh = GenMeshSphere(0.1f, 16, 16);
    Model sphereModel = LoadModelFromMesh(sphereMesh);

    cubeModel.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = LoadTexture("resources/models/obj/board.png");

    Texture2D bearingTexture = LoadTexture("resources/models/obj/bearing_bearing_BaseColor.png");
    sphereModel.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = bearingTexture;

    //SetCameraMode(camera, CAMERA_FREE); // Set a free camera mode

    // // Handler to be called when data is received
    // auto handler1 = [&buffer, &length, &delimiter, &orientation, &orientation_x, &orientation_y](const boost::system::error_code& error, std::size_t bytes_transferred)
    // {
    //     // print to console
    //     std::cout << "Received: " << std::string(buffer.data(), length) << std::endl;

    //     if (!error)
    //     {
    //         std::string orientation_data(buffer.data(), length);
    //         orientation = split(orientation_data, delimiter);
    //         orientation_x = orientation[0];
    //         orientation_y = orientation[1];
    //     }
    //     else
    //     {
    //         // Handle error
    //     }
    // };

    // auto handler2 = [&buffer](const boost::system::error_code& error, std::size_t bytes_transferred)
    // {
    //     if (!error)
    //     {
    //         // Process received data stored in buffer
    //         // Note: remember to handle the case where bytes_transferred is 0
    //     }
    //     else
    //     {
    //         // Handle error
    //     }
    // };

    //io_context.run();

    SetTargetFPS(60);

    // Game loop
    while (!WindowShouldClose())
    {
        // UDP
        //socket1.async_receive_from(boost::asio::buffer(buffer), sender_endpoint, handler1);
        //socket2.async_receive_from(boost::asio::buffer(buffer), sender_endpoint, handler2);

        // Receive from socket1
        if(socket1.is_open())
        {
            length = socket1.receive_from(boost::asio::buffer(buffer), sender_endpoint);

            if(length > 0 ) {
                std::string orientation_data(buffer.data(), length);
                orientation = split(orientation_data, delimiter);
                orientation_x = orientation[0];
                orientation_y = orientation[1];
            }
        }

        // Receive from socket2
        if(socket2.is_open())
        {
            length = socket2.receive_from(boost::asio::buffer(buffer), sender_endpoint);
            
            if(length > 0 ) {
                std::string joystick_data = std::string(buffer.data(), length);
                joystick = split(joystick_data, delimiter);
                joystick_action = joystick[0];
                joystick_state = joystick[1];
            }
        }

        // Use received orientation data to tilt board
        btScalar rotationAngleX = std::stof(orientation_x)*DEG2RAD;
        btVector3 rotationAxisX(1, 0, 0);
        btQuaternion rotationX(rotationAxisX, rotationAngleX);

        btScalar rotationAngleZ = -std::stof(orientation_y)*DEG2RAD;
        btVector3 rotationAxisZ(0, 0, 1);
        btQuaternion rotationZ(rotationAxisZ, rotationAngleZ);

        btQuaternion rotation = rotationX * rotationZ;

        tileRigidBody->getMotionState()->getWorldTransform(tileTransform);
        tileTransform.setRotation(rotation);
        tileRigidBody->setWorldTransform(tileTransform);

        // Update physics
        dynamicsWorld->stepSimulation(1 / 60.f, 10);

        // Update camera target
        btTransform sphereTransform;
        sphereRigidBody->getMotionState()->getWorldTransform(sphereTransform);
        btVector3 sphereOrigin = sphereTransform.getOrigin();
        sphereOrigin = sphereTransform.getOrigin();
        camera.target = (Vector3){sphereOrigin.getX(), sphereOrigin.getY(), sphereOrigin.getZ()};
        camera.position = (Vector3){sphereOrigin.getX() + 0.5f, sphereOrigin.getY() + 2.0f, sphereOrigin.getZ() + 2.0f};;  // Camera position

        // Tranformation matrix for rotations
        cubeModel.transform = MatrixRotateXYZ((Vector3){ rotationAngleX, 0.0f, rotationAngleZ });

        // CSV file logging
        // Timestamp 
        time_t now = time(0);

        // convert now to string form
        std::string date_time = ctime(&now);

        // Write game data to .csv file
        outputFile << "\"" << date_time << "\", " << 
        orientation_x << ", " << orientation_y << ", " << 
        joystick_action << ", " << joystick_state << ", " << 
        sphereOrigin.getX() << ", " <<  sphereOrigin.getY() << ", " << sphereOrigin.getZ() << std::endl;

        // Draw
        BeginDrawing();
        ClearBackground(RAYWHITE);

        DrawTopPanel((float)WINDOW_WIDTH, topbarHeight, topPanelButtons);

        BeginMode3D(camera);

            // Render cube
            DrawModel(cubeModel, (Vector3){tileOrigin.getX(), tileOrigin.getY(), tileOrigin.getZ()}, 1.0f, WHITE);
            DrawGrid(100, 10.0f);

            // Render sphere
            sphereRigidBody->getMotionState()->getWorldTransform(sphereTransform);
            DrawModel(sphereModel, (Vector3){sphereOrigin.getX(), sphereOrigin.getY(), sphereOrigin.getZ()}, 1.0f, WHITE);

        EndMode3D();

        EndDrawing();
    }

    //io_context.stop();

    // Bullet cleanup
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
    delete broadphase;
    delete dispatcher;
    delete collisionConfiguration;

    // raylib cleanup
    UnloadModel(cubeModel);

    UnloadModel(sphereModel);
    UnloadTexture(bearingTexture);

    CloseWindow();

    return 0;
}

void DrawTopPanel(float windowWidth, float height, const std::vector<TopPanelButton>& buttons)
{
    float xPosition = padding;

    GuiDrawRectangle({0, 0, (float)windowWidth, height}, 0, BLACK, LIGHTGRAY);

    int buttonTextPadding = GuiGetStyle(BUTTON, TEXT_PADDING);
    GuiSetStyle(BUTTON, TEXT_PADDING, textPadding);

    for(size_t i = 0; i < buttons.size(); i++) {
        if(GuiButton({xPosition, padding, buttonWidth, buttonHeight }, buttons[i].Label.c_str())) {
            buttons[i].Callback();
        }
        xPosition += buttonWidth + padding;
    }

    GuiSetStyle(BUTTON, TEXT_PADDING, buttonTextPadding);
}

void DrawStartGamePanel(Vector2 windowSize, Vector2 panelSize)
{
    if (state == GameState::Gameplay) return;
    
    int result = GuiTextInputBox((Rectangle){ (float)GetScreenWidth()/2 - 120, (float)GetScreenHeight()/2 - 60, 240, 140 }, GuiIconText(ICON_FILE_SAVE, "Enter player name:"), "Enter player name:", "Start;Quit", rayguiBuffer, 255, NULL);

    if (result == 1)
    {
        // TODO: Validate textInput value and save
        if ((rayguiBuffer != NULL) && (rayguiBuffer[0] == '\0')) {
            printf("Player name is empty\n");
            return;
        }

        printf("%s\n", rayguiBuffer);

        // TODO: Change game state
        ChangeState(GameState::Gameplay);
    }

    if ((result == 0) || (result == 1) || (result == 2))
    {
        TextCopy(rayguiBuffer, "\0");
        if((result == 0) || (result == 2))
        {
            exit(0);
        }
    }
}

void DrawAboutPanel(Vector2 windowSize, Vector2 panelSize, bool* showAboutPanel)
{
    float x = (windowSize.x / 2.0f) - (panelSize.x / 2.0f);
    float y = (windowSize.y / 2.0f) - (panelSize.y / 2.0f);
    int32_t windowBox = GuiWindowBox({x, y, panelSize.x, panelSize.y}, "About");
    if(windowBox == 1) { // Close button pressed
        *showAboutPanel = false;
    }

    constexpr const char* madeByText = "Made by Michael, Victor & Pierre";
    constexpr float fontSize = 24.0f;
    constexpr float spacing = 1.0f;

    Vector2 textSize = MeasureTextEx(GetFontDefault(), madeByText, fontSize, spacing);

    x = (windowSize.x / 2.0f) - (textSize.x / 2.0f);
    y = (windowSize.y / 2.0f) - (textSize.y / 2.0f);
    DrawText(madeByText, x, y, (int32_t)fontSize, BLACK);
}

void ChangeState(GameState newState)
{
    if (newState == GameState::StartMenu)
    {
        /* code */
        //Show GUI.
    }
    else if (newState == GameState::Gameplay)
    {
        /* code */
        //Hide GUI.
    }
    state = newState;
}