#include <boost/asio.hpp>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace boost::asio;
using boost::asio::ip::udp;

struct JoystickEvent {
    std::string action;
    std::string state;
};

void handleOrientationData(const std::string& data) {
    // Parse the orientation data
    std::istringstream iss(data);
    double x, y;
    char comma;
    iss >> x >> comma >> y;

    // Print to console
    std::cout << "Received orientation data: x = " << x << ", y = " << y << std::endl;

    // Write to CSV file
    std::ofstream file("orientation_data.csv", std::ios_base::app);
    file << std::fixed << std::setprecision(2) << x << "," << y << std::endl;
}

void handleJoystickEvent(const std::string& data) {
    // Parse the joystick event
    std::istringstream iss(data);
    std::string action, state;
    char comma;
    std::getline(iss, action, ',');
    std::getline(iss, state);

    // Print to console
    std::cout << "Received joystick event: action = " << action << ", state = " << state << std::endl;

    // Write to CSV file
    std::ofstream file("joystick_event.csv", std::ios_base::app);
    file << action << "," << state << std::endl;
}

int main() {
    io_service io_service;
    udp::socket socket(io_service, udp::endpoint(udp::v4(), 5100));

    while (true) {
        char data[1024];
        udp::endpoint sender_endpoint;
        size_t length = socket.receive_from(buffer(data, 1024), sender_endpoint);
        std::string message(data, length);

        // Check whether the message is orientation data or joystick event
        if (sender_endpoint.port() == 5100) {
            handleOrientationData(message);
        } else if (sender_endpoint.port() == 5101) {
            handleJoystickEvent(message);
        }
    }

    return 0;
}
