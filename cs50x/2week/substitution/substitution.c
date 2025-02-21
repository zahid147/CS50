#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    for (int i = 0, k = strlen(argv[1]); i < k; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }

        for (int j = i + 1; j < k; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                printf("Every charecter must be unique!\n");
                return 1;
            }
        }
    }

    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    for (int i = 0, j = strlen(plaintext); i < j; i++)
    {
        if (isupper(plaintext[i]))
        {
            int uposition = plaintext[i] - 65;
            printf("%c", toupper(argv[1][uposition]));
        }

        else if (islower(plaintext[i]))
        {
            int lposition = plaintext[i] - 97;
            printf("%c", toupper(argv[1][lposition]) + 32);
        }

        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}