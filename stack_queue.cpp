#include<bits/stdc++.h>
using namespace std;

int stk[10], sp = 0, que[10], qp1 = 0, qp2 = 0;

int isFull(int n);
int isEmpty(int n);
void push(int n);
void pop();
void enqueue(int n);
void dequeue();


int main()
{
    int n;
    cout << "Size of array: ";
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    sort(arr,arr+n);

    for(int i = 0; i < n; i++){
        if(i%2 == 0){
            if(!isFull(sp)){
                push(arr[i]);
            }
        }
        else{
            if(!isFull(qp2)){
                enqueue(arr[i]);
            }
        }
    }

    while(1){
        if(!isEmpty(qp2)){
            dequeue();
        }
        else{
            break;
        }
    }
    while(1){
        if(!isEmpty(sp)){
            pop();
        }
        else{
            break;
        }
    }
    cout << endl;
}

int isFull(int n){
    if(n > 9) return 1;
    else return 0;
}
int isEmpty(int n){
    if (n == 0) return 1;
    else return 0;
}

void push(int n){
    stk[sp] = n;
    sp++;
}

void pop(){
    cout << stk[sp-1] << " ";
    sp--;
}

void enqueue(int n){
    que[qp2] = n;
    qp2++;
}

void dequeue(){
    cout << que[qp1] << " ";
    for(int i = 0; i < qp2-1; i++){
        que[i] = que[i+1];
    }
    qp2--;
}

