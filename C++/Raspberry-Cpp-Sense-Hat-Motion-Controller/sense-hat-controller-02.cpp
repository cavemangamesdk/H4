/*
* Source: https://github.com/platu/libsensehat-cpp
*/

#include <boost/asio.hpp>
#include <sensehat.h>
#include <thread>
#include <iostream>
#include <string>
#include <chrono>

using namespace std;
using namespace boost::asio;

bool ConnectSenseHat() {
    bool status = senseInit();
    senseClear();
    senseSetIMUConfig(true, true, true);
    return status;
}

string GetOrientationData() {
    double x, y ,z;
    senseGetOrientationDegrees(x, y, z);
    return to_string(-x) + "," + to_string(y);
}

int main() {
    io_service io_service;

    ip::udp::resolver resolver(io_service);
    ip::udp::resolver::query query(ip::udp::v4(), "192.168.109.1", "5100");
    ip::udp::endpoint receiver_endpoint = *resolver.resolve(query);

    ip::udp::socket socket(io_service);
    socket.open(ip::udp::v4());

    if(ConnectSenseHat()) {
        while(true) {
            string message = GetOrientationData();

            socket.send_to(buffer(message, message.size()), receiver_endpoint);
            
            // Adding sleep for a while, to not overwhelm the network or CPU. 
            // You can modify this sleep duration or remove it as per your requirement.
            this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }

    senseShutdown();

    return EXIT_SUCCESS;
}
