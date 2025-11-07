#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;
int* vastus;
int pikkus = 3;
int main()
{
    fastio;
    sort(vastus, vastus + pikkus);
    bool veel = 1;
    while(veel){
        for (int i = 0; i < pikkus; i++)
        {
            cout << vastus[i];
        }
        cout << endl;
        veel = next_permutation(vastus, vastus + pikkus)
        
    }
    return 0;
}