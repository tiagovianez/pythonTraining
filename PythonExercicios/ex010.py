#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode comprar.
#Considere: US$1,00 = R$ 3,27
n = float(input('Digite o valor em reais presente na carteira do cliente: R$'))
d = (n / 3.27)
print('Com R$ {:.2f} você pode comprar: US$ {:.2f}'.format(n, d))