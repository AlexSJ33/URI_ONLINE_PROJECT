#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Faça um programa que leia 5 valores inteiros.
Conte quantos destes valores digitados são pares e mostre esta informação.
Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída
Imprima a mensagem conforme o exemplo fornecido,
indicando a quantidade de valores pares lidos.
Exemplo de Entrada	Exemplo de Saída
7                     3 valores pares
-5
6
-4
12
"""

print('{:=^45}'.format(' URI Online Judge | 1065 '))
print('{:^45}'.format('Pares entre Cinco Números'))
contador = 0
soma = 0
for x in range(5):
    n = int(input('Valores: '))
    if n %2 ==0:
         contador =contador+1
 
print('{} valores pares'.format(contador))
