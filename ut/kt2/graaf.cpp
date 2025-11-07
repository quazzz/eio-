#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

void backtrack(int i, unordered_set<int>& blackset, unordered_set<int> mustadTippud, int& maxblack, vector<int>& best, int n, int m, vector<vector<int>>& edges){
    if(i > n){
        vector<int> current(blackset.begin(), blackset.end());
        if(blackset.size() > maxblack){
            maxblack = blackset.size();
            best = current;
        }
        else if(blackset.size() == maxblack) {
            if(current < best){
                best = current;
            }
        }
        return;
    }
    if(mustadTippud.find(i) == mustadTippud.end()) {
        blackset.insert(i);
        set<int> uued = mustadTippud;
        uued.insert(edges[i].begin(), edges[i].end());
        backtrack(i + 1, blackset, uued, maxblack, best, n, m, edges);
        blackset.erase(i);

    }
    backtrack(i + 1, blackset, mustadTippud, maxblack, best, n, m, edges);
}

int main()
{
    fastio;
    int n,m; cin >> n >> m;
    vector<vector<int>> edges(n + 1);
    for (size_t i = 0; i < m; i++)
    {
        int yks, kaks; cin >> yks >> kaks;
        edges[yks].push_back(kaks);
        edges[kaks].push_back(yks);
    }
    int maxblack = 0;
    vector<int> best;
    unordered_set<int> blackset, mustadTippud;
    backtrack(1, blackset, mustadTippud, maxblack, best, n,m, edges);
    cout << maxblack << endl;
    for (size_t i = 0; i < maxblack; i++)
    {
        if(i == maxblack - 1){
            cout << best[i];
            break;
        }
        cout << best[i] << ' ';
    }
    

    
    return 0;
}