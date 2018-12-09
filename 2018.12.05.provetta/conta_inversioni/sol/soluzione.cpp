/**
 *  Soluzione di numero_di_inversioni, scritta da Andrea Cracco 2018.12.04
 */
#include <iostream>

using namespace std;

static const int MAXN = 1000000;

int N = 0;
int P[MAXN];
int T[2][MAXN];

int merge(int *p, int s, int e, int l) {
	if (e - s <= 1) {
		if (e - s == 1) T[l][s] = p[s];
		return 0;
	}
	int m = (s+e)/2;

	int f1 = merge(p, s, m, !l);
	int s1 = merge(p, m, e, !l);

	int sol = s1 + f1;
	int p1 = m-s;
	int p2 = e-m;

	int oth = !l;
	for (int i = e-1; p2 || p1; i--) {
		if (p1 && (!p2 || (T[oth][s + p1-1] > T[oth][m + p2-1]))) {
			T[l][i] = T[oth][s + --p1];
			sol += p2;
		}
		else {
			T[l][i] = T[oth][m + --p2];
		}
	}

	return sol;
}


int numero_di_inversioni(int N, int p[]) {
	return merge(p, 0, N, 0);
}

int main() {
	while (cin >> P[N++]);
	N--;

	cout << numero_di_inversioni(N, P) << endl;

	return 0;
}
