#include <stdio.h>
#include <stdlib.h>
#include <winsock.h>

typedef struct UDPSocketData
{
    int socket;
    struct sockaddr_in address;
} UDPSocketData;

void error(char *msg) {
    perror(msg);
    exit(0);
}

int initSocket() {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0)
        error("socket");
    return sock;
}

void InitWSA() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0)
        error("Error initializing the Windows Sockets Library");
}

void checkArguments(int argc, char* argv[]) {
    if (argc != 3)
    {
        printf("Usage: %s <server_name> <port>\n",argv[0]);
        exit(1);
    }
}

void initServerAddress(const char* serverAddress, const char* serverPort, struct sockaddr_in *server) {
    struct hostent *hp; // DNS stuff
    (*server).sin_family = AF_INET;
    hp = gethostbyname(serverAddress);

    if (hp == 0)
        error("Unknown host");

    memcpy((char *)&(*server).sin_addr, (char *)hp->h_addr, hp->h_length);
    (*server).sin_port = htons(atoi(serverPort));
}

void clientCode(UDPSocketData* socketData) {
    char buffer[256];
    int length = sizeof(struct sockaddr_in);
    struct sockaddr_in from;
    int ret;

    printf("Please enter the message: ");
    memset((void*)buffer, 0, 256);
    scanf("%s", buffer);
    ret = sendto(socketData->socket, buffer, strlen(buffer), 0, (struct sockaddr*) &socketData->address, length);

    if (ret < 0) error("Sendto");

    ret = recvfrom(socketData->socket, buffer, 256, 0, (struct sockaddr*) &from, &length);

    if (ret < 0) error("recvfrom");

    printf("Got an ack: ");
    printf("%s", buffer);
}

UDPSocketData createSocketData(const char* serverAddress, const char* serverPort)
{
    UDPSocketData socketData;
    socketData.socket = initSocket();
    initServerAddress(serverAddress, serverPort, &socketData.address);

    return socketData;
}

int main(int argc, char *argv[])
{
    InitWSA();

    checkArguments(argc, argv);
    UDPSocketData socketData = createSocketData(argv[1], argv[2]);

    clientCode(&socketData);

    return 0;
}

