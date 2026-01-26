#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

int main()
{
    fastio;
    int n; cin >> n;
    vector<int> arr(3);
    arr[0] = 0;
    arr[1] = 1;
    for(size_t i = 2; i < n + 1; ++i){
        arr[i % 3] = arr[(i - 1) % 3] + arr[(i - 2) % 3];
    }
    cout << arr[n % 3];
    return 0;
}