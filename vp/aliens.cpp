#include <iostream>
using namespace std;

char* vastus;
int pikkus;

void leia(int asukoht){
    if(asukoht == pikkus) {
        for(int i = 0; i < pikkus; ++i){
            cout << vastus[i];
        }
        cout << endl;
        return;
    }
    if(asukoht == 0){
        vastus[asukoht] = 'A';
        leia(asukoht + 1);
        vastus[asukoht] = 'T';
        leia(asukoht + 1);
        vastus[asukoht] = 'C';
        leia(asukoht + 1);
        vastus[asukoht] = 'G';
        leia(asukoht + 1);
        return;

    }
    char eelmine = vastus[asukoht - 1];
    switch(eelmine){
        case 'A':
        case 'T':
            vastus[asukoht] = 'C';
            leia(asukoht + 1);
            vastus[asukoht] = 'G';
            leia(asukoht + 1);
            break;
    case 'G':
        vastus[asukoht] = 'C';
        leia(asukoht + 1);
    case 'C':
        vastus[asukoht] = 'A';
        leia(asukoht + 1);
        vastus[asukoht] = 'T';
        leia(asukoht + 1);
        break;
    }
}

int main() {
    cin >> pikkus;
    vastus = new char[pikkus];
    leia(0);
}
