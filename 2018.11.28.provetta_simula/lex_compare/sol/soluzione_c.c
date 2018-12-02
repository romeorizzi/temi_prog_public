/**
 *  Soluzione di perm_recognition, scritta da Romeo Rizzi 2018.11.28, ultima modifica 2018.11.30
 */
#include <stdio.h>

const int MINORE = -1;
const int UGUALE = 0;
const int MAGGIORE = 1;

const int MAXL = 100;

int lex_compare(char *s, char *t) {
  //printf("B%sE\n", s);
  //printf("B%sE\n", t);
  if(*s == '\0' && *t == '\0')
    return UGUALE;
  if(*s == '\0')
    return MINORE;
  if(*t == '\0')
    return MAGGIORE;
  if (*s<*t)
    return MINORE;
  if(*s>*t)
    return MAGGIORE;
  return lex_compare(s+1,t+1);
}

int main() {
  char s[MAXL], t[MAXL];
  scanf("%s", s);
  scanf("%s", t);
  printf("%d\n", lex_compare(s, t) );
  return 0;
}

