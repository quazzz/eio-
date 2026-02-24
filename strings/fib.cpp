#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

vector<long long> gene(int val){
    vector<long long> fib = {1, 2};
    while(fib.back() < val){
        fib.push_back(fib.back() + fib[fib.size() - 2]);

    }
    return fib;
}

int main() {
    int n; cin >> n;
    vector<long long> input(n);
    long long maxfib = 0;
    for(int i = 0; i < n; ++i){
        cin >> input[i];
        maxfib = max(maxfib, input[i]);
    }
    string line;
    cin.ignore();
    getline(cin, line);
    string letters;
    for(char c: line){
        if(isupper(c)) letters += c;
    }
    vector<long long> fib_seq = gene(maxfib);
    map<long long, int> indeksid;
    for(int i = 0; i < fib_seq.size(); ++i){
        indeksid[fib_seq[i]] = i + 1;
    }
    int max_pos = 0;
    for(long long f: input){
        if(indeksid.count(f))
            max_pos = max(max_pos, indeksid[f]);
    }
    string res(max_pos,' ');
    for(int i = 0; i < n; ++i){
        long long f = input[i];
        if(indeksid.count(f)) {
            int pos = indeksid[f] - 1;
            res[pos] = letters[i];
        }
    }
    cout << res << endl;
    return 0; 
}