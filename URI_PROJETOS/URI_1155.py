#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 1/2 + 1/3 + … + 1/100

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída

"""

print('{:=^45}'.format(' URI Online Judge | 1155 '))
print('{:^45}'.format('Sequência S'))

s=1
for i in range (2,101):
    s=s+(1/i)
print('{:.2f}'.format(s))
