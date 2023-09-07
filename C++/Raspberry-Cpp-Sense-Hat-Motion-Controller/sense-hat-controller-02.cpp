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
    senseSetJoystickWaitTime(0, 20);
	bool clicked = senseGetJoystickEvent(joystick);
    if (clicked) {

        joystickState joystickState;

        // Identify action on stick
        switch (joystick.action) {
            case KEY_ENTER:	joystickState.action = "push  "; break;
            case KEY_UP:	joystickState.action = "up    "; break;
            case KEY_LEFT:	joystickState.action = "left  "; break;
            case KEY_RIGHT:	joystickState.action = "right "; break;
            case KEY_DOWN:	joystickState.action = "down  "; break;
            // case else
            default:		joystickState.action = "none  "; break;
        }

        // Identify state of stick
        switch(joystick.state) {
            case KEY_RELEASED:	joystickState.state = "released"; break;
            case KEY_PRESSED:	joystickState.state = "pressed"; break;
            case KEY_HELD:		joystickState.state = "held"; break;
            // case else
            default:			joystickState.state = "none"; break;
        }

        return joystickState;

    } else {
        joystickState joystickState;
        joystickState.action = "none  ";
        joystickState.state = "none";
        return joystickState;
    }
    //sleep_until(system_clock::now() + milliseconds(20));
}

int main() {
    
    std::string ip = "192.168.109.1";
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
        while(true) {
            
            string orientationMessage = GetOrientationData();
            joystickState joystickEvent = GetJoystickInput();

            socket.send_to(buffer(orientationMessage, orientationMessage.size()), orientation_endpoint);
            socket.send_to(buffer(joystickEvent.action + "," + joystickEvent.state, joystickEvent.action.size() + joystickEvent.state.size()), joystick_endpoint);

            //socket.send_to(buffer(to_string(joystickEvent.timestamp) + "," + to_string(joystickEvent.type) + "," + to_string(joystickEvent.code) + "," + to_string(joystickEvent.value), 100), joystick_endpoint);
            
            // Adding sleep for a while, to not overwhelm the network or CPU. 
            // You can modify this sleep duration or remove it as per your requirement.
            this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }

    senseShutdown();

    return EXIT_SUCCESS;
}
