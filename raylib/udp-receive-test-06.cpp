#include <iostream>
#include <string>
#include <fstream>
#include <boost/asio.hpp>

#define MAX_BUFFER_SIZE 1024

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

    while (true) {
        boost::asio::ip::udp::endpoint sender_endpoint;
        size_t length;

        // Receive from socket1
        length = socket1.receive_from(boost::asio::buffer(buffer), sender_endpoint);
        std::string received_data(buffer.data(), length);
        std::cout << "Received data from " << sender_endpoint.address() << ":" << sender_endpoint.port()
                  << " (Port 5100): " << received_data << std::endl;
        outputFile << "5100," << received_data << std::endl;

        // Receive from socket2
        length = socket2.receive_from(boost::asio::buffer(buffer), sender_endpoint);
        received_data = std::string(buffer.data(), length);
        std::cout << "Received data from " << sender_endpoint.address() << ":" << sender_endpoint.port()
                  << " (Port 5101): " << received_data << std::endl;
        outputFile << "5101," << received_data << std::endl;
    }

    outputFile.close();

    return 0;
}
