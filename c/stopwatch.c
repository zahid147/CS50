#include<stdio.h>
#include<unistd.h>

void clr();

int main(void)
{
    int h, m, s, hour, minute, second;

    clr();
    printf("Input duration:(hh mm ss) ");
    scanf("%i %i %i",&hour, &minute, &second);

    h = m = s =0;
    while(1){
        clr();

        printf("#### STOP WATCH ####\n\n");
        printf("      %.2i:%.2i:%.2i\n\n", h,m,s);
        printf("####################\n");
        s++;
        sleep(1);

        if (h == hour && m == minute && s == second)
        {
            return 0;
        }

        if(s == 60){
            m++;
            s=0;
        }
        if(m == 60){
            h++;
            m=0;
        }
    }
}




void clr()
{
    printf("\e[1;1H\e[2J");
}