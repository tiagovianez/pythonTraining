#CRIE UM PROGRAMA QUE LEIA UMA 'FRASE' E DIGA SE ELA É "PALINDRONO" OU NÃO, DESCONSIDERANDO OS ESPAÇOS.
phrase = str(input('Write the phrase or word: ')).strip().upper()
word = phrase.split()
together = ''.join(word)
inverse = together[::-1]
if together == inverse:
    print('Is PALINDRONE')
else:
    print('Is NOT Palindrone')
