#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

int main()
{
    fastio;
    int pikkus; cin >> pikkus;
    vector<char> vastus(pikkus);
    for (size_t i = 0; i < pikkus; i++) cin >> vastus[i];
    int suurarv = 1 << pikkus;
    for (size_t i = 0; i < suurarv; i++)
    {
        for (size_t j = 0; j < pikkus; j++)
        {
            char taht = vastus[j];
            if((1 << j) & i){
                taht -= ('a' - 'A');
            }
            cout << taht;
        }
        cout << endl;
        
    }
    
    
    
    return 0;
}