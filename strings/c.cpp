#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

string solve(const string &s, int k) {
    if (k <= 0 || k > (int)s.size()) return "";
    unordered_map<string, int> freq;
    int n = s.size();
    
    for (int i = 0; i <= n - k; ++i) {
        freq[s.substr(i, k)]++;
    }
    string res;
    int count = 0;
    for (auto &p : freq) {
        if (p.second > count || (p.second == count && p.first < res)) {
            count = p.second;
            res = p.first;
        }
    }
    return res;
}
int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    cout << solve(s, n) << endl;
    return 0;
}