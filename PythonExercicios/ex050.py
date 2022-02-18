#DESENVOLVA UM PROGRAMA QUE LEIA 'SEIS NÚMEROS INTEIROS' E MOSTRE A SOMA APENAS DAQUELES QUE FOREM 'PARES'.
#SE O VALOR DIGITADO FOR 'IMPAR', DESCONSIDERE-O.
soma = 0
cont = 0
for c in range(1, 7): #CRIANDO UM LAÇO DE REPETIÇÃO
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você digitou {} números PARES e a soma deles equivale a {}.'.format(cont, soma))