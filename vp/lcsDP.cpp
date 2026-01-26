#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

int leiaYhised(int* jada1, int* jada2, int p1, int p2){
    int** yhised = new int*[p1 + 1];
    for(int i =0; i <= p1; ++i){
        yhised[i] = new int(p2 + 1);
    }
    for(int i = 0; i <= p1; ++i){
        yhised[i][0] = 0;
    }
    for (size_t i = 0; i <= p2; i++)
    {
        yhised[0][i] = 0;
    }
    for(int i = 1; i<= p1; ++i){
        for(int j = 1; j <= p2; ++j){
            if(jada1[i - 1] == jada2[i-1]){
                yhised[i][j] = yhised[i-1][j-1] + 1;

            }
            else {
                yhised[i][j] = max((yhised[i-1][j]), (yhised[i][j-1]));
            }
        }
    }
    return yhised[p1][p2];
    
}

int main()
{
    fastio;
    // code goes here
    return 0;
}