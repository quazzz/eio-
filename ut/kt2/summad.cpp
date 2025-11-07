#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;
void backtrack(int idx, int cursum, vector<int>& curComb, int s, const vector<int>& arr){
    if(cursum == s){
        for(int x: curComb) cout << x << " ";
        cout << endl;
        return;
    }
    if(cursum > s || idx == arr.size()) return;
    curComb.push_back(arr[idx]);
    backtrack(idx + 1, cursum + arr[idx], curComb, s, arr);
    curComb.pop_back();
    backtrack(idx + 1, cursum, curComb, s, arr);
}
int main()
{
    fastio;
    int s,n; cin >> s >> n;
    vector<int> liidetavad(n);
    for (size_t i = 0; i < n; i++)
    {
        cin >> liidetavad[i];
    }
    for(int x: liidetavad){
        cout << x << endl;
    }
    
    backtrack(0,0,vector<int>(n), s, liidetavad);
    // code goes here
    return 0;
}
