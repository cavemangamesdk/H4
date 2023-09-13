#include <iostream>
#include <fstream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <cstring>
#include <regex>

#define BUFLEN 512
#define PORT 5100

std::string cleanPacket(const std::string& packet) {
    std::regex reg("([+-]?\\d+\\.\\d{2})");
    std::sregex_iterator currentMatch(packet.begin(), packet.end(), reg);
    std::sregex_iterator lastMatch;

    std::string cleanedPacket;
    for (; currentMatch != lastMatch; ++currentMatch) {
        cleanedPacket += currentMatch->str() + ",";
    }
    cleanedPacket.pop_back(); // Remove the trailing comma

    return cleanedPacket;
}

int main(void)
{
    struct sockaddr_in si_me, si_other;
    int s, slen = sizeof(si_other);
    char buf[BUFLEN];

    if ((s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
    {
        perror("socket");
        return 1;
    }

    memset((char *)&si_me, 0, sizeof(si_me));
    si_me.sin_family = AF_INET;
    si_me.sin_port = htons(PORT);
    si_me.sin_addr.s_addr = htonl(INADDR_ANY);
    
    if (bind(s, (struct sockaddr *)&si_me, sizeof(si_me)) == -1)
    {
        perror("bind");
        return 1;
    }

    std::ofstream outputFile("output.csv");

    while (1)
    {
        if (recvfrom(s, buf, BUFLEN, 0, (struct sockaddr *)&si_other, (socklen_t *)&slen) == -1)
        {
            perror("recvfrom");
            close(s);
            return 1;
        }

        std::string packet(buf);
        std::string cleanedPacket = cleanPacket(packet);

        std::cout << "Received packet: " << cleanedPacket << std::endl;
        outputFile << cleanedPacket << std::endl;
    }

    close(s);
    return 0;
}
