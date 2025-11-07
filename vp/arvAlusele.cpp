#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;
string arvAlusele(unsigned int n, unsigned int alus){
    string s = "";
    if(n == 0) return "0";
    while(n){
        int d = n % alus;
        s+= (char) (d < 10) ? '0' + d: 'A' +d -10;
        n /= alus;
    }
    reverse(s.begin(), s.end());
    return s;
}
int main()
{
    fastio;
    // code goes here
    return 0;
}
string arvAlusele2(unsigned int n, unsigned char alus){
    string s = "";
    unsigned int aste = alus;
    while (n > aste){
        aste *= alus;
    }
    aste /= alus;
    while(aste){
        int d = n / aste;
        s+=(char)(d<10) ? '0' + d: 'A' + d - 10;
        n %= aste;
        aste /= alus;
    }
    return s;

}