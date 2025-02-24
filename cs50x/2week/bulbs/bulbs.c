#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string input = get_string("Text: ");
    for (int i = 0; i < strlen(input); i++)
    {
        int ascii = input[i];
        int binary[] = {0, 0, 0, 0, 0, 0, 0, 0};

        int j = 0;
        while (ascii > 0)
        {
            binary[j] = ascii % 2;
            ascii /= 2;
            j++;
        }

        for (int k = BITS_IN_BYTE - 1; k >= 0; k--)
        {
            print_bulb(binary[k]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
