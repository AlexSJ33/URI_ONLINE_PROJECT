#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia 1 valor inteiro N (2 < N < 1000). 
A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N  ...  10 x N = 10N
Entrada
A entrada contém um valor inteiro N (2 < N < 1000).
Saída
Imprima a tabuada de N, conforme o exemplo fornecido.
"""
print('{:=^45}'.format(' URI Online Judge | 1078 '))
print('{:^45}'.format('Tabuada'))

x = 1
n = int(input())
while x <= 10:
    print('{} x {} = {}'.format(x,n,(x*n)))
    x+=1
