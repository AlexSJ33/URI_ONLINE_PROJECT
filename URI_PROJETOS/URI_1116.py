#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo.
Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.
Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.
Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.
Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

Exemplo de Entrada	Exemplo de Saída
3                   -1.5
3 -2                divisao impossivel
-8 0                0.0
0 8                
"""


print('{:=^45}'.format(' URI Online Judge | 1116 '))
print('{:^45}'.format('Dividindo X por Y'))
N = int(input())
qtde = 0

while qtde < N:
    try:
        x,y = list(map(int,input().split()))
        qtde +=1
        if x < 0:
            print('divisao impossivel')
        else:
            print('{:.1f}'.format(x/y))
    except ZeroDivisionError:
        print('divisao impossivel')
        continue