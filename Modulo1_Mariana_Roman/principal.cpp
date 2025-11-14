#include <iostream>
#include "lexico.h"

int main() {
    string entrada;

    cout << "Ingresa una cadena: ";
    getline(cin, entrada);

    Lexico lexer(entrada);

    do {
        lexer.sigToken();

        switch (lexer.token) {
        case IDENTIFICADOR:
            cout << "IDENTIFICADOR: " << lexer.lexema << endl;
            break;
        case REAL:
            cout << "REAL: " << lexer.lexema << endl;
            break;
        case ERROR:
            cout << "ERROR: " << lexer.lexema << endl;
            break;
        case FIN:
            cout << "Fin de analisis" << endl;
            break;
        }
    } while (lexer.token != FIN);

    return 0;
}
