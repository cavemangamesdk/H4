/*
    Raylib and UDP motion controller signal over wlan test
    Call this program with the IP address of the computer running the UDP server as argument
*/

#include <iostream>
#include <string>
#include <fstream>
#include <raylib.h>        // Required for graphics
#include <raymath.h>       // Required for MatrixRotateXYZ()
#include <boost/asio.hpp>  // required for UDP
#include <ctime>

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

int main(int argc, char** argv)
{
    // UDP  
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

    // String delimiter
    std::string delimiter = ",";

    boost::asio::io_context io_context;
    boost::asio::ip::udp::socket socket1(io_context);
    boost::asio::ip::udp::socket socket2(io_context);

    // Bind the first socket to port 5100
    boost::asio::ip::udp::endpoint receiver_endpoint1(boost::asio::ip::make_address(IP_ADDR), 5100);
    socket1.open(boost::asio::ip::udp::v4());
    socket1.bind(receiver_endpoint1);

    // Bind the second socket to port 5101
    boost::asio::ip::udp::endpoint receiver_endpoint2(boost::asio::ip::make_address(IP_ADDR), 5101);
    socket2.open(boost::asio::ip::udp::v4());
    socket2.bind(receiver_endpoint2);

    std::array<char, MAX_BUFFER_SIZE> buffer;

    std::ofstream outputFile;
    outputFile.open("received_data.csv");
    outputFile << "timestamp, orientation_x, orientation_y, joystick_action, joystick_state" << std::endl;

    const int screenWidth = 900; //800;
    const int screenHeight = 600; //450;

    //SetConfigFlags(FLAG_MSAA_4X_HINT | FLAG_WINDOW_HIGHDPI);
    InitWindow(screenWidth, screenHeight, "Plane rotation (yaw, pitch, roll) with Sense Hat controller");

    Camera camera = { 0 };
    camera.position = (Vector3){ 0.0f, 60.0f, -100.0f };// Camera position perspective
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

    // Main game loop
    while (!WindowShouldClose())    // Detect window close button or ESC key
    {
        // UDP

        // Receive UDP data from game controller
        boost::asio::ip::udp::endpoint sender_endpoint;
        size_t length;

        // Timestamp 
        time_t now = time(0);

        // convert now to string form
        std::string date_time = ctime(&now);

        // Receive from socket1
        length = socket1.receive_from(boost::asio::buffer(buffer), sender_endpoint);
        std::string orientation_data(buffer.data(), length);

        // Split string
        std::vector<std::string> orientation = split(orientation_data, delimiter);
        std::string orientation_x = orientation[0];
        std::string orientation_y = orientation[1];

        // Print to console
        std::cout << orientation_data << std::endl;
        std::cout << orientation_x << ", " << orientation_y << std::endl;

        // Receive from socket2
        length = socket2.receive_from(boost::asio::buffer(buffer), sender_endpoint);
        std::string joystick_data = std::string(buffer.data(), length);

        // Split string
        std::vector<std::string> joystick = split(joystick_data, delimiter);
        std::string joystick_action = joystick[0];
        std::string joystick_state = joystick[1];

        // Print to console
        std::cout << joystick_data << std::endl;
        std::cout << joystick_action << ", " << joystick_state << std::endl;

        // Log to csv file
        outputFile << "\"" << date_time << "\", " << orientation_x << ", " << orientation_y << ", " << joystick_action << ", " << joystick_state << std::endl;

        //
        pitch = -std::stof(orientation_x);
        roll = std::stof(orientation_y);

        // Tranformation matrix for rotations
        model.transform = MatrixRotateXYZ((Vector3){ DEG2RAD*pitch, DEG2RAD*yaw, DEG2RAD*roll });

        BeginDrawing();

            ClearBackground(BLACK);

            BeginMode3D(camera);

                DrawModel(model, (Vector3){ 0.0f, 0.0f, 0.0f }, 1.0f, WHITE);   // Draw 3d model with texture
                DrawGrid(100, 100.0f);

            EndMode3D();
            
            DrawText("UDP Receiver", 10, 10, 20, DARKGRAY);
            DrawText(orientation_data.c_str(), 10, 40, 20, BLACK);
            DrawText(joystick_data.c_str(), 10, 70, 20, BLACK);
            DrawText("(c) WWI Plane Model created by GiaHanLam", screenWidth - 240, screenHeight - 20, 10, DARKGRAY);

        EndDrawing();
    }

    // Cleanup
    outputFile.close();
    
    UnloadModel(model);     // Unload model data

    CloseWindow();          // Close window and OpenGL context

    return 0;
}
