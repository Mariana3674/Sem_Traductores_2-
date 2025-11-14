#include "lexico.h"
#include <cctype>

Lexico::Lexico(string fuente) {
    this->fuente = fuente;
    ind = 0;
    c = fuente[ind];
}

char Lexico::sigCaracter() {
    if (ind < fuente.length())
        return fuente[ind++];
    return '\0';
}

bool Lexico::esLetra(char c) {
    return isalpha(c);
}

bool Lexico::esDigito(char c) {
    return isdigit(c);
}

void Lexico::sigToken() {
    lexema = "";

    while (isspace(c)) {
        c = sigCaracter();
    }

    if (c == '\0') {
        token = FIN;
        return;
    }

    if (esLetra(c)) {
        lexema += c;
        c = sigCaracter();
        while (esLetra(c) || esDigito(c)) {
            lexema += c;
            c = sigCaracter();
        }
        token = IDENTIFICADOR;
        return;
    }

    if (esDigito(c)) {
        string parteEntera = "";
        string parteDecimal = "";

        while (esDigito(c)) {
            parteEntera += c;
            c = sigCaracter();
        }

        if (c == '.') {
            c = sigCaracter();

            if (!esDigito(c)) {
                token = ERROR;
                lexema = parteEntera + ".";
                return;
            }

            while (esDigito(c)) {
                parteDecimal += c;
                c = sigCaracter();
            }

            lexema = parteEntera + "." + parteDecimal;
            token = REAL;
            return;
        }
    }

    lexema = c;
    token = ERROR;
    c = sigCaracter();
}
