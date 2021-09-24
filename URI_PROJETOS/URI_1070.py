#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia um valor inteiro X. Em seguida apresente os 6 valores
ímpares consecutivos a partir de X, um valor por linha,
inclusive o X ser for o caso.
Entrada
A entrada será um valor inteiro positivo.
Saída
A saída será uma sequência de seis números ímpares.

Exemplo de Entrada	Exemplo de Saída
8                   9
                    11
                    13
                    15
                    17
                    19
"""
print('{:=^45}'.format(' URI Online Judge | 1070 '))
print('{:^45}'.format('Seis Números Ímpares'))

contador = 0
num = int(input())
while contador < 12:
    if num % 2 != 0:
        print(num)
    contador += 1
    num += 1