#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

char* vastus;
char* esialgne;
bool* kasVoetud;
int pikkus;

void LeiaKoikVoimalused(int asukoht)
{
	if (asukoht == pikkus) {
		for (int i = 0; i < pikkus; i++) {
			cout << vastus[i];
		}
		cout << endl;
		return;
	}
	for (int i = 0; i < pikkus; i++) {
		if (kasVoetud[i] ||
			(i > 0 && !kasVoetud[i - 1] && esialgne[i - 1] == esialgne[i])) {
			continue;
		}
		kasVoetud[i] = 1;
		vastus[asukoht] = esialgne[i];
		LeiaKoikVoimalused(asukoht + 1);
		kasVoetud[i] = 0;
	}
}

int main()
{
	string s;
	cin >> s;
	pikkus = s.size();
	esialgne = new char[pikkus];
	vastus = new char[pikkus];
	kasVoetud = new bool[pikkus];
	for (int i = 0; i < pikkus; i++)
	{
		esialgne[i] = s[i];
		kasVoetud[i] = 0;
	}
	sort(esialgne, esialgne + pikkus);
	LeiaKoikVoimalused(0);
	cin >> s;
}