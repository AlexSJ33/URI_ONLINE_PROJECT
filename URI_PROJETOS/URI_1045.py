"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os
em ordem decrescente, de modo que o lado A representa o maior dos 3 lados.
A seguir, determine o tipo de triângulo que estes três lados formam,
com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A^2 = B^2 + C^2, apresente a mensagem: TRIANGULO RETANGULO
se A^2 > B^2 + C^2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A^2 < B^2 + C^2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
"""
from math import pow
n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))
n3 = float(input('Insira o terceiro numero: '))
lista = [n1,n2,n3]
ordenada = sorted(lista, key=float, reverse=True)
a = ordenada[0]
b = ordenada[1]
c = ordenada[2]
print ('A = {}\nB = {}\nC = {}'.format(a,b,c))


if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif pow(a,2) == pow(b,2) + pow(c,2):
    print('TRIANGULO RETANGULO')
elif pow(a,2) > pow(b,2) + pow(c,2):
    print('TRIANGULO OBTUSANGULO')
else:
    print('TRIANGULO ACUTANGULO')
if (a == b == c):
    print('TRIANGULO EQUILATERO')
elif (a == b) or (a == c) or (b == c):
    print('TRIANGULO ISOSCELES')
