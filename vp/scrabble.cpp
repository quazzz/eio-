#include <bits/stdc++.h>
#define SP 9000000
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"
map<int,int> suurarvud;
char soel[SP];

int onAlgarv(int p) {
    int i;
    if(p < SP){
        return soel[p];
    }
    if(suurarvud.find(p) == suurarvud.end()){
        for(i = 2; i <= sqrt(p); i++){
            if((i < SP) && (soel[i] == 0)) continue;
            if(p % i == 0){
                suurarvud[p] = 0;
                return 0;
            }
        }
        suurarvud[p] = 1;
    }
    return suurarvud[p];
}
using namespace std;

int main()
{
    fastio;
    // code goes here
    return 0;
}