#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia 6 valores. Em seguida, mostre quantos destes valores
digitados foram positivos. Na próxima linha, deve-se mostrar
a média de todos os valores positivos digitados, com um dígito
após o ponto decimal.
Entrada
A entrada contém 6 números que podem ser valores inteiros ou
de ponto flutuante. Pelo menos um destes números será positivo.
Saída
O primeiro valor de saída é a quantidade de valores positivos.
A próxima linha deve mostrar a média dos valores positivos digitados.
Exemplo de Entrada	Exemplo de Saída
7                   4 valores positivos
-5                  7.4
6
-3.4
4.6
12
"""

print('{:=^45}'.format(' URI Online Judge | 1064 '))
print('{:^45}'.format('Positivos e Média'))
contador = 0
soma = 0
for x in range(6):
    n = float(input('Valores: '))
    if n >0:
        soma +=n
        contador =contador+1
        media = soma/contador     
print('{} valores positivos'.format(contador))
print('{:.1f}'.format(media))