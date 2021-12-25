#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p1 = float(input('Digite o preço: '))
p2 = (p1 * 0.95)
print('O preço desse produto com desconto de 5% fica: R${:.2f}'.format(p2))