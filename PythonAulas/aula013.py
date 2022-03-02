for c in range(6, 0, -1): #CONTAGEM DECRESCENTE
    print(c)
print('FIM')

######################
for c in range(0, 20, 2): #CONTAGEM DE 0 A 7, PULANDO EM 2 EM 2:
    print(c)
print('FIM!')

######################
n = int(input('Digite um número: ')) #CONTAGEM CRESCENTE ATÉ O VALOR DE ENTRADA.
for c in range(0, n+2):
    print(c)
print('FIM')

######################
i = int(input('Início: ')) #De onde irá startar os passos
f = int(input('Fim: '))  #Até onde irá finalizar os passos
p = int(input('Passo: '))  #Ritmo
for c in range(i, f+1, p):
    print(c)
print('FIM')
#######################
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório dos valores digitados é {}.'.format(s))