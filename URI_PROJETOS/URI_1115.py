#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um programa para ler as coordenadas (X,Y) 
de uma quantidade indeterminada de pontos no sistema cartesiano.
Para cada ponto escrever o quadrante a que ele pertence.
O algoritmo será encerrado quando pelo menos uma de duas coordenadas
for NULA (nesta situação sem escrever mensagem alguma).
Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.
Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

Exemplo de Entrada	Exemplo de Saída
2 2                 primeiro
3 -2                quarto
-8 -1               terceiro
-7 1                segundo
0 2
"""
# se x for <= 0 e y >= 0 --> segundo quadrante
# se x for >= 0 e y >= 0 --> primeiro quadrante
# se x for <= 0 e y <= 0 --> terceiro quadrante
# se x for >= 0 e y <= 0 --> quarto quadrante

print('{:=^45}'.format(' URI Online Judge | 1115 '))
print('{:^45}'.format('Quadrante'))

while True:
    try:
        x,y = list(map(int,input().split()))
        if x == 0 or y ==0:
            break
        # se x for <= 0 e y >= 0 --> segundo quadrante
        elif x <= 0  and y >= 0:
            print('segundo')
        # se x for >= 0 e y >= 0 --> primeiro quadrante
        elif x >= 0 and y >= 0:
            print('primeiro')
        # se x for <= 0 e y <= 0 --> terceiro quadrante
        elif x <= 0 and y <= 0:
            print('terceiro')
        # se x for >= 0 e y <= 0 --> quarto quadrante
        elif x >= 0 and y <= 0:
            print('quarto')
    except EOFError:
        break