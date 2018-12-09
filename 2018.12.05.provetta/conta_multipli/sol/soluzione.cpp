/**
 *  Soluzione di conta_multipli, scritta da Alessandro Righi 2018.12.05
 */

#include <iostream>

using namespace std;

typedef unsigned long long ull;

int main() {
	ull a, b, c;

	cin >> a >> b >> c;

	ull count = 0;
	for (ull n = 0; n <= c; n++)
		if (n % a == 0 && n % b != 0)
			count++;

	cout << count;
	return 0;
}

