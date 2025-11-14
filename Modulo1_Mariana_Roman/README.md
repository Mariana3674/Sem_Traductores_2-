# Módulo 1 – Analizador Léxico

Este programa implementa un analizador léxico en C++, de acuerdo con las especificaciones del profesor.

## Tokens reconocidos

### Identificadores
Regla:
    identificador = letra (letra | digito)*

### Números reales
Regla:
    real = entero . entero+

## Archivos incluidos
- lexico.h
- lexico.cpp
- principal.cpp

## Compilar en Mac (VS Code o terminal)
    g++ principal.cpp lexico.cpp -o analizador
    ./analizador
