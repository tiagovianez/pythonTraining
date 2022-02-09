#IDENTIFICANDO SE A MÉDIA DE UM ALUNO FOI BOA OU RUIM
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = ((n1 + n2) / 2)
print('Sua média foi: {:.2f}'.format(m))
if m >= 6.0:
    print('PARABÉNS! Sua média é boa!')
else:
    print('Estude mais! Sua nota foi abaixo da média.')



