#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacenete de um triangulo retangulo, calcule e mostre
#o comprimento da hipotenusa.
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('O valor da hipotenusa é: {:.2f}'.format(math.hypot(co, ca)))
