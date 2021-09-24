#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia um número inteiro que representa
um código de DDD para discagem interurbana.
Em seguida, informe à qual cidade o DDD pertence,
considerando a tabela abaixo:
DDD              Destination
61                Brasilia
71                Salvador
11                Sao Paulo
21                Rio de Janeiro
32                Juiz de Fora
19                Campinas
27                Vitoria
31                Belo Horizonte
Se a entrada for qualquer outro DDD que não
esteja presente na tabela acima, o programa
deverá informar: DDD nao cadastrado"""
print('{:=^45}'.format(' URI Online Judge | 1050 '))
print('{:^45}'.format('DDD'))
num=int(input().strip())
my_dic={61:'Brasilia',
   71:'Salvador',
   11:'Sao Paulo',
   21:'Rio de Janeiro',
   32:'Juiz de Fora',
   19:'Campinas',
   27:'Vitoria',
   31:'Belo Horizonte'}
if num in my_dic:
    print(my_dic[num])
else:
    print('DDD nao cadastrado')