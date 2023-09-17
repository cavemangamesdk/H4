#include <iostream>
#include <string>
#include <boost/asio.hpp>

#define MAX_BUFFER_SIZE 1024

int main() {
    boost::asio::io_context io_context;
    boost::asio::ip::udp::socket socket(io_context);
    boost::asio::ip::udp::endpoint receiver_endpoint(boost::asio::ip::make_address("192.168.109.243"), 5100); // Replace with your desired IP address and port

    socket.open(boost::asio::ip::udp::v4());
    socket.bind(receiver_endpoint);

    std::array<char, MAX_BUFFER_SIZE> buffer;

    while (true) {
        boost::asio::ip::udp::endpoint sender_endpoint;
        size_t length = socket.receive_from(boost::asio::buffer(buffer), sender_endpoint);

        std::string received_data(buffer.data(), length);
        std::cout << "Received data from " << sender_endpoint.address() << ":" << sender_endpoint.port()
                  << " - " << received_data << std::endl;
    }

    return 0;
}
