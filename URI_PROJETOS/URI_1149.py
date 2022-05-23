#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma 
de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for 
negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos 
ou negativos. Todos os valores estão na mesma linha.

Saída

Saída
A saída contém apenas um valor inteiro.

Exemplo de Entrada	Exemplo de Saída
3 2                 7
3 -1 0 -2 2         7
"""

print('{:=^45}'.format(' URI Online Judge | 1149 '))
print('{:^45}'.format('Somando Inteiros Consecutivos'))

n = list(map(int, input().split()))
i = 1
y = 0

while n[i] <= 0:
    if n[i] <=0:
        i = i + 1
    if n[i] > 0:
        break

for c in range(0,n[i]):
    y = y + n[0] + c
   
print(y)
