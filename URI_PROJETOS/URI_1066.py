#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia 5 valores Inteiros. A seguir mostre quantos valores
digitados foram pares, quantos valores digitados foram ímpares,
quantos valores digitados foram positivos e quantos valores
digitados foram negativos.
Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída
Imprima a mensagem conforme o exemplo fornecido, uma 
mensagem por linha, não esquecendo o final de linha após cada uma.
Exemplo de Entrada	Exemplo de Saída
-5                  3 valor(es) par(es)
0                   2 valor(es) impar(es)
-3                  1 valor(es) positivo(s)
-4                  3 valor(es) negativo(s)
"""
print('{:=^45}'.format(' URI Online Judge | 1066 '))
print('{:^45}'.format('Pares, Ímpares, Positivos e Negativos'))
pares = 0
impar = 0
positivo = 0
negativo = 0
for x in range(5):
    n = int(input('Valores: '))
    if n %2 ==0:
         pares = pares+1
    if not n %2 ==0:
        impar = impar+1
    if n > 0:
        positivo = positivo+1
    if n < 0:
        negativo = negativo+1
 
print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))