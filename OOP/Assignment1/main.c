#include <stdio.h>
#include <string.h>

int main() {
    char* message = (char*) malloc (100);

    scanf("%s", message);
    printf("%s", message);

    return 0;
}
