#include <stdio.h>
#include <string.h>
#include <time.h>

typedef struct tm tm;

int checkCondition(char* dateString, time_t currentTime)
{
    printf("Unaltered line: %s\n", dateString);
    tm date;
    strptime(dateString, "%d-%m-%Y", &date);
    time_t time = mktime(&date);
    int difference = (int)difftime(currentTime, time);
    printf("Diff: %d\n", difference);

    return 1;
}

int main() {
    char line[50];
    time_t t = time(NULL);
//    tm currentTime = *localtime(&t);

    scanf("%s", line);

    while (strcmp(line, "exit") != 0)
    {
        if (checkCondition(line, t))
            printf("Time: %s\n", line);
        scanf("%s", line);
    }
        return 0;
}
