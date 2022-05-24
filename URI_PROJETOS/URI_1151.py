#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci.
Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores.
Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

Exemplo de Entrada	Exemplo de Saída
5                   0 1 1 2 3
"""

print('{:=^45}'.format(' URI Online Judge | 1151 '))
print('{:^45}'.format('Fibonacci Fácil'))

n = int(input())
n1 = [0] * n

for x in range(0,n):
    if x <= 1:
        n1[x] = x
    else:
        n1[x] = n1[x-1] + n1[x-2]
    if x == n-1:
        print('%d'%(n1[x]),end='')
    else:
        print('%d'%(n1[x]),end=' ')
print()
