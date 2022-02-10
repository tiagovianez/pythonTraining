#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.
d = int(input('Qual a distância da sua viagem em KM? '))
vp1 = (d * 0.5)
vp2 = (d * 0.45)
if d <= 200:
    print('O preço da sua passagem para essa viagem é: R$ {:.2f}'.format(vp1))
else:
    print('O preço da sua passagem para essa viagem é: R$ {:.2f}'.format(vp2))

