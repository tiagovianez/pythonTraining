#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A
#'BASE DE CONVERSÃO:'
#- 1 PARA BINÁRIO
#- 2 PARA OCTAL
#- 3 PARA HEXADECIMAL
print('=-'*40)
print('CONVERSOR DE NÚMERO')
print('=-'*40)
n = int(input('Digite um número inteiro: '))
bs = int(input('Escolha uma base para conversão:\n'
               '1 - Binário\n'
               '2 - Octal\n'
               '3 - Hexadecimal\n'
               ' '))
if bs == 1:
    print('A conversão desse número em binário é: {}'.format(bin(n)))
elif bs == 2:
    print('A conversão desse número para OCTAL é: {}'.format(oct(n)))
elif bs == 3:
    print('A conversão desse número para HEXADECIMAL é: {}'.format(hex(n)))
else:
    print('Número de base inválida! Digite uma entre 1, 2 e 3.')


