#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite o seu nome completo: ')).strip()
print('Esse nome tem SILVA? {}'.format('SILVA' in nome.upper()))


