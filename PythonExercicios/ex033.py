#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O 'MAIOR' E QUAL É O 'MENOR'.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('O número {} é o maior entre {} e {}'.format(n1, n2, n3))
elif n2 > n1 and n2 > n3:
    print('O número {} é o maior entre {} e {}'.format(n2, n1, n3))
else:
    print('O número {} é o maior entre {} e {}'.format(n3, n1, n2))
