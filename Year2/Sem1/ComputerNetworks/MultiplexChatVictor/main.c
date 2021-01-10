#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdbool.h>
#include <memory.h>
#include <unistd.h>

#define NO_FLAGS 0
#define BUFFER_SIZE 1024

typedef struct sockaddr_in SocketAddress;

typedef struct TCPSocketData
{
    int socket;
    SocketAddress address;
    socklen_t length;
} TCPSocketData;

typedef struct ServerState
{
    struct TCPSocketData serverSocket;
    fd_set fileDescriptors;
    int connections;
    int maxFileDescriptor;
} ServerState;

void error(char* message)
{
    perror(message);
    exit(1);
}

void warning(char* message)
{
    printf("Warn: %s\n", message);
}

void checkArguments(int argc, char* argv[])
{
    if (argc != 2)
        error("Please provide a port");
}

SocketAddress createSocketAddress(char* port)
{
    SocketAddress socketAddress;
    socketAddress.sin_addr.s_addr = INADDR_ANY;
    socketAddress.sin_port = htons(atoi(port));
    socketAddress.sin_family = AF_INET;

    return socketAddress;
}

struct TCPSocketData createTCPSocketData(char* port)
{
    struct TCPSocketData tcpSocketData;
    tcpSocketData.socket = socket(AF_INET, SOCK_STREAM, 0);
    tcpSocketData.address = createSocketAddress(port);
    tcpSocketData.length = sizeof(tcpSocketData.address);

    if (bind(tcpSocketData.socket, (const struct sockaddr*)&tcpSocketData.address, tcpSocketData.length) < 0)
        error("Bind failed");

    if (listen(tcpSocketData.socket, 10) < 0)
        error("Listen failed");

    int yes = 1;
    if (setsockopt(tcpSocketData.socket, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int) ) == -1) {
        perror("setsockopt:");
        exit(1);
    }

    return tcpSocketData;
}

bool isReadable(const fd_set *fileDescriptors, int fileDescriptor)
{
    return FD_ISSET(fileDescriptor, fileDescriptors);
}

TCPSocketData createClientSocket(int serverSocket)
{
    TCPSocketData clientSocketData;
    clientSocketData.length = sizeof(struct sockaddr_in);
    int sock = accept(
            serverSocket,
            (struct sockaddr*)&clientSocketData.address, &clientSocketData.length);

    if (sock < 0)
        error("Accept failed");

    clientSocketData.socket = sock;

    return clientSocketData;
}

void initServerState(ServerState* serverState, char* port)
{
    serverState->serverSocket = createTCPSocketData(port);
    serverState->connections = 0;
    serverState->maxFileDescriptor = serverState->serverSocket.socket;
    FD_ZERO(&serverState->fileDescriptors);
    FD_SET(serverState->serverSocket.socket, &serverState->fileDescriptors);
}

void newClientConnected(ServerState *serverState)
{
    // new connection
    TCPSocketData clientSocketData = createClientSocket(serverState->serverSocket.socket);
    ++serverState->connections;

    if (clientSocketData.socket > serverState->maxFileDescriptor)
        serverState->maxFileDescriptor = clientSocketData.socket;

    FD_SET(clientSocketData.socket, &serverState->fileDescriptors);

    char welcomeMessage[BUFFER_SIZE];
    sprintf(welcomeMessage,
            "Welcome, user! There are currently %d users in the chat\n",
            serverState->connections);
    send(clientSocketData.socket, welcomeMessage, strlen(welcomeMessage), NO_FLAGS);
}

void removeUserConnection(ServerState* serverState, int clientSocket)
{
    FD_CLR(clientSocket, &serverState->fileDescriptors);
    close(clientSocket);
    --serverState->connections;
}

void sendMessageToOthers(char* message, ServerState* serverState, int clientSocket)
{
    for (int socket = 0; socket <= serverState->maxFileDescriptor; ++socket)
        if (FD_ISSET(socket, &serverState->fileDescriptors))
            if (socket != serverState->serverSocket.socket && socket != clientSocket)
                send(socket, message, strlen(message), NO_FLAGS);
}

void handleReceiveError(ServerState *serverState, int clientSocket, int receivedBytes)
{
    if (receivedBytes == 0)
        warning("User left");
    else
        warning("Receive failed");
    removeUserConnection(serverState, clientSocket);
}

void handleUserQuit(ServerState *serverState, int clientSocket, char *message)
{
    warning("User left");
    sprintf(message, "User %d left", clientSocket);
    sendMessageToOthers(message, serverState, clientSocket);
    removeUserConnection(serverState, clientSocket);
}

void forwardClientMessage(ServerState *serverState, int clientSocket, const char *buffer, char *message)
{
    sprintf(message, "User %d: %s", clientSocket, buffer);
    sendMessageToOthers(message, serverState, clientSocket);
}

void handleReceiveSuccess(ServerState *serverState, int clientSocket, char *buffer, int receivedBytes)
{
    char message[1024];
    buffer[receivedBytes] = 0; // make sure string is null-terminated
    if (strncasecmp("QUIT", buffer, 4) == 0) {
        handleUserQuit(serverState, clientSocket, message);
    }
    else {
        forwardClientMessage(serverState, clientSocket, buffer, message);
    }
}

void processClientRequest(ServerState* serverState, int clientSocket)
{
    char buffer[BUFFER_SIZE];
    int receivedBytes = recv(clientSocket, buffer, BUFFER_SIZE, NO_FLAGS);
    if (receivedBytes <= 0) {
        handleReceiveError(serverState, clientSocket, receivedBytes);
    }
    else {
        handleReceiveSuccess(serverState, clientSocket, buffer, receivedBytes);
    }
}

void findRequestingClient(ServerState *serverState)
{
    fd_set fileDescriptorsRead = serverState->fileDescriptors;
    if (select(serverState->maxFileDescriptor + 1, &fileDescriptorsRead, NULL, NULL, NULL) < 0)
        error("Select failed");

    for (int fileDescriptor = 0; fileDescriptor <= serverState->maxFileDescriptor; ++fileDescriptor)
        if (isReadable(&fileDescriptorsRead, fileDescriptor)) {
            if (fileDescriptor == serverState->serverSocket.socket) {
                newClientConnected(serverState);
            }
            else {
                processClientRequest(serverState, fileDescriptor);
            }
        }
}

void loop(ServerState* serverState) {
    findRequestingClient(serverState);
}

int main(int argc, char* argv[])
{
    checkArguments(argc, argv);

    ServerState serverState;
    initServerState(&serverState, argv[1]);

    int yes = 1;
    if (setsockopt(serverState.serverSocket.socket, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int) ) == -1) {
        perror("setsockopt:");
        exit(1);
    }

    while(1)
    {
        loop(&serverState);
    }
}
