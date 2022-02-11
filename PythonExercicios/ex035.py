#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a + b > c and a + c > b and c + b > a:
    print('PODEMOS FORMAR um triângulo, com os segmentos citados!')
else:
    print('NÃO É POSSÍVEL formar um triângulo!')