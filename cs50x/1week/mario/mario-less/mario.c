#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size;
    do
    {
        size = get_int("Height: ");
    }
    while(size < 1 || size > 8);

    for(int height = 0; height < size; height++){
        for(int space = size; space > height+1; space--){
            printf(" ");
        }
        for(int tile = 0; tile <= height; tile++){
            printf("#");
        }
        printf("\n");
    }
}
