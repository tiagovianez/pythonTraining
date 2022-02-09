#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada km acima do limite.


v = float(input('Digite a velocidade do carro em km/h: '))
multa = (v-80) * 7
if v > 80:
    print('Atenção, você foi multado por ter excedido o limite de 80km/h!\n'
          'O valor da sua multa é R$ {:.2f}'.format(multa))
elif v == 80:
    print('Você está no limite da velocidade!')
else:
    print('Está tranquilo, você está abaixo do limite da velocidade!\n'
          'Dirija com segurança!')


