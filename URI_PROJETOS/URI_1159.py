#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""O programa deve ler um valor inteiro X indefinidas vezes.
(O programa irá parar quando o valor de X for igual a 0).
Para cada X lido, imprima a soma dos 5 pares consecutivos a partir
de X, inclusive o X , se for par. Se o valor de entrada for 4, por exemplo,
a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que
se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.

Entrada
O arquivo de entrada contém muitos valores inteiros. O último valor do arquivo é zero.

Saída
Imprima a saida conforme a explicação acima e o exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
4                   40
11                  80
0
"""

print('{:=^45}'.format(' URI Online Judge | 1159 '))
print('{:^45}'.format('Soma de Pares Consecutivos'))


def soma_pares(num):
    cont = 1
    l = []
    p = 0
    while cont <= 5:
            
        if not num % 2 == 0:
            num += 1
        while p < cont:
            l.append(num)
            p += 1
            num += 1   
        cont +=1
    print(sum(l))

while True:
    x = int(input())
    if x <= 0:
        break
    else:
        soma_pares(x)
