#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um programa que leia um valor inteiro N (1 < N < 1000).
Este N é a quantidade de linhas de saída que serão apresentadas
na execução do programa.
Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.


Exemplo de Entrada	Exemplo de Saída
5                   1 1 1
                    2 4 8
                    3 9 27
                    4 16 64
                    5 25 125
"""
print('{:=^45}'.format(' URI Online Judge | 1143 '))
print('{:^45}'.format('Quadrado e ao Cubo'))

n = int(input())
y = 1

for x in range(n):
    print(y, y**2, y**3, end=" ")
    print()
    y += 1
