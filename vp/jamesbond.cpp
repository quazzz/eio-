#include <iostream>
using namespace std;
string vastus = "abc";
int pikkus = 3;
void leiaVoimalused(int asukoht)
{
    if (asukoht == pikkus)
    {
        for (size_t i = 0; i < pikkus; i++)
        {
            cout << vastus[i];
        }
        cout << endl;
        return;
    }
    vastus[asukoht] -= ('a' - 'A');
    leiaVoimalused(asukoht + 1);
    vastus[asukoht] += ('a' - 'A');
    leiaVoimalused(asukoht + 1);
}
int main() {
    leiaVoimalused(0);
    return 0;
}