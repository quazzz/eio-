#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

int main()
{
    fastio;
    // code goes here
    return 0;
}
int kahendotsi(int algus, int lopp){
    
}
long long topeltKahendOtsi(){
    long long algus = 0, lopp = 0;
    int samm = 1;
    char ch;
    while (lopp >= 0)
    {
        cout << lopp << endl;
        cin >> ch;
        if(ch == '=') return lopp;
        else if (ch == '<') break;
        else if (ch == '>') {
            algus = lopp;
            lopp = algus + samm;
            samm *= 2;
        }
        else
            cout << 'sistste > < või =' << endl;
        /* code */
    }
    if(algus <= lopp)
        return 
    
}