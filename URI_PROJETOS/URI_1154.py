#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, 
a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de
idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.
A média deve ser impressa com dois dígitos após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
34                  39.25 
56
44
23
-2
"""

print('{:=^45}'.format(' URI Online Judge | 1154 '))
print('{:^45}'.format('Idades'))


soma = 0
cont = 0
while True:
    n = int(input())
    if n <=0:
        break
    soma += n
    cont += 1

print('{:.2f}'.format(soma/cont))