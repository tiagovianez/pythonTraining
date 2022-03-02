#FAÇA UM PROGRAMA QUE LEIA UM 'NÚMERO INTEIRO' E DIGA SE ELE É OU NÃO É UM 'NÚMERO PRIMO'.
n = int(input('Digite um número: '))
tot = 0 #CONTADOR DE QUANTAS VEZES O NÚMERO FOI DIVIDIDO.
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1 #ACUMULADOR
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[m0 número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('É por isso ele É PRIMO!')
else:
    print('E por isso ele não é PRIMO!')

