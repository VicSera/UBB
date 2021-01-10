#include <sys/types.h>
#include <stdio.h>
#include <string.h>
#include <WinSock2.h>
#include <stdint.h>
#include <io.h>

#define NO_FLAGS 0

void init_server(struct sockaddr_in* server)
{
    memset(server, 0, sizeof(struct sockaddr_in));
    server->sin_port = htons(1234);
    server->sin_family = AF_INET;
    server->sin_addr.s_addr = inet_addr("192.168.100.145");
}

void init_socket(SOCKET* sock)
{
    *sock = socket(AF_INET, SOCK_STREAM, 0);
    if (*sock < 0)
    {
        printf("Eroare la crearea socketului client\n");
        exit(1);
    }
}

void connect_socket_to_server(SOCKET sock, struct sockaddr_in* server)
{
    if (connect(sock, (const struct sockaddr*)server, sizeof(struct sockaddr_in)) < 0)
    {
        printf("Eroare la conectarea la server\n");
        exit(1);
    }
}

void send_message(SOCKET sock, const char* str)
{
    uint32_t length = strlen(str);

    printf("Sending length to server... ");
    if (send(sock, (const char*)&length, sizeof(uint32_t), NO_FLAGS) < 0)
    {
        printf("Couldn't send length to server :(\n");
        exit(1);
    }
    printf("SENT (length: %u)\n", length);
    printf("Sending message to server... ");
    if (send(sock, str, length, NO_FLAGS) < 0)
    {
        printf("Couldn't send message to server :(\n");
        exit(1);
    }
    printf("SENT (message: %s)\n", str);
}

void wait_for_response(SOCKET sock, char* str, uint32_t expected_length)
{
    uint32_t length = recv(sock, str, expected_length, NO_FLAGS);

    if (length != expected_length)
    {
        printf("Received message has a different length - %u vs. %u :(\n", length, expected_length);
        exit(1);
    }
}

void run_client(SOCKET sock)
{
    char message[100], reversed_message[100];

    printf("Message: ");
    scanf("%s", message);
    send_message(sock, message);
    wait_for_response(sock, reversed_message, strlen(message));

    printf("The reversed message is: %s\n", reversed_message);
}

int main()
{
#ifdef _WIN32
    WSADATA wsa;
	
	printf("\nInitialising Winsock...");
	if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
	{
		printf("Error initializing the Windows Sockets Library");
		return -1;
	}
#endif
	
	printf("Initialised.\n");

    SOCKET sock;
    struct sockaddr_in server;

    init_socket(&sock);
    init_server(&server);

    connect_socket_to_server(sock, &server);

    run_client(sock);

    close(sock);
}