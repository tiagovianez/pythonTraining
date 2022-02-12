import datetime
# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
#- SE ELE 'AINDA VAI SE ALISTAR' AO SERVIÇO MILITAR.
#- SE É A 'HORA DE SE ALISTAR'.
#- SE 'JÁ PASSOU DO TEMPO' DO ALISTAMENTO
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.
dn = int(input('Digite o seu ANO DE NASCIMENTO: '))
date = datetime.date.today()
y = int(date.strftime("%Y"))
idade = (y-dn)
print('A sua idade é: {} anos'.format(idade))
if idade < 18:
    print('Você ainda NÃO POSSUI IDADE SUFICIENTE para se alistar.')
elif idade == 18:
    print('JÁ ESTÁ NA HORA de se alistar!')
else:
    print('Você JÁ PASSOU DO TEMPO do alistamento.')
