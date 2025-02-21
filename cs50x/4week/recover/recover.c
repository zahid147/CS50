#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Could not open.\n");
        return 1;
    }

    bool found = false;
    unsigned char buffer[512];
    int c = 0;

    FILE *outfile = NULL;

    char *filename = malloc(8 * sizeof(char));

    while (fread(buffer, sizeof(char), 512, infile))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (found)
            {
                fclose(outfile);
            }
            else
            {
                found = true;
            }

            sprintf(filename, "%03i.jpg", c);
            outfile = fopen(filename, "w");
            if (outfile == NULL)
            {
                fclose(infile);
                return 1;
            }
            c++;
        }

        if (found)
        {
            fwrite(buffer, sizeof(char), 512, outfile);
        }
    }
    free(filename);
    fclose(infile);
    if (found)
    {
        fclose(outfile);
    }
    return 0;
}