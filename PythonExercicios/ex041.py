#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE
#SUA CATEGORIA, DE ACORDO COM A IDADE:
#- ATÉ 9 ANOS: MIRIM
#- ATÉ 14 ANOS: INFANTIL
#- ATÉ 19 ANOS: JUNIOR
#- ATÉ 20 ANOS: SÊNIOR
#- ACIMA: MASTER
import datetime
print('=-'*20)
print('E aí, preparado para essa Confederação?!')
print('=-'*20)
an = int(input('Por favor, digite o seu ANO DE NASCIMENTO :'))
date = datetime.date.today()
y = int(date.strftime("%Y"))
idade = (y-an)
print('Sua idade é: {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria é: MIRIM')
elif 9 < idade <= 14:
    print('Sua categoria é: INFANTIL')
elif 14 < idade <= 19:
    print('Sua categoria é: JÚNIOR')
elif 19 < idade <= 20:
    print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER')


