#Faça um programa que leia uma frase pelo teclado e mostre:
#a) Quantas vezes aparece a letra "A";
#b) Em que posição ela parece a primeira vez;
#c) Em que posição ela aparece a última vez
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição: {}'.format(frase.rfind('A')+1))