#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer
uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número
de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem
"Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo
deve ser executado novamente solicitando o número de gols marcados pelos times em 
uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo 
Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". 
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a 
descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.


Exemplo de Entrada	Exemplo de Saída
3 2                 Novo grenal (1-sim 2-nao)
1                   Novo grenal (1-sim 2-nao)
2 3                 Novo grenal (1-sim 2-nao)
1                   3 grenais
3 1                 Inter:2
2                   Gremio:1
                    Empates:0
                    Inter venceu mais
"""

print('{:=^45}'.format(' URI Online Judge | 1131 '))
print('{:^45}'.format('Grenais'))

grenais = 0
v_inter = 0
v_gremio = 0
empates = 0

while True:
    i,g = list(map(int,input().split()))
    grenais +=1
    if i > g:
        v_inter += 1
    elif g > i:
        v_gremio += 1
    else:
        empates +=1

    n = int(input('Novo grenal (1-sim 2-nao)\n'))
    while n < 1 or n > 2:
        n = int(input('Novo grenal (1-sim 2-nao)\n'))
    if n == 1:
        continue  
    else:
        break

print('{} grenais'.format(grenais))
print('Inter:{}'.format(v_inter))
print('Gremio:{}'.format(v_gremio))
print('Empates:{}'.format(empates))
if v_inter > v_gremio:
    print('Inter venceu mais')
elif v_gremio > v_inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')

