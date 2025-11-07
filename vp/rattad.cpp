#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;
int syt(int a, int b){
    while(b > 0){
        int c = b;
        b = a % b;
        a = c;
    }
    return a;
}
int main()
{
    fastio;
    int m,n; cin >> m >> n;
    set<pair<int,int>> s;
    for (size_t a = m; a <= n; a++)
    {
        for(int b = m; b <= n; b++){
            int d = syt(a,b);
            pair<int,int> p = make_pair(a / d, b / d);
            s.insert(p);
        }
    }
    cout << s.size();
    
    return 0;
}