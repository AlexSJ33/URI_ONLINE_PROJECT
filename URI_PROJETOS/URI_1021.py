"""Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.
Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
Obs: Utilize ponto (.) para separar a parte decimal."""
"""
############## meu codigo ################
n=float(input())
if 0 < n < 1000000:
    print("NOTAS:")
    resto=n
    nota= 100
    q= int(resto/nota)
    print(q," nota(s) de R$ 100,00")
    resto=resto%nota
    nota= 50
    q= int(resto/nota)
    print(q," nota(s) de R$ 50,00")
    resto=resto%nota
    nota= 20
    q= int(resto/nota)
    print(q," nota(s) de R$ 20,00")
    resto=resto%nota
    nota= 10
    q= int(resto/nota)
    print(q," nota(s) de R$ 10,00")
    resto=resto%nota
    nota= 5
    q= int(resto/nota)
    print(q," nota(s) de R$ 5,00")
    resto=resto%nota
    nota= 2
    q= int(resto/nota)
    print(q," nota(s) de R$ 2,00")
    resto=resto%nota

    print("MOEDAS:")
    nota= 1
    q= int(resto/nota)
    print(q," moeda(s) de R$ 1,00")
    nota= 0.50
    q= int(resto/nota)
    print(q," moeda(s) de R$ 0,50")
    nota= 0.25
    q= int(resto/nota)
    print(q," moeda(s) de R$ 0,25")
    nota= 0.10
    q= int(resto/nota)
    print(q," moeda(s) de R$ 0,10")
    nota= 0.05
    q= int(resto/nota)
    print(q," moeda(s) de R$ 0,05")
    nota= 0.01
    q= int(resto/nota)
    print(q," moeda(s) de R$ 0,01")"""

################  o do cara  #####################

v = float(input())
if 0 <= v <= 1000000.00:
    notas = [100, 50, 20, 10, 5, 2, 1]
    moedas = [50, 25, 10, 5, 1]
    print('NOTAS:')
    vn = v // 1
    for n in notas:
        x = vn // n
        if n != 1:
            print("%i nota(s) de R$ %.2f" % (x, n))
        else:
            print('MOEDAS:')
            print("%i moeda(s) de R$ %.2f" % (x, n))
        vn -= x * n
    v = int(v*100)
    vn = int(str(v)[-2:])
    for n in moedas:
        x = vn // n
        m = float(n)/100
        print("%i moedas(s) de R$ %.2f" % (x, m))
        vn -= x * n