#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira;
#Arredondamento para cima e para baixo
from math import trunc, floor, ceil
n = float(input('Digite um valor: '))
print('O valor {} em inteiro corresponde a: {}'.format(n, trunc(n)))
print('O valor {} arredondado para cima corresponde a: {}'.format(n, ceil(n)))
print('O valor {} arredondado para baixo corresponde a: {}'.format(n, floor(n)))
