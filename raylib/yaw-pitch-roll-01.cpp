#include <iostream>
#include <string>
#include <fstream>
#include <raylib.h>
#include "raymath.h"        // Required for: MatrixRotateXYZ()
#include <boost/asio.hpp>

#define MAX_BUFFER_SIZE 1024
#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600


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

//------------------------------------------------------------------------------------
// Program main entry point
//------------------------------------------------------------------------------------
int main(void)
{
    // UDP  

    // String delimiter
    std::string delimiter = ",";

    boost::asio::io_context io_context;
    boost::asio::ip::udp::socket socket1(io_context);
    boost::asio::ip::udp::socket socket2(io_context);

    // Bind the first socket to port 5100
    boost::asio::ip::udp::endpoint receiver_endpoint1(boost::asio::ip::make_address("192.168.109.243"), 5100); // Replace with your desired IP address
    socket1.open(boost::asio::ip::udp::v4());
    socket1.bind(receiver_endpoint1);

    // Bind the second socket to port 5101
    boost::asio::ip::udp::endpoint receiver_endpoint2(boost::asio::ip::make_address("192.168.109.243"), 5101); // Replace with your desired IP address
    socket2.open(boost::asio::ip::udp::v4());
    socket2.bind(receiver_endpoint2);

    std::array<char, MAX_BUFFER_SIZE> buffer1;
    std::array<char, MAX_BUFFER_SIZE> buffer2;

    std::ofstream outputFile;
    outputFile.open("received_data.csv");


    // Initialization
    //--------------------------------------------------------------------------------------
    const int screenWidth = 800;
    const int screenHeight = 450;

    //SetConfigFlags(FLAG_MSAA_4X_HINT | FLAG_WINDOW_HIGHDPI);
    InitWindow(screenWidth, screenHeight, "raylib [models] example - plane rotations (yaw, pitch, roll)");

    Camera camera = { 0 };
    camera.position = (Vector3){ 0.0f, 50.0f, -120.0f };// Camera position perspective
    camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };      // Camera looking at point
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };          // Camera up vector (rotation towards target)
    camera.fovy = 30.0f;                                // Camera field-of-view Y
    camera.projection = CAMERA_PERSPECTIVE;             // Camera type

    Model model = LoadModel("resources/models/obj/plane.obj");                  // Load model
    Texture2D texture = LoadTexture("resources/models/obj/plane_diffuse.png");  // Load model texture
    model.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = texture;            // Set map diffuse texture

    float pitch = 0.0f;
    float roll = 0.0f;
    float yaw = 0.0f;

    SetTargetFPS(60);               // Set our game to run at 60 frames-per-second
    //--------------------------------------------------------------------------------------

    // Main game loop
    while (!WindowShouldClose())    // Detect window close button or ESC key
    {
        // UDP

        // Receive UDP data from game controller
        boost::asio::ip::udp::endpoint sender_endpoint;
        size_t length;

        // Receive from socket1
        length = socket1.receive_from(boost::asio::buffer(buffer1), sender_endpoint);
        std::string orientation_data(buffer1.data(), length);

        // std::string x = orientation_data.substr(0, orientation_data.find(delimiter));
        // std::string y = orientation_data.substr(1, orientation_data.find(delimiter));

        std::vector<std::string> v = split (orientation_data, delimiter);

        std::cout << orientation_data << std::endl;
        std::cout << v[0] << ", " << v[1] << std::endl;

        // Receive from socket2
        length = socket2.receive_from(boost::asio::buffer(buffer2), sender_endpoint);
        std::string joystick_data = std::string(buffer2.data(), length);

        // std::string action = joystick_data.substr(0, joystick_data.find(delimiter));
        // std::string state = joystick_data.substr(1, joystick_data.find(delimiter));

        std::cout << joystick_data << std::endl;
        std::vector<std::string> j = split (joystick_data, delimiter);

        std::cout << j[0] << ", " << j[1] << std::endl;
        
        // Update
        //----------------------------------------------------------------------------------
        
        // if(action == "up") {
        //     pitch -= 0.6f;
        // }

        // if(action == "down") {
        //     pitch += 0.6f;
        // }

        pitch = -std::stof(v[0]);
        roll = std::stof(v[1]);

        
        
        // // Plane pitch (x-axis) controls
        // if (IsKeyDown(KEY_DOWN)) pitch += 0.6f;
        // else if (IsKeyDown(KEY_UP)) pitch -= 0.6f;
        // else
        // {
        //     if (pitch > 0.3f) pitch -= 0.3f;
        //     else if (pitch < -0.3f) pitch += 0.3f;
        // }

        // // Plane yaw (y-axis) controls
        // if (IsKeyDown(KEY_S)) yaw -= 1.0f;
        // else if (IsKeyDown(KEY_A)) yaw += 1.0f;
        // else
        // {
        //     if (yaw > 0.0f) yaw -= 0.5f;
        //     else if (yaw < 0.0f) yaw += 0.5f;
        // }

        // // Plane roll (z-axis) controls
        // if (IsKeyDown(KEY_LEFT)) roll -= 1.0f;
        // else if (IsKeyDown(KEY_RIGHT)) roll += 1.0f;
        // else
        // {
        //     if (roll > 0.0f) roll -= 0.5f;
        //     else if (roll < 0.0f) roll += 0.5f;
        // }

        // Tranformation matrix for rotations
        model.transform = MatrixRotateXYZ((Vector3){ DEG2RAD*pitch, DEG2RAD*yaw, DEG2RAD*roll });
        //----------------------------------------------------------------------------------

        // Draw
        //----------------------------------------------------------------------------------
        BeginDrawing();

            ClearBackground(RAYWHITE);

            // Draw 3D model (recomended to draw 3D always before 2D)
            BeginMode3D(camera);

                DrawModel(model, (Vector3){ 0.0f, -8.0f, 0.0f }, 1.0f, WHITE);   // Draw 3d model with texture
                DrawGrid(10, 10.0f);

            EndMode3D();

            // Draw controls info
            DrawRectangle(30, 370, 260, 70, Fade(GREEN, 0.5f));
            DrawRectangleLines(30, 370, 260, 70, Fade(DARKGREEN, 0.5f));
            DrawText("Pitch controlled with: KEY_UP / KEY_DOWN", 40, 380, 10, DARKGRAY);
            DrawText("Roll controlled with: KEY_LEFT / KEY_RIGHT", 40, 400, 10, DARKGRAY);
            DrawText("Yaw controlled with: KEY_A / KEY_S", 40, 420, 10, DARKGRAY);

            DrawText("(c) WWI Plane Model created by GiaHanLam", screenWidth - 240, screenHeight - 20, 10, DARKGRAY);

        EndDrawing();
        //----------------------------------------------------------------------------------
    }

    // De-Initialization
    //--------------------------------------------------------------------------------------
    outputFile.close();
    
    UnloadModel(model);     // Unload model data

    CloseWindow();          // Close window and OpenGL context
    //--------------------------------------------------------------------------------------

    return 0;
}
