#DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU 'IMC' E MOSTRE SEU STATUS,
#DE ACORDO COM A TABELA ABAIXO:
#-ABAIXO DE 18.5: ABAIXO DO PESO
#-ENTRE 18.5 E 25: PESO IDEAL
#-25 ATÉ 30: SOBREPESO
#-30 ATÉ 40: OBESIDADE
#-ACIMA DE 40: OBESIDADE MÓRBIDA
import math
print('='*20)
print('CALCULADORA DE IMC')
print('='*20)
p = float(input('Digite o seu Peso em KG (ex.: 69.2): '))
a = float(input('Digite a sua Altura (ex.: 1.70): '))
imc = (p/(pow(a, 2)))
print('Seu IMC é de: {:.2f} kg/m².'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 < imc < 25:
    print('Você está com PESO IDEAL!')
elif 25 < imc <= 30:
    print('Você está com SOBREPESO!')
elif 30 < imc <= 40:
    print('Você está com OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')
