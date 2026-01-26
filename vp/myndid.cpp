#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

int leiaKogus(int s, int n, vector<int> v){
    if(s < 0){
        return 1000000;
    }
    if(s == 0){
        return 0;
    }
    else{
        int vastus = 10000000;
        for(int i = 0; i < n; ++i){
            vastus = min(vastus, 1 + leiaKogus(s - v[i], n, v));
        }
        return vastus;
    }
}

int leiakogus2(int s, int n, vector<int> v){
    int kogused[s+1];
    kogused[0] = 0;
    for(int i = 1; i <= s; ++i){
        kogused[i] = 1000000;
    }
    for(int i = 0; i <= s; ++i){
        for(int j = 0; j < n; ++j){
            if(v[j] <= i){
                kogused[i] = min(kogused[i - v[j]] + 1, kogused[i]);
            }
        }
    }
    return kogused[s];
}
int main()
{
    fastio;
    // code goes here
    return 0;
}