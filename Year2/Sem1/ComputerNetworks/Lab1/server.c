// exists on all platforms

#include <stdio.h>

// this section will only be compiled on NON Windows platforms

#ifndef _WIN32

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h>
#include <stdlib.h>

#define closesocket close

typedef int SOCKET;

#else
// on Windows include and link these things
#include <WinSock2.h>
// for uint16_t an so
#include <cstdint>
// this is how we can link a library directly from the source code with the VC++ compiler – otherwise got o project settings and link to it explicitly
//#pragma comment(lib,"Ws2_32.lib")

#endif

#define NO_FLAGS 0

void init_socket(SOCKET* sock)
{
    *sock = socket(AF_INET, SOCK_STREAM, 0);
    if (*sock < 0)
    {
        printf("Eroare la crearea socketului client\n");
        exit(1);
    }

    printf("Socket created\n");
}

void init_server(struct sockaddr_in* server)
{
    memset(server, 0, sizeof(struct sockaddr_in));
    server->sin_port = htons(1234);
    server->sin_family = AF_INET;
    server->sin_addr.s_addr = INADDR_ANY;

    printf("Server created\n");
}

void bind_socket_and_listen(SOCKET sock, struct sockaddr_in* server)
{
    if (bind(sock, (struct sockaddr*)server, sizeof(struct sockaddr_in)) < 0)
    {
        perror("Bind error:");
        exit(1);
    }
    listen(sock, 5);

    printf("Socket bound and called listen\n");
}

void init_client(struct sockaddr_in* client, unsigned int* client_length)
{
    *client_length = sizeof(client);
    memset(&client, 0, sizeof(client));

    printf("Constructed client\n");
}

void connect_to_client(SOCKET sock, struct sockaddr_in* client, unsigned int* client_length, SOCKET* connection)
{
    printf("Listening for incoming connections\n");
    *connection = accept(sock, (struct sockaddr *)client, client_length);
    int err = errno;
#ifdef _WIN32
    err = WSAGetLastError();
#endif
    if (*connection < 0)
    {
        printf("accept error: %d", err);
        return;
    }
    printf("Incoming connected client from: %s:%d\n", inet_ntoa(client->sin_addr), ntohs(client->sin_port));
}

int receive_length(SOCKET connection, uint32_t* length)
{
    printf("Waiting for length... ");
    if (recv(connection, (char*)length, sizeof(uint32_t), NO_FLAGS) < 0)
    {
        return -1;
    }
    printf("DONE (received: %u)\n", *length);

    return 0;
}

int receive_message(SOCKET connection, char* message, uint32_t expected_length)
{
    printf("Waiting for message... ");
    recv(connection, message, expected_length, NO_FLAGS);
    printf("DONE (received: %s)\n", message);

    return strlen(message);
}

void reverse_message(char* message, char* reversed_message, uint32_t length)
{
    for (unsigned int i = 0; i < length; ++i)
    {
        reversed_message[i] = message[length - i - 1];
    }
    reversed_message[length] = '\0';

    printf("Reversed message is: %s\n", reversed_message);
}

int send_message(SOCKET connection, char* message, uint32_t length)
{
    printf("Sending message back... ");
    return send(connection, message, length, NO_FLAGS);
}

int send_reversed_message(SOCKET connection, char* message, uint32_t length)
{
    char reversed_message[100] = "";
    reverse_message(message, reversed_message, length);

    return send_message(connection, reversed_message, length);
}

void serve_client(SOCKET connection)
{
    char message[100] = "";
    uint32_t length;
    if (receive_length(connection, &length) < 0)
    {
        printf("Couldn't receive message size :(\n");
        return;
    }
    if (receive_message(connection, message, length) != length)
    {
        printf("Couldn't receive entire message :(\n");
        return;
    }
    if (send_reversed_message(connection, message, length) < 0)
    {
        printf("Couldn't respond to client :(\n");
        return;
    }
    else
    {
        printf("SENT\n");
    }
}

void loop(SOCKET sock, struct sockaddr_in* client, unsigned int* client_length)
{
    SOCKET connection;
    connect_to_client(sock, client, client_length, &connection);
    int pid = fork();
    if (pid == 0)
    {
        serve_client(connection);
        closesocket(connection);
        exit(0);
    }
    else if (pid < 0)
    {
        perror("Couldn't create child process");
        exit(1);
    }
    

    closesocket(connection);
}

int main()
{
    SOCKET sock;
    struct sockaddr_in server, client;
    unsigned int client_length;

    // initialize the Windows Sockets LIbrary only when compiled on Windows
#ifdef _WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0)
    {
        printf("Error initializing the Windows Sockets LIbrary");
        return -1;
    }
#endif

    init_socket(&sock);
    init_server(&server);
    bind_socket_and_listen(sock, &server);
    init_client(&client, &client_length);
    
    while (1)
    {
        loop(sock, &client, &client_length);
    }
    // never reached
    // Release the Windows Sockets Library
#ifdef WIN32
    WSACleanup();
#endif
}