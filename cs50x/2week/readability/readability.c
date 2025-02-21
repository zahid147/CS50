#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

float letter, word, sentence;

int readability(string text);

int main(void)
{
    //taking input
    string text = get_string("Text: ");

    //using function
    int grade = readability(text);

    //print result
    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }

    //tests
    //printf("%0.0f--%0.0f--%0.0f\n", letter, word, sentence);
    //printf("%f--%f\n", L, S);
}


int readability(string text)
{
    letter = 0.0, word = 1.0, sentence = 0.0;
    int len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        if (isalpha(text[i]))
        {
            letter++;
        }
        else if (isspace(text[i]))
        {
            word++;
        }
        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentence++;
        }
    }
    float L = letter / word * 100, S = sentence / word * 100, index = 0.0588 * L - 0.296 * S - 15.8;

    return round(index);
}