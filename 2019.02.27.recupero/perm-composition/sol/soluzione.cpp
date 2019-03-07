/**
 *  Soluzione di perm_composition, scritta da Alessandro Righi 2018.11.29
 */
#include <iostream>

using namespace std;

static const int MAXN = 1000000;

void perm_composition(int N, int p1[], int p2[], int ris[]) {
	for (int i = 0; i < N; i++) {
		ris[i] = p2[p1[i]];
	}
}

int main() {
	static int N, p1[MAXN], p2[MAXN], ris[MAXN];
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> p1[i];
	for (int i = 0; i < N; i++)
		cin >> p2[i];

	perm_composition(N, p1, p2, ris);

	for (int i = 0; i < N; i++)
		cout << ris[i] << ' ';	
	return 0;
}

