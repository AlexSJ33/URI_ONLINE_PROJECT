#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Ler um número inteiro N e calcular todos os seus divisores.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Escreva todos os divisores positivos de N, um valor por linha.

Exemplo de Entrada	Exemplo de Saída
6                   1
                    2
                    3
                    6
"""

print('{:=^45}'.format(' URI Online Judge | 1157 '))
print('{:^45}'.format('Divisores I'))

n = int(input())

def divisores(num):

    for z in range(1, num+1):
        if num % z == 0:
            print(z)

divisores(n)

        