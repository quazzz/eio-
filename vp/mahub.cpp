#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;
bool mahub(int suurus, int& m, int& n, vector<int>& asjad){
    int mitmes = 1;
    int praegune = 0;
    int i = 0;
    while(i < m){
        if(mitmes > n){
            return false;
        }
        if(praegune + asjad[i] > suurus){
            mitmes++;
            praegune = 0;
        }
        else {
            praegune += asjad[i];
            ++i;
        }
    }
    return true;
}
int main()
{
    fastio;
    int n; cin >> n;
    int m; cin >> m;
    vector<int> asjad(m);
    for (size_t i = 0; i < m; i++) cin >> asjad[i];

    int vahim = 0;
    int suurim = m;
    w
    
        return 0;
}
