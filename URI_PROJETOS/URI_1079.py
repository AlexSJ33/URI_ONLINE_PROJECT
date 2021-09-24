#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia 1 valor inteiro N, que representa o número de casos 
de teste que vem a seguir. Cada caso de teste consiste de 3 
valores reais, cada um deles com uma casa decimal. 
Apresente a média ponderada para cada um destes conjuntos de
3 valores, sendo que o primeiro valor tem peso 2, o segundo 
valor tem peso 3 e o terceiro valor tem peso 5.
Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha.
Cada N linha a seguir contém um caso de teste com três valores
com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada
dos 3 valores, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
3                       
6.5 4.3 6.2             5.7
5.1 4.2 8.1             6.3
8.0 9.0 10.0            9.3
"""
print('{:=^45}'.format(' URI Online Judge | 1079 '))
print('{:^45}'.format('Médias Ponderadas'))

N = float(input())

cont = 0
x = 0
media_p = []
while cont < N:
    a,b,c = input().split(" ")
    a = round(float(a),2)
    b = round(float(b),2)
    c = round(float(c),2)
    media_p.append(((a * 2 ) + (b * 3 ) + (c * 5 ))/(2+3+5))
    cont+=1
    
while x < N:
    print('{:.1f}'.format(media_p[x]))
    x+=1


"""
maior = 0
lista = {}
posicao = 0
while posicao < 100:
    valor = int(input())
    if(valor > maior):
        maior = valor
        lista[valor] = posicao
    posicao += 1
print(maior)
print(lista[maior]+1)
"""