##########Conversão de Tempo############

"""Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
   e informe-o expresso no formato horas:minutos:segundos.
   Entrada
   O arquivo de entrada contém um valor inteiro N.
   Saída
   Imprima o tempo lido no arquivo de entrada (segundos), convertido para
   horas:minutos:segundos, conforme exemplo fornecido."""
t=int(input())
h_s=3600
h= int(t/h_s)
m= int(t-(h_s*h))/60
s= int(t % h_s)%60
print ("%d:%d:%d" % (h, m, s))