#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex:
# Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

n = str(input('Digite um número entre 0 a 9999: '))
print('Analisando o número...')
print('A unidade desse número é: {}'.format(n[3]))
print('A dezena desse número é: {}'.format(n[2]))
print('A centena desse número é: {}'.format(n[1]))
print('O milhar desse número é: {}'.format(n[0]))