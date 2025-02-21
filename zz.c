#include<stdio.h>
#include<math.h>
int prime(int n){
    if (n < 2) return 0;
    else if (n == 2) return 1;
    else{
        if(n%2 == 0) return 0;
        for(int i = 3; i < sqrt(n)+1; i += 2){
            if(n%i == 0) return 0;
        }
        return 1;
    }
}

int main(){
    int num = 2,cnt = 0;
    while (1){
        if(prime(num)){
            printf("%d,",num);
            cnt++;
            num++;
        }
        else{
            num++;
        }
        if(num > 100) break;
    }
    return 0;
}
