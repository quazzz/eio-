#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

int dsyt(int a, int b, int &x, int &y){
    if(b == 0){
        x = 1;
        y = 0;
        return a;
    }
    int x1,y1,syt = dsyt(b,a%b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return syt;
}
int main()
{
    fastio;
    // code goes here
    return 0;
}