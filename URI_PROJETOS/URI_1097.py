#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
Entrada
Não há nenhuma entrada neste problema.
Saída
Imprima a sequencia conforme exemplo abaixo.
Exemplo de Entrada	Exemplo de Saída
                    I=1 J=7
                    I=1 J=6
                    I=1 J=5
                    I=3 J=9
                    I=3 J=8
                    I=3 J=7
                    ...
                    I=9 J=15
                    I=9 J=14
                    I=9 J=13
"""
print('{:=^45}'.format(' URI Online Judge | 1097 '))
print('{:^45}'.format('Sequencia IJ 3'))
i = 1
j = 7

while(i<10):
    for x in range(3):
        print('I={} J={}'.format(i,j))
        
        j += -1
    i += 2
    j = i + 6
