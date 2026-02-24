#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
    int n; cin >> n;
    vector<long long> a(n);
    vector<int> r(n);
    for(int i = 0; i < n; ++i) cin >> a[i] >> r[i];
    vector<pair<int, int>> left(n), right(n);
    for(int i = 0; i < n; ++i){
        left[i] = {i - r[i], i };
        right[i] = {i + r[i], i};
    }
    sort(begin(left), end(left));
    sort(begin(right), end(right));
    vector<long long> power(n);
    int lefti, righti = 0;
    int besti = 0;
    long long intensity = 0;
    for(int i = 0; i < n; ++i){
        while(lefti < n and left[lefti].first <= i){
            int lampi = left[lefti].second;
            if(besti == -1 or besti + r[besti] < lampi + r[lampi]){
                besti = lampi;
            }
            ++lefti;
        }
        a[i] -= intensity;
        if(a[i] > 0){
            power[besti] += a[i];
            intensity += a[i];
        }
        while(righti < n and right[righti].first <= i){
            int lampi = right[righti].second;
            intensity -= power[lampi];
            righti++;
        }
    }
    long long sum = 0;
    for(int i = 0; i < n; ++i){
        sum += power[i];
    }
    cout << sum << endl;
}