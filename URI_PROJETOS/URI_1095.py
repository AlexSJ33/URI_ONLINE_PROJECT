#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
Entrada
Não há nenhuma entrada neste problema.
Saída
Imprima a sequencia conforme exemplo abaixo

Exemplo de Entrada	Exemplo de Saída
                    I=1 J=60
                    I=4 J=55
                    I=7 J=50
                    ...
                    I=? J=0
"""
print('{:=^45}'.format(' URI Online Judge | 1095 '))
print('{:^45}'.format('Sequencia IJ 1'))
i = -2
j = 65
while j > 0:
    j -=5
    i +=3
    print('I={} J={}'.format(i,j))