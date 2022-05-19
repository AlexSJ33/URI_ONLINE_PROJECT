#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim).
Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido).
O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.


Exemplo de Entrada	Exemplo de Saída
8                   MUITO OBRIGADO
1                   Alcool: 1
7                   Gasolina: 2
2                   Diesel: 0
2
4
"""

print('{:=^45}'.format(' URI Online Judge | 1134 '))
print('{:^45}'.format('Tipo de Combustível'))

alcool = 0
gasolina = 0
diesel = 0

while True:
    n = int(input())
    if n == 4:
        break
    elif n == 1:
        alcool += 1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel += 1
    else:
        continue
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))