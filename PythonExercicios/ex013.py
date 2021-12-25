#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s1 = float(input('Digite o salário: '))
s2 = (s1 * 0.15) + s1
print('O seu novo salário é: R${:.2f}'.format(s2))