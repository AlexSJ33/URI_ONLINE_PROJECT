#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Faça um programa que leia as notas referentes às duas avaliações de um aluno.
Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas
válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.
Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.
Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " 
seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
-3.5                nota invalida
3.5                 nota invalida
11.0                media = 6.75
10.0               
"""


print('{:=^45}'.format(' URI Online Judge | 1117 '))
print('{:^45}'.format('Validação de Nota'))

nota_valida = 0
x=0
media=0
while nota_valida!=2:
    x = float(input())
    if x>=0 and x<=10:
        media+=x/2
        nota_valida+=1
    else:
        print('nota invalida')


print('media = %.2f'%(media))