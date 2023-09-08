/*
    This program is intended to run on a Raspberry Pi with WiFi access and a Sense Hat module installed.  
    It sends orientation data and joystick events to a Unity game on the same wlan via UDP.

    Links:
    sensehat library: https://github.com/platu/libsensehat-cpp
    boost library: https://www.boost.org/
*/

#include <boost/asio.hpp>
#include <sensehat.h>
#include <thread> 
#include <iostream>
#include <string>
#include <chrono>

using namespace std;
using namespace boost::asio;

struct joystickState {
    std::string action;
    std::string state;
};

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

joystickState GetJoystickInput() {
    
    stick_t joystick;
    joystickState joystickState;

    senseSetJoystickWaitTime(0, 20);
	bool clicked = senseGetJoystickEvent(joystick);
    
    if (clicked) {

        // Action is inverted because the joystick is mounted upside down
        switch (joystick.action) {
            case KEY_ENTER:	joystickState.action = "push";  break;
            case KEY_UP:	joystickState.action = "down";  break;
            case KEY_LEFT:	joystickState.action = "right"; break;
            case KEY_RIGHT:	joystickState.action = "left";  break;
            case KEY_DOWN:	joystickState.action = "up";    break;
            default:		joystickState.action = "none";  break;
        }

        switch(joystick.state) {
            case KEY_RELEASED: joystickState.state = "released"; break;
            case KEY_PRESSED:  joystickState.state = "pressed";  break;
            case KEY_HELD:     joystickState.state = "held";     break;
            default:           joystickState.state = "none";     break;
        }

        return joystickState;

    } else {

        joystickState.action = "none";
        joystickState.state = "none";

        return joystickState;
    }
}

// main takes the UDP IPv4 address as an argument
int main(int argc, char* argv[]) {

    std::string ip = "";
    
    // Set ip to argument value if provided
    if (argc == 2) {
        std::string arg = argv[1];

        cout << "IP: " << arg << endl;

        ip = arg;
    } else {
        return EXIT_FAILURE;
    }
    
    std::string orientation_port = "5100";
    std::string joystick_port = "5101";

    io_service io_service;

    ip::udp::resolver resolver(io_service);
    
    ip::udp::resolver::query orientationQuery(ip::udp::v4(), ip, orientation_port);
    ip::udp::resolver::query joystickQuery(ip::udp::v4(), ip, joystick_port);
    
    ip::udp::endpoint orientation_endpoint = *resolver.resolve(orientationQuery);
    ip::udp::endpoint joystick_endpoint = *resolver.resolve(joystickQuery);

    ip::udp::socket socket(io_service);

    socket.open(ip::udp::v4());

    if(ConnectSenseHat()) {

        // TODO: exit program if joystick is clicked?
        while(true) {
            
            string orientationMessage = GetOrientationData();
            joystickState joystickEvent = GetJoystickInput();

            socket.send_to(buffer(orientationMessage, orientationMessage.size()), orientation_endpoint);
            socket.send_to(buffer(joystickEvent.action + "," + joystickEvent.state, joystickEvent.action.size() + joystickEvent.state.size() + 1), joystick_endpoint);
            //socket.send_to(buffer(joystickEvent.action + "," + joystickEvent.state, joystickEvent.action.size() + 1 + joystickEvent.state.size() + 1), joystick_endpoint);

            this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }

    senseShutdown();

    return EXIT_SUCCESS;
}
