"""
    Com base na tabela abaixo, escreva um programa que leia 
    o código de um item e a quantidade deste item.
    A seguir, calcule e mostre o valor da conta a pagar.
"""
tabela = ['codigo','especificação','preço']
linha1 = {1:' 1   | Cachorro Quente  | R$ 4.00',
          2:' 2   | X-Salada         | R$ 4.50',
          3:'3   | X-Bacon          | R$ 5.00',
          4:' 4   | Torrada simples  | R$ 2.00',
          5:' 5   | Refrigerante     | R$ 1.50'}
linha2 = {1:'Cachorro quente',2:'X-Salada',3:'X-Bacon',4:'Torrada simples',5:'Refrigerante'}

produtos= {1:4.0,2:4.5,3:5.0,4:2.0,5:1.5}
print('\n',tabela[0],'|',tabela[1],'|',tabela[2])
print("---------------------------------")
print("",linha1[1],'\n',linha1[2],'\n',"",linha1[3],'\n',linha1[4],'\n',linha1[5])

n, y = map(int,input('\nInforme codigo e quantidade do seu pedido:').split())
chave = n
n = float(produtos[n])*y

if chave in linha2:
    print('\nSaindo',y, linha2[chave], 'no capricho!')
print(f"Total a pagar: R$ {n:.2f}")