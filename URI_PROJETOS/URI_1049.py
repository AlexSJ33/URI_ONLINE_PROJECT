#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Neste problema, você deverá ler 3 palavras
que definem o tipo de animal possível segundo
o esquema abaixo, da esquerda para a direita.
Em seguida conclua qual dos animais seguintes
foi escolhido, através das três palavras fornecidas.
Entrada
A entrada contém 3 palavras, uma em cada linha,
necessárias para identificar o animal segundo a
figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
"""

print('{:=^45}'.format(' URI Online Judge | 1049 '))
print('{:^45}'.format('Animal'))
animal_1 = str(input().strip().lower())
animal_2 = str(input().strip().lower())
animal_3 = str(input().strip().lower())
if animal_1 == 'vertebrado' and animal_2 == 'ave' and animal_3 == 'carnivoro':
    print('aguia')
elif animal_1 == 'vertebrado' and animal_2 == 'ave' and animal_3 == 'onivoro':
    print('pomba')
elif animal_1 == 'vertebrado' and animal_2 == 'mamifero' and animal_3 == 'onivoro':
    print('homem')
elif animal_1 == 'vertebrado' and animal_2 == 'mamifero' and animal_3 == 'herbivoro':
    print('vaca')
elif animal_1 == 'invertebrado' and animal_2 == 'inseto' and animal_3 == 'hematofago':
    print('pulga')
elif animal_1 == 'invertebrado' and animal_2 == 'inseto' and animal_3 == 'herbivoro':
    print('lagarta')
elif animal_1 == 'invertebrado' and animal_2 == 'anelideo' and animal_3 == 'hematofago':
    print('sanguessuga')
elif animal_1 == 'invertebrado' and animal_2 == 'anelideo' and animal_3 == 'onivoro':
    print('minhoca')