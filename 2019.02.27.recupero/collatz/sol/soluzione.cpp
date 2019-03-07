/**
 *  Soluzione di collatz
 */
#include <iostream>
using namespace std;


void simula(int n) {
  while(n > 1) {
    cout << n << endl;
    if(n % 2 == 0)
      n /= 2;
    else
      n = 3*n +1;
  }
  cout << 1 << endl;
}


int main() {
  int n;
  cin >> n;
  simula(n);
  return 0;
}

