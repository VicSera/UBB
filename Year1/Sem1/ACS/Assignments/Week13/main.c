//
// Created by victor on 08.01.2020.
//
#include <stdio.h>

extern int match_words(char template[], char word[]);

int main()
{
    char word[20] = {0};
    char template[20] = {0};

    scanf("%s", template);

    while (1)
    {
        scanf("%s", word);
        if (word[0] == '$')
            break;
        if (match_words(template, word))
            printf("Match!\n");
        else
            printf("No match!\n");
    }

    return 0;
}

