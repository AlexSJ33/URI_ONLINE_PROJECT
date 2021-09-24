#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Faça um programa que leia 6 valores. Estes valores serão
somente negativos ou positivos (desconsidere os valores nulos).
A seguir, mostre a quantidade de valores positivos digitados.
Entrada
Seis valores, negativos e/ou positivos.
Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
Exemplo de Entrada	Exemplo de Saída
7                   4 valores positivos
-5
6
-3.4
4.6
12
"""
print('{:=^45}'.format(' URI Online Judge | 1060 '))
print('{:^45}'.format('Números Positivos'))
contador = 0
for x in range(6):
    n = float(input('Valores: '))
    if n >0:
        contador =contador+1
print('{} valores positivos'.format(contador))