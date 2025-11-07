#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

const int SP = 1000;
char soel[SP];
void alg() {
    int i,j;
    for(i = 0; i < SP; ++i){
        soel[i] = 1;
    }
    soel[0] = 0;
    soel[1] = 0;
    for(i = 2; i <= SP; ++i){
        if(soel[i] == 1)
            for(j = i * i; j < SP; j+=i)
                soel[j] = 0;
    }
}