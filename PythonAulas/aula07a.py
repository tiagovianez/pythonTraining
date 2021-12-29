#Ordem de precedência
#1. ()
#2. **
#3. * / // %
#4. + -

#PRÁTICA
# n = input('Digite um nome: ')
# print('Prazer em lhe conhecer, {}!'.format(n))

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \nO produto é {} e a \nDivisão é {}'.format(s, m, d))
print('A divisão inteira é {} e a potência {}'.format(di, e))