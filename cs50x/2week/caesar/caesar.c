#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{        score += status[i];

//command-line-verify

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    for (int i = 0, j = strlen(argv[1]); i < j; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }


//transforming key

    int key = atoi(argv[1]);


//getting input and printing

    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    for (int i = 0, j = strlen(plaintext); i < j; i++)
    {
        if (isupper(plaintext[i]))
        {
            plaintext[i] = (plaintext[i] - 65 + key) % 26;
            printf("%c", plaintext[i] + 65);
        }

        else if (islower(plaintext[i]))
        {
            plaintext[i] = (plaintext[i] - 97 + key) % 26;
            printf("%c", plaintext[i] + 97);
        }

        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}