#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Este programa deve ler uma variável inteira X inúmeras vezes
(deve parar quando o valor no arquivo de entrada for igual a zero).
Para cada valor lido imprima a sequência de 1 até X, com um espaço 
entre cada número e seu sucessor.

Entrada
O arquivo de entrada contém vários números inteiros.
O último número no arquivo de entrada é 0.

Saída
Para cada número N do arquivo de entrada deve ser impressa uma
linha de 1 até N, conforme o exemplo abaixo. Não deve haver espaço
em branco após o último valor da linha.

Exemplo de Entrada	Exemplo de Saída
5                   1 2 3 4 5
10                  1 2 3 4 5 6 7 8 9 10
3                   1 2 3
0                   
"""

print('{:=^45}'.format(' URI Online Judge | 1146 '))
print('{:^45}'.format('Sequências Crescentes'))


while True:
    n = int(input())
    if n == 0:
        break
    else:
        for x in range(1,n):
            print(x,end=' ')
        print(n,end='\n')
