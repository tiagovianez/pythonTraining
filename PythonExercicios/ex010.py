#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode comprar.
#Considere: US$1,00 = R$ 3,27
n = int(input('Digite o valor em reais presente na carteira do cliente: '))
d = (n / 3.27)
print('A quantidade em dólar que o cliente pode adquirir é US$ {:.2f}'.format(d))