#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
Entrada
Não há nenhuma entrada neste problema.
Saída
Imprima a sequencia conforme exemplo abaixo
Exemplo de Entrada	Exemplo de Saída
                    I=1 J=7
                    I=1 J=6
                    I=1 J=5
                    I=3 J=7
                    I=3 J=6
                    I=3 J=5
                    ...
                    I=9 J=7
                    I=9 J=6
                    I=9 J=5
"""
print('{:=^45}'.format(' URI Online Judge | 1096 '))
print('{:^45}'.format('Sequencia IJ 2'))
I=-1
for i in range (1,6):
    i=I+2
    print('I={} J={}'.format(i,7))
    print('I={} J={}'.format(i,6))
    print('I={} J={}'.format(i,5))
    I=i
