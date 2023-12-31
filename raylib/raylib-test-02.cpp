#include <iostream>
#include <string>
#include <fstream>
#include <raylib.h>
#include <boost/asio.hpp>

#define MAX_BUFFER_SIZE 1024
#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600

int main() {
    

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

    std::array<char, MAX_BUFFER_SIZE> buffer;

    std::ofstream outputFile;
    outputFile.open("received_data.csv");

     // Initialization
    //--------------------------------------------------------------------------------------
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "UDP Receiver");

    // Define the camera to look into our 3d world
    Camera3D camera = { 0 };
    camera.position = (Vector3){ 10.0f, 10.0f, 10.0f }; // Camera position
    camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };      // Camera looking at point
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };          // Camera up vector (rotation towards target)
    camera.fovy = 45.0f;                                // Camera field-of-view Y
    camera.projection = CAMERA_PERSPECTIVE;             // Camera projection type

    Vector3 cubePosition = { 0.0f, 0.0f, 0.0f };

    DisableCursor();                    // Limit cursor to relative movement inside the window

    SetTargetFPS(60);                   // Set our game to run at 60 frames-per-second
    //--------------------------------------------------------------------------------------

    // String delimiter
    std::string delimiter = ",";

    while (!WindowShouldClose()) {
        
        // Receive UDP data from game controller
        boost::asio::ip::udp::endpoint sender_endpoint;
        size_t length;

        // Receive from socket1
        length = socket1.receive_from(boost::asio::buffer(buffer), sender_endpoint);
        std::string orientation_data(buffer.data(), length);

        std::string x = orientation_data.substr(0, orientation_data.find(delimiter));
        std::string y = orientation_data.substr(1, orientation_data.find(delimiter));

        std::cout << x << ", " << y << std::endl;

        // std::cout << "Received data from " << sender_endpoint.address() << ":" << sender_endpoint.port()
        //         << " (Port 5100): " << orientation_data << std::endl;
        //outputFile << "5100," << orientation_data << std::endl;

        // Receive from socket2
        length = socket2.receive_from(boost::asio::buffer(buffer), sender_endpoint);
        std::string joystick_data = std::string(buffer.data(), length);

        std::string action = joystick_data.substr(0, joystick_data.find(delimiter));
        std::string state = joystick_data.substr(1, joystick_data.find(delimiter));

        std::cout << action << ", " << state << std::endl;

        // std::cout << "Received data from " << sender_endpoint.address() << ":" << sender_endpoint.port()
        //         << " (Port 5101): " << joystick_data << std::endl;
        //outputFile << "5101," << joystick_data << std::endl;
    
        
        UpdateCamera(&camera, CAMERA_FREE);
        
        camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };
        
        // joystick_data case
        if(action == "up") {
            camera.fovy += 1.0f;
        }

        if(action == "down") {
            camera.fovy -= 1.0f;
        }
        
        BeginDrawing();
            
            ClearBackground(RAYWHITE);

            BeginMode3D(camera);

                DrawCube(cubePosition, 2.0f, 2.0f, 2.0f, RED);
                DrawCubeWires(cubePosition, 2.0f, 2.0f, 2.0f, MAROON);

                DrawGrid(10, 1.0f);

            EndMode3D();

            DrawText("UDP Receiver", 10, 10, 20, DARKGRAY);
            DrawText(orientation_data.c_str(), 10, 40, 20, BLACK);
            DrawText(joystick_data.c_str(), 10, 70, 20, BLACK);

        EndDrawing();
    }

    outputFile.close();
    CloseWindow();

    return 0;
}
