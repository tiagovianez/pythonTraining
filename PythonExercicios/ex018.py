#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite o valor do ângulo: '))
#CONVERSÃO PARA RADIANOS
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))

print('O ângulo de {} tem o SENO de {:.2f}\n'
      'O ângulo de {} tem o COSSENO de {:.2f}\n'
      'O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, seno, a, cosseno, a, tangente))