// problem: game123_123, Romeo Rizzi 2019

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;

ifstream *fin;
ifstream *fcor;
ifstream *fout;

void ex(const char *msg, float res) {
  if(msg) {
    fprintf(stderr, "%s ", msg);
  }
  printf("%f\n", res);
  exit(0);
}

template <class T>
T safe_read(const T &lowerBound, const T &upperBound) {
  // Legge in maniera sicura un tipo ordinato e controlla che stia in
  // [lowerBound, upperBound]
  T x;
  if (lowerBound > upperBound) {
      cerr << "safe_read chiamato con parametri errati: " << lowerBound << " " << upperBound << "\n";
      return 1;
  }
  *fout >> x;
  if (fout->fail() || fout->eof())
    ex("Output malformato", 0.0f);
  if (x < lowerBound)
    ex("Output invalido: in una mossa non puoi togliere un numero negativo di gettoni.", 0.0f);
  if (x > upperBound)
    ex("Output invalido: in una mossa non puoi togliere massimo 3 gettoni.", 0.0f);
  return x;
}


int main(int argc, char *argv[]) {
  if(argc < 4) {
      cerr << "Usage: " << argv[0] << " <input> <correct output> <test output>" << endl;
      return 1;
  }

  fin = new ifstream(argv[1]);
  fcor = new ifstream(argv[2]);
  fout = new ifstream(argv[3]);

  if(fin->fail()) {
      cerr << "Impossibile aprire il file di input " << argv[1] << "." << endl;
      return 1;
  }
  if(fcor->fail()) {
      cerr << "Impossibile aprire il file di output corretto " << argv[2] << "." << endl;
      return 1;
  }
  if(fout->fail())
    ex("Impossibile aprire il file di output generato dal codice sottoposto al problema.", 0.0);

  int n1, n2, c_m1, c_m2, m1, m2; // c_m1 e c_m2 nemmeno servono, solo per mantenere approccio generale standard dove può aiutare poter sbirciare ad una soluzione di riferimento piuttosto che impiegare e spoilerare nel correttore una soluzione piena. 
  *fin >> n1 >> n2;
  *fcor >> c_m1 >> c_m2;
  m1 = safe_read(0, 3);
  m2 = safe_read(0, 3);
  if(m1 * m2 > 0)
    ex("Non puoi togliere gettoni da entrambi gli stack in una singola mossa.", 0.0);
  if( (m1 + m2 == 0) && (c_m1 + c_m2 > 0) )
    ex("Ti sei arreso in una situazione dove invece potevi vincere.", 0.0);
  
  if( (m1 + m2 > 0) && (c_m1 + c_m2 == 0) )
    ex("Inutile giocare in una situazione persa. Dovresti arrenderti come spiegato nel testo dell'esercizio.", 0.0);

  int new1 = n1-m1, new2 = n2-m2;
  int diff = new1 - new2;
  if(diff < 0)  diff = -diff;
  
  if (diff % 4 == 0)
      ex("Output corretto.", 1.0);
    else
      ex("In una situazione di vittoria hai effettuato una mossa non vincente.", 0.0);

  ex("Panic.", 0.0);
  return 0;
}
