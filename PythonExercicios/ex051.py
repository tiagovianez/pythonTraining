#DESENVOLVA UM PROGRAMA QUE LEIA O 'PRIMEIRO TERMO' E A 'RAZÃO' DE UMA PA. NO FINAL, MOSTRE OS '10' PRIMEIROS TERMOS
#DESSA PROGRESSÃO.
t = int(input('Primeiro termo: '))
r = int(input('Digite a razão: '))
dt = t + (10 - 1) * r
for c in range(t, dt + r, r):
    print('{}'.format(c), end=" ")
print('FIM!')