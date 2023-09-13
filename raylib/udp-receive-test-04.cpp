#include <iostream>
#include <string>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <cstring>
#include <unistd.h>

#define MAX_BUFFER_SIZE 1024

int main() {
    int sockfd;
    struct sockaddr_in recvAddr, senderAddr;
    char buffer[MAX_BUFFER_SIZE];

    // Create a UDP socket
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&recvAddr, 0, sizeof(recvAddr));
    memset(&senderAddr, 0, sizeof(senderAddr));

    // Receiver information
    recvAddr.sin_family = AF_INET; // IPv4
    recvAddr.sin_addr.s_addr = inet_addr("192.168.109.243"); // Replace with your desired IP address
    recvAddr.sin_port = htons(5101); // Replace with your desired port number

    // Bind the socket with the receiver address
    if (bind(sockfd, (const struct sockaddr *)&recvAddr, sizeof(recvAddr)) < 0) {
        perror("bind failed");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    while (true) {
        int len, n;
        len = sizeof(senderAddr);

        // Receive data
        n = recvfrom(sockfd, (char *)buffer, MAX_BUFFER_SIZE, 0, (struct sockaddr *)&senderAddr, (socklen_t *)&len);
        buffer[n] = '\0';

        // Print the received data
        std::cout << "Received data from " << inet_ntoa(senderAddr.sin_addr) << ":" << ntohs(senderAddr.sin_port)
                  << " - " << buffer << std::endl;
    }

    close(sockfd);

    return 0;
}
