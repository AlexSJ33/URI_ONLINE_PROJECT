#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um programa que leia 2 valores X e Y e que imprima todos os valores 
entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.


Exemplo de Entrada	Exemplo de Saída
10                  12
18                  13
                    17
"""

print('{:=^45}'.format(' URI Online Judge | 1133 '))
print('{:^45}'.format('Resto da Divisão'))


x = int(input())
while x < 0:
    x = int(input())
y = int(input())
while y < 0:
    y = int(input())
        
if x < y:
    for z in range(x+1,y):
        if (z % 5 == 2) or (z % 5 == 3):
            print(z, end='\n')
else:
    for z in range(y+1,x):
        if (z % 5 == 2) or (z % 5 == 3):
            print(z, end='\n')
            
