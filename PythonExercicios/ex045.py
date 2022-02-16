#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ!
from random import randint
from time import sleep

#definindo os itens
itens = ('Pedra', 'Papel', 'Tesoura')

#jogada do computador
computador = randint(0, 2)

#apresentar as opções
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada?: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-='*20)

#mostrando o que cada um jogou...
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 20)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCE')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA')

else:
    print('JOGADA INVÁLIDA')