#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s1 = float(input('Digite o salário atual: R$'))
s2 = (s1 * 0.15) + s1
print('Um funcionário que ganhava R${:.2f}, passará a ganhar R${:.2f}'.format(s1, s2))