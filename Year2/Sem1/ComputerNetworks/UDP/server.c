#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef WIN32
#include <winsock.h>
#else
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#endif

#define NO_FLAGS 0

void error(char *msg) {
    perror(msg);
    exit(0);
}

void checkArguments(int argc)
{
    if (argc < 2)
        error("No port provided");
}

int initSocket()
{
    int sock = socket(AF_INET, SOCK_DGRAM, NO_FLAGS);
    if (sock < 0)
        error("Could not open socket");
}

void initServerSocketAddress(struct sockaddr_in* serverAddress, int* length, char* argv[])
{
    *length = sizeof(*serverAddress);
    memset(serverAddress, 0, *length);
    serverAddress->sin_family = AF_INET;
    serverAddress->sin_addr.s_addr = INADDR_ANY;
    serverAddress->sin_port = htons(atoi(argv[1]));
}

void bindSocketToAddress(int socket, struct sockaddr_in* serverAddress, int length)
{
    if (bind(socket, (struct sockaddr *)serverAddress, length) < 0)
        error("Could not bind address to socket");
}

void receiveMessage(int sock, char* buffer, struct sockaddr_in* client, int* clientLength)
{
    int ret = recvfrom(sock, buffer, 1024, NO_FLAGS, (struct sockaddr *)client, clientLength);
    if (ret < 0)
        error("Could not receive message");
}

void processRequest(char* request, char* response)
{
    sprintf(response, "Received message: %s", request);
}

void sendResponse(int sock, char* response, struct sockaddr_in* client, int clientLength)
{
    int ret = sendto(sock, response, strlen(response), NO_FLAGS, (struct sockaddr*)client, clientLength);
    if (ret < 0)
        error("Could not send response to client");
}

void loop(int sock)
{
    int clientLength;
    struct sockaddr_in client;
    char buffer[1024], response[1024];
    clientLength = sizeof(client);

    receiveMessage(sock, buffer, &client, &clientLength);

    printf("Received a datagram: %s\n", buffer);
    processRequest(buffer, response);

    sendResponse(sock, response, &client, clientLength);
}

int main(int argc, char *argv[]) {
    int sock, length;
    struct sockaddr_in server;

    checkArguments(argc);
    sock = initSocket();
    initServerSocketAddress(&server, &length, argv);
    bindSocketToAddress(sock, &server, length);

    while (1)
        loop(sock);
}