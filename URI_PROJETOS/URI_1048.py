#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A empresa ABC resolveu conceder um aumento
de salários a seus funcionários de acordo
com a tabela abaixo:
Salário	             Percentual de Reajuste
0 - 400.00                 15%
400.01 - 800.00            12%
800.01 - 1200.00           10%
1200.01 - 2000.00           7%
Acima de 2000.00            4%
"""

print('{:=^45}'.format(' URI Online Judge | 1048 '))
print('{:^45}'.format('Aumento de Salário'))
valor = float(input())
r1 = valor*0.15
r2 = valor*0.12
r3 = valor*0.10
r4 = valor*0.07
r5 = valor*0.04
if valor < 400.01:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %'.format(valor+r1,r1))
elif valor >= 400.01 and valor < 800.01:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %'.format(valor+r2,r2))
elif valor >= 800.01 and valor < 1200.01:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %'.format(valor+r3,r3))
elif valor >= 1200.01 and valor < 2000.01:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %'.format(valor+r4,r4))
else:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %'.format(valor+r5,r5))
