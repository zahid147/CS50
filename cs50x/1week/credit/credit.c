#include <cs50.h>
#include <stdio.h>

int count(long num);

int main(void)
{
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while(number < 0);
    int length = count(number);

    if(length == 0){
        printf("INVALID\n");
        return 0;
    }

    int temp1 = 0, temp2 = 0, temp, temp3 = 0, temp4;
    for(long i = number; i > 0; i /= 10){
        temp3++;
        temp = i%10;
        if(temp3%2 == 0){
            temp4 = 2*temp;
            if(temp4 <= 9){
                temp1 += temp4;
            }
            else{
                for(int j = temp4; j > 0; j /= 10){
                    temp1 += j%10;
                }
            }
        }
        else{
            temp2 += temp;
        }
    }
    temp = temp1 + temp2;
    if(!(temp % 10 == 0)){
        printf("INVALID\n");
        return 0;
    }

    if(length == 15){
        for(long i = number; i > 99; i /= 10){
            number /= 10;
        }
        if(number == 34 || number == 37){
            printf("AMEX\n");
        }
        else{
            printf("INVALID\n");
        }
    }
    if(length == 13){
        for(long i = number; i > 9; i /= 10){
            number /= 10;
        }
        if(number == 4){
            printf("VISA\n");
        }
        else{
            printf("INVALID\n");
        }
    }
    if(length == 16){
        for(long i = number; i > 99; i /= 10){
            number /= 10;
        }
        if(number >= 51 && number <= 55){
            printf("MASTERCARD\n");
        }
        else{
            number /= 10;
            if(number == 4){
            printf("VISA\n");
            }
            else{
                printf("INVALID\n");
            }
        }
    }
}

int count(long num)
{
    int count = 0;
    for(long i = num; i > 0; i /= 10){
        count++;
    }
    if(!(count == 13 || count == 15 || count == 16)){
        return 0;
    }
    return count;
}
