#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia a hora inicial, minuto inicial, hora final 
e minuto final de um jogo. A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto 
e duração máxima de 24 horas.
Entrada
Quatro números inteiros representando 
a hora de início e fim do jogo.
Saída
Mostre a seguinte mensagem: 
“O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)”.

Exemplo de Entrada	Exemplo de Saída
7 8 9 10            O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
7 7 7 7             O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)
7 10 8 9            O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)"""

print('{:=^45}'.format(' URI Online Judge | 1047 '))
print('{:^45}'.format('Tempo de Jogo com Minutos'))

x = input().split()
hi, mi, hf, mf = x

hi = int(x[0])
mi = int(x[1])
hf = int(x[2])
mf = int(x[3])

if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi == hf:
    if mi < mf:
        m = mf - mi
        h = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = 23
    if mi == mf:
        h = 24
        m = 0
    
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))