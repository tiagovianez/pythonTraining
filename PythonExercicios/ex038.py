#ESCREVA UM PROGRAMA QUE LEIA 'DOIS NUMEROS INTEIROS' E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
#- O 'PRIMEIRO VALOR' É MAIOR
#- O 'SEGUNDO VALOR' É MAIOR
#- 'NÃO EXISTE' VALOR MAIOR, OS DOIS SÃO 'IGUAIS'
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O PRIMEIRO VALOR {} é o MAIOR.'.format(n1))
elif n2 > n1:
    print('O SEGUNDO VALOR {} é o MAIOR.'.format(n2))
else:
    print('NÃO EXISTE valor maior, os dois são IGUAIS.')