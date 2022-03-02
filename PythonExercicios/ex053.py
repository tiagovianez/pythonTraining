#CRIE UM PROGRAMA QUE LEIA UMA 'FRASE' E DIGA SE ELA É "PALINDRONO" OU NÃO, DESCONSIDERANDO OS ESPAÇOS.
phrase = str(input('write a phrase or word: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
print('You write a phrase {}'.format(together))
if together == together[::-1]:
    print('IS POLIDROME')
else:
    print('NOT POLINDROME')
print(together[::-1])