"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
   no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
   A seguir mostre o valor lido e a relação de notas necessárias.
   Entrada
   O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
   Saída
   Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
   conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha,
   caso contrário seu programa apresentará a mensagem: “Presentation Error”."""
n=int(input())
if 0 < n < 1000000:
    print(n)
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
    nota= 1
    q= int(resto/nota)
    print(q," nota(s) de R$ 1,00")