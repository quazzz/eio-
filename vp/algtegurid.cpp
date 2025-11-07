#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;
vector<long long> algegurid(long long n){
    vector<long long> tegurid;
    int aa=1;
    while(++aa < MS){
        if(!soel[aa]) continue;
        if(aa * aa > n) break;
        while(n % aa == 0){
            tegurid.push_back(aa);
            n /= aa;
        }

    }
    if(n!=0) tegurid.push_back(n);
    return tegurid;
}
int main()
{
    fastio;
    // code goes here
    return 0;
}