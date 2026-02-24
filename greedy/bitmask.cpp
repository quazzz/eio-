#include <iostream>
using namespace std;
int main() {
    unsigned int n,l,u; cin >> n >> l >> u;
    unsigned int m = 0;
    for(int i = 31; i >= 0; --i){
        unsigned int bit = 1U << i;
        if(!(n & bit) && (m | bit) <= u){
            m |= bit;
        }
    }
    if( m < l) {
        m = l;
    }
    cout << m << endl;
    return 0;
}