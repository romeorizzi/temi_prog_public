/**
 *  Soluzione di perm_recognition, scritta da Romeo Rizzi 2018.11.28
 */
#include <iostream>
using namespace std;

const int MAXN = 1000000;
int n, f[MAXN], seen[MAXN];

int is_perm(int n, int f[MAXN]) {
  for(int i = 0; i<n; i++) {
    if(f[i] < 0) return 0;
    if(f[i] >= n) return 0;
    if(seen[f[i]]) return 0;
    seen[f[i]] = 1;
  }
  return 1;
}

int main() {
  int n;
  cin >> n;
  for(int i = 0; i<n; i++)
     cin >> f[i];
  if(is_perm(n,f))
     cout << "True" << endl;
  else
     cout << "False" << endl;    
  return 0;
}

