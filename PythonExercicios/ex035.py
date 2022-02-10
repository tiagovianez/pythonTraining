#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.
a = float(input('Digite o primeiro comprimento da reta: '))
b = float(input('Digite o segundo comprimento da reta: '))
c = float(input('Digite o terceiro comprimento da reta: '))
if a + b > c:
    print('Podemos formar um triângulo!')
else:
    print('Não é possível formar um triângulo')