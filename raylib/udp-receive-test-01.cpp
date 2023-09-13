#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <fstream>
#include <cstring>

#define BUFLEN 512
#define PORT 5100

int main(void)
{
    struct sockaddr_in si_me, si_other;
    int s, slen = sizeof(si_other);
    char buf[BUFLEN];

    if ((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
    {
        perror("socket");
        return 1;
    }

    memset((char *) &si_me, 0, sizeof(si_me));
    si_me.sin_family = AF_INET;
    si_me.sin_port = htons(PORT);
    si_me.sin_addr.s_addr = htonl(INADDR_ANY);
    if (bind(s, (struct sockaddr*)&si_me, sizeof(si_me)) == -1)
    {
        perror("bind");
        return 1;
    }

    std::ofstream outputFile("output.csv");

    while(1)
    {
        if (recvfrom(s, buf, BUFLEN, 0, (struct sockaddr*)&si_other, (socklen_t*)&slen) == -1)
        {
            perror("recvfrom");
            return 1;
        }

        outputFile << buf << std::endl;
    }

    close(s);
    return 0;
}
