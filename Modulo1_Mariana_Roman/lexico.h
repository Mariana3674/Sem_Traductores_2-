#ifndef LEXICO_H
#define LEXICO_H

#include <string>
using namespace std;

enum TipoToken {
    IDENTIFICADOR,
    REAL,
    ERROR,
    FIN
};

class Lexico {
public:
    string fuente;
    int ind;
    char c;
    string lexema;
    TipoToken token;

    Lexico(string fuente);
    char sigCaracter();
    void sigToken();
    bool esLetra(char c);
    bool esDigito(char c);
};

#endif
