#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno.
Calcule e imprima a média semestral. O programa só deverá aceitar notas válidas
(uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que
informe um código (1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente,
(aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a execução
de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

Entrada
O arquivo de entrada contém vários valores reais, positivos ou negativos. Quando forem lidas duas notas válidas,
deve ser lido um valor inteiro X . O programa deve parar quando o valor lido para este X for igual a 2.

Saída
Se uma nota inválida for lida, deve ser impressa a mensagem “nota invalida”. Quando duas notas válidas forem lidas,
deve ser impressa a mensagem “media = ” seguido do valor do cálculo.
Antes da leitura de X deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e esta mensagem deve ser apresentada
novamente se o valor da entrada padrão para X for menor do que 1 ou maior do que 2, conforme o exemplo abaixo.

A média deve ser impressa com dois dígitos após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
-3.5                nota invalida
3.5                 nota invalida
11.0                media = 6.75
10.0                novo calculo (1-sim 2-nao)
4                   novo calculo (1-sim 2-nao)
1                   media = 8.50
8.0                 novo calculo (1-sim 2-nao)
9.0
2
"""

print('{:=^45}'.format(' URI Online Judge | 1118 '))
print('{:^45}'.format('Várias Notas Com Validação'))

s = True
while s:
        nota_valida = 0
        x=0
        media=0
        while nota_valida!=2:
            x = float(input())
            if x>=0 and x<=10:
                media+=x/2
                nota_valida+=1
            else:
                print('nota invalida')
        print('media = %.2f'%(media))

        n = int(input('novo calculo (1-sim 2-nao)\n'))
        while n < 1 or n > 2:
            n = int(input('novo calculo (1-sim 2-nao)\n'))
        if n == 1: 
            continue
        else:
            break