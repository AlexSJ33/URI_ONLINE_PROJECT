#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia um valor inteiro X (1 <= X <= 1000).
Em seguida mostre os ímpares de 1 até X, um valor
por linha, inclusive o X, se for o caso.
Entrada
O arquivo de entrada contém 1 valor inteiro qualquer.
Saída
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

Exemplo de Entrada	Exemplo de Saída
8                    1
                     3
                     5
                     7
"""
print('{:=^45}'.format(' URI Online Judge | 1067 '))
print('{:^45}'.format('Números Ímpares'))

n = int(input())
for x in range(1, n+1, 2):
    print(x)