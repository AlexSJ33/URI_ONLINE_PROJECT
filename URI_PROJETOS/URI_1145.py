#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um programa que leia dois valores X e Y. 
A seguir, mostre uma sequência de 1 até Y, passando 
para a próxima linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas, com 1 espaço 
em branco entre cada número, conforme exemplo abaixo. Não deve haver
espaço em branco após o último valor da linha.


Exemplo de Entrada	Exemplo de Saída
3 99                1 2 3
                    4 5 6
                    7 8 9
                    2 5 9
                    10 11 12
                    ...
                    97 98 99
"""

print('{:=^45}'.format(' URI Online Judge | 1145 '))
print('{:^45}'.format('Sequência Lógica 2'))

n1,n2 = list(map(int,input().split()))
c = 1
for x in range(1,(int((n2/n1))+1)):
    limit = ""
    for y in range(n1):
        limit += str(c) + " "
        c += 1
    print(limit[:-1])