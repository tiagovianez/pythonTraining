#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
#PARA SALÁRIO SUPERIORES A 'R$1250.00'. CALCULE UM AUMENTO DE '10%';
#PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%;

s = float(input('Digite o salário do funcionário: '))
a1 = (s * 0.10)
a2 = (s * 0.15)
if s <= 1250:
    print('O aumento do salário desse colaborador é: R$ {:.2f}'.format(a2))
else:
    print('O aumento do salário desse colaborador é: R$ {:.2f}'.format(a1))