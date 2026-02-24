#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n; cin >> n;
    vector<int> fraktsioonid;
    int summa = 0;
    int next = 2;
    while(summa + next <= n){
        fraktsioonid.push_back(next);
        summa += next;
        next++;
    }
    int jaanud = n - summa;
    if(jaanud > 0){
        fraktsioonid.back() += jaanud;
    }
    
    cout << fraktsioonid.size() << endl;
    for(int i = 0; i < fraktsioonid.size(); ++i){
        if(i > 0) cout << ' ';
        cout << fraktsioonid[i];
    }
    return 0;
}