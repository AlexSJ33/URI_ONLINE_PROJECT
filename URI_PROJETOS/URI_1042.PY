"""
Leia 3 valores inteiros e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente, uma linha
em branco e em seguida, os valores na sequência como foram lidos.
"""

n, x, y = list(map(int,input().split()))
lista = [n,x,y]
lista.sort()
for x in lista:
    print(x)
print()
for b in n, x, y:
    print(b)