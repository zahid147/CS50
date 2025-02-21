#include<stdio.h>
#include<math.h>

void max(int arr[], int n){
    int max = arr[0];
    for(int i = 1; i < n; i++){
        if (arr[i] > max) max = arr[i];
    }
    printf("The maximum number : %d\n",max);
}
void min(int arr[], int n){
    int min = arr[0];
    for(int i = 1; i < n; i++){
        if (arr[i] < min) min =arr[i];
    }
    printf("The minimum number : %d\n",min);
}

int isPrime(int n){
    if(n < 2) return 0;
    else if(n == 2) return 1;
    else{
        for(int i = 2; i < sqrt(n)+1; i++){
            if(n%i == 0) return 0;
        }
        return 1;
    }
}
void countPrime(int arr[], int n){
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(isPrime(arr[i])) cnt++;
    }
    printf("The number of prime numbers : %d\n", cnt);
}

int isPalindrome(int n){
    int tmp = 0;
    for(int i = n; i > 0; i /= 10){
        tmp = tmp*10 + i%10;
    }
    if(n == tmp) return 1;
    else return 0;
}
void countPalindrome(int arr[], int n){
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(isPalindrome(arr[i])) cnt++;
    }
    printf("The number of palindrome numbers : %d\n", cnt);
}

int countDivisor(int n){
    int sum = 0;
    for(int i = 1; i <= n; i++){
        if(n%i == 0) sum++;
    }
    return sum;
}
void maxDivisor(int arr[], int n){
    int tmp1 = 0,tmp2 = 0,ans = 0;
    for(int i = 1; i < n; i++){
        tmp2 = countDivisor(arr[i]);
        if(tmp2 > tmp1){
            tmp1 = tmp2;
            if(arr[i] > ans) ans = arr[i];
        }
    }
    printf("The number that has the maximum number of divisors : %d\n",ans);
}

int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    max(arr,n);
    min(arr,n);
    countPrime(arr,n);
    countPalindrome(arr,n);
    maxDivisor(arr,n);
}
