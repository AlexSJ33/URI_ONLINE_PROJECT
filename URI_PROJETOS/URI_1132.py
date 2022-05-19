#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a 
soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.


Exemplo de Entrada	Exemplo de Saída
100                 13954
200
"""

print('{:=^45}'.format(' URI Online Judge | 1132 '))
print('{:^45}'.format('Múltiplos de 13'))

x = int(input())
y = int(input())
soma = 0
if x < y:
    for z in range(x,y+1):
        if not (z % 13 == 0):
            soma += z
    print(soma)
else:
    for z in range(y,x+1):
        if not (z % 13 == 0):
            soma += z
    print(soma)
        