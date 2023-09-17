#include <iostream>
#include <fstream>
#include <boost/asio.hpp>

using namespace std;
using namespace boost::asio;

struct JoystickEvent {
  string action;
  string state;
};

void saveToCSV(const string& filename, const string& data) {
  ofstream file(filename, ios::app);
  if (file.is_open()) {
    file << data << endl;
    file.close();
  } else {
    cerr << "Failed to open " << filename << " for writing" << endl;
  }
}

int main() {
  boost::asio::io_service io_service;
  ip::udp::socket socket(io_service);
  ip::udp::endpoint remote_endpoint;
  
  socket.open(ip::udp::v4());
  socket.bind(ip::udp::endpoint(ip::udp::v4(), 5100));
  
  ofstream outputFile("output.csv");

  // Buffer for receiving data
  char buffer[1024];
  
  while (true) {
    memset(buffer, 0, sizeof(buffer));
    size_t length = socket.receive_from(buffer, sizeof(buffer), remote_endpoint);

    // Convert received data to string
    string receivedData(buffer, buffer + length);

    // Parsing received data into orientation and joystick
    string orientationData = receivedData.substr(0, receivedData.find(","));
    string joystickData = receivedData.substr(receivedData.find(",") + 1);

    // Print received data to console
    cout << "Received Orientation: " << orientationData << endl;
    cout << "Received Joystick: " << joystickData << endl;

    // Save received data to CSV file
    saveToCSV("output.csv", receivedData);
  }

  socket.close();

  return 0;
}
