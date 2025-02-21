// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool l = false, u = false, n = false, s = false;

    for (int i = 0, len = strlen(password); i < len; i++)
    {
        int ll = islower(password[i]), uu = isupper(password[i]), nn = isdigit(password[i]), ss = ispunct(password[i]);

        if (ll != 0)
        {
            l = true;
        }
        else if (uu != 0)
        {
            u = true;
        }
        else if (nn != 0)
        {
            n = true;
        }
        else if (ss != 0)
        {
            s = true;
        }
    }
    if (l == true && u == true && n == true && s == true)
    {
        return true;
    }
    return false;
}
