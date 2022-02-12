#ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
#O PROGRAMA VAI PERGUNTAR O 'VALOR DA CASA', O 'SALÁRIO' DO COMPRADOR E EM 'QUANTOS ANOS' ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER '30%' DO SALÁRIO OU ENTÃO O EMPRÉSTIMOS SERÁ NEGADO.
print('=-'*40)
print('ANALISE DE EMPRÉSTIMO PARA AQUISIÇÃO DE UMA CASA')
print('=-'*40)
vc = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
t = float(input('Em quantos meses você quer pagar? '))
prestacao = (vc/t)
print('O valor da sua prestação mensal é: R$ {:.2f}'.format(prestacao))
if prestacao <= (0.3*s):
    print('Oba! Seu crédito bancário FOI APROVADO!')
else:
    print('Infelizmente seu crédito bancário NÃO FOI APROVADO.')
