#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Faça um programa que mostre os números 
pares entre 1 e 100, inclusive.
Entrada
Neste problema extremamente simples de repetição não há entrada.
Saída
Imprima todos os números pares entre 1 e 100,
inclusive se for o caso, um em cada linha."""

print('{:=^45}'.format(' URI Online Judge | 1059 '))
print('{:^45}'.format('Números Pares'))

for x in range(2,100+1,2):
    print(x)