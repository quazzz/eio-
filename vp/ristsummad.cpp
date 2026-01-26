#include <bits/stdc++.h>

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)

#define endl "\n"

using namespace std;

int main()
{
    int tabel[100][100];
    tabel[0][0] = 1;
    for (int i = 0; i < 9; ++i)
    {
        for (int j = 0; j < 90; ++j)
        {
            for (int k = 0; k < 10; k++)
            {
                tabel[i + 1][j + k] += tabel[i][j];
            }
        }
    }
    int n;
    cin >> n;
    int rist;
    cin >> rist;
    int jark;
    cin >> jark;
    int loenda(int n, int ristsumma, int jark)
    {
        if (n == 0)
            return 0;
        int esimene = n / pow(10, jark);
        if (ristsumma < esimene)
            return 0;
        int aste = rint(pow(10, jark));
        int vastus = loenda(n % aste, ristsumma - esimene, jark - 1);
        for (int i = 0; i < esimene; i++)
        {
            vastus += tabel[jark][ristsumma - i];
        }
    }
    fastio;

    return 0;
}