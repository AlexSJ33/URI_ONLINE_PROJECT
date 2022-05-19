#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um programa que leia um valor inteiro N. 
Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.


Exemplo de Entrada	Exemplo de Saída
7                   1 2 3 PUM
                    5 6 7 PUM
                    9 10 11 PUM
                    13 14 15 PUM
                    17 18 19 PUM
                    21 22 23 PUM
                    25 26 27 PUM
"""
print('{:=^45}'.format(' URI Online Judge | 1142 '))
print('{:^45}'.format('PUM'))

n = int(input())
y = 1

for x in range(1, n+1):
    for p in range(y,y+3):
        print(p,end=" ")
    print('PUM')
    y+=4
            
