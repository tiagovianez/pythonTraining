#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.
ano = int(input('Digite o ano desejado: '))
if ano % 4 == 0:
    print('Esse é um ano bissexto')
else:
    print('Esse não é um ano bissexto')