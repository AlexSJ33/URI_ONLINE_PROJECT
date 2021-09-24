#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
Entrada
Não há nenhuma entrada neste problema.
Saída
Imprima a sequencia conforme exemplo abaixo.
Exemplo de Entrada	Exemplo de Saída
                    I=0 J=1
                    I=0 J=2
                    I=0 J=3
                    I=0.2 J=1.2
                    I=0.2 J=2.2
                    I=0.2 J=3.2
                    .....
                    I=2 J=?
                    I=2 J=?
                    I=2 J=?
"""
print('{:=^45}'.format(' URI Online Judge | 1098 '))
print('{:^45}'.format('Sequencia IJ 4'))

i = 0
j = 1
while i <= 2:
    for a in range(3):
        if int(i) != i:
            print('I={:.1f} J={:.1f}'.format(i,j))
        else:
            print('I={:.0f} J={:.0f}'.format(i,j))
        j += 1
    i = round(i + 0.2, 1)
    j = round(j - 2.8, 1)