// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string argv);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowel word\n");
        return 1;
    }

    string change = replace(argv[1]);
    printf("%s\n", change);
}


string replace(string argv)
{
    for (int i = 0, l = strlen(argv); i < l; i++)
    {
        switch (argv[i])
        {
            case 'a':
                argv[i] = '6';
                break;
            case 'e':
                argv[i] = '3';
                break;
            case 'i':
                argv[i] = '1';
                break;
            case 'o':
                argv[i] = '0';
                break;
        }
    }
    return argv;
}