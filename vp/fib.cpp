#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

int fib1(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fib1(n-1) + fib1(n - 2);
}

const int Max = 1000;
long A[Max];
long fib2(int n){
    if(n == 0) return 0;
    if(n==1) return 1;
    if (A[n] == 0) A[n] = fib2(n - 1) + fib2(n - 2);
    return A[n];
}
long fib3(int n){
    const int Max = 100000;
    long A[Max];
    A[0] = 0;
    A[1] = 1;
    for(int i = 2; i <= n; ++i){
        A[i] = A[i - 1] + A[i - 2];
    }
    return A[n];
}
long fib4(int n) {
    long a[3];
    a[0] = 0;
    a[1] = 1;
    for(int i = 2; i <= n; ++i){
        a[i % 3] = a[(i-1) % 3] + a[(i - 2) % 3];
    }
    return a[n % 3];
}