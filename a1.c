#include<stdio.h>
#include<string.h>
#include<math.h>
int main()
{
    int t,i=1;
    scanf("%d",&t);
    while(i<=t)
    {
        char str[11] = "", stt[11] = "",result[20] = "";
        scanf("%s%s",str,stt);
        int d1 = (str[0] - '0')*10 + str[1] - '0';
        int d2 = (stt[0] - '0')*10 + stt[1] - '0';
        int m2 = (stt[3] - '0')*10 + stt[4] - '0';
        int m1 = (str[3] - '0')*10 + str[4] - '0';
        int y1 = (str[6] - '0')*1000 + (str[7] - '0')*100 + (str[8] - '0')*10 + str[9] - '0';
        int y2 = (stt[6] - '0')*1000 + (stt[7] - '0')*100 + (stt[8] - '0')*10 + stt[9] - '0';
        int age;
        if(y1 < y2)
        {
            strcpy(result,"Invalid birth date");
        }
        else
        {
            if((y1 - y2)>130)
            {
                strcpy(result,"Check birth date");
            }
            else if(y1 - y2 == 1)
            {
                if(m2 > m1)
                {
                    strcpy(result,"0");
                }
                else
                {
                    if(d2 > d1)
                    {
                        strcpy(result,"0");
                    }
                    else
                    {
                        strcpy(result,"1");
                    }
                }
            }
            else if(y1 == y2)
            {
                if(m2 > m1)
                {
                    strcpy(result,"Invalid birth date");
                }
                else if(m2 == m1 && d2 > d1)
                {
                    strcpy(result,"Invalid birth date");
                }
                else
                {
                    strcpy(result,"0");
                }
            }
            else
            {
                age = y1 - y2;
                if(m1 <= m2 && d1 <= d2)
                {
                    age--;
                }
            }
        }
        if(strlen(result) != 0)
        {
            printf("Case #%d: %s\n",i,result);
        }
        else
        {
            printf("Case #%d: %d\n",i,age);
        }
        i++;
    }
    return 0;
}
