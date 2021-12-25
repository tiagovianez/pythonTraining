#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
##Forma mais ráṕida e fácil
n = int(input('Digite um valor: '))
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)