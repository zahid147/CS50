#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i = get_int("First number: ");
    int j = get_int("Second number: ");

    int i_a[i], j_a[j], c[i+j];

    for (int k = 0; k < i; k++)
    {
        i_a[k] = 0;
    }

    for (int k = 0; k < j; k++)
    {
        j_a[k] = 0;
    }

    for (int k = 0; k < i+j; k++)
    {
        c[k] = 0;
    }

    int l = 0;
    for (int k = 1; k <= i; k ++)
    {
        if (i % k == 0)
        {
            while (l < i)
            {
                i_a[l] = k;
                l++;
                break;
            }
        }
    }

    l = 0;
    for (int k = 1; k <= j; k ++)
    {
        if (j % k == 0)
        {
            while(l < j)
            {
                j_a[l] = k;
                l++;
                break;
            }
        }
    }

    l = 0;
    for (int m = 0; m < i; m++)
    {
        for (int n = 0; n < j; n++)
        {
            if (i_a[m] == j_a[n])
            {
                while (l < i+j)
                {
                    c[l] = j_a[n];
                    l++;
                    break;
                }
            }
        }
    }

    int max = 0;
    for (int k = 0; k < i+j; k++)
    {
        if (c[k] > max)
        {
            max = c[k];
        }
    }

    printf("GCD is: %i\n", max);
}