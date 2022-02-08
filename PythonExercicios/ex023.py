#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex:
# Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
n = str(input('Digite um valor entre 0 e 9999: '))
print('A unidade desse valor é: {}'.format(n[3]))
print('A dezena desse valor é: {}'.format(n[2]))
print('A centena desse valor é: {}'.format(n[1]))
print('A milhar desse valor é: {}'.format(n[0]))