/**
 *  Soluzione di game123_123
 */
#include <iostream>
using namespace std;


void play(int n1, int n2, int &togli1, int &togli2) {
  if( (n1%4) == (n2%4) )
      	togli1 = togli2 = 0;
  else {	
    if(n1 > n2)
      togli1 = (n1-n2)%4;
    else
      togli2 = (n2-n1)%4;
  }
}

int main() {
  int n1, n2;
  cin >> n1 >> n2;
  int togli1 = 0, togli2 = 0;
  play(n1, n2, togli1, togli2);
  cout << togli1 << endl << togli2 << endl;
  return 0;
}

