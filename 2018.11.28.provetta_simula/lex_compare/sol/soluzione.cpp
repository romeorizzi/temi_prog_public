/**
 *  Soluzione di perm_recognition, scritta da Romeo Rizzi 2018.11.28
 */
#include <iostream>
#include <string>
using namespace std;

const int MINORE = -1;
const int UGUALE = 0;
const int MAGGIORE = 1;

const int MAXL = 60;

char s[MAXL+2], t[MAXL+2]; 

int lex_compare(string s, string t) {
  if(s.empty() && t.empty())
    return UGUALE;
  if(s.empty())
    return MINORE;
  if(t.empty())
    return MAGGIORE;
  if (s[0]<t[0])
    return MINORE;
  if(s[0]>t[0])
    return MAGGIORE;
  s.erase(0,1);
  t.erase(0,1);
  return lex_compare(s,t);
}

int main() {
  string s, t;
  getline (cin,s);
  getline (cin,t);
  cout << lex_compare(s, t) << endl;
  return 0;
}

