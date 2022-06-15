#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y
ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de
teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma dos consecutivos números ímpares a partir do valor X.

Exemplo de Entrada	Exemplo de Saída
2                   21
4 3                 24
11 2
"""

print('{:=^45}'.format(' URI Online Judge | 1158 '))
print('{:^45}'.format('Soma de Ímpares Consecutivos III'))


n = int(input())

def entradas(num):
    count = 1

    while count <= num:
        l = []
        p = 0
        x,y = list(map(int,input().split()))
        
        if x % 2 == 0:
            x += 1
        
        while p < y:
            l.append(x)
            p += 1
            x += 2        
        
        print(sum(l))
        count +=1
    
entradas(n)
