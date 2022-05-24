#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída

"""

print('{:=^45}'.format(' URI Online Judge | 1156 '))
print('{:^45}'.format('Sequência S II'))

num=1
cont=0
for x in range(1,40,2):
    a=x/num
    cont=cont+a
    num=num*2
print('{:.2f}'.format(cont))