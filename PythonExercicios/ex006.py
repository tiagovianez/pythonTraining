#Crie um algorítmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** 0.5
print('O dobro desse valor é: {}\nSeu triplo é: {}\nSua raiz quadrada é: {:.2f}.'.format(d, t, rq))