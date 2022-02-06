#Crie um programa que leia o nome completo de uma pessoa e mostre:
#a) O nome com todas as letras maiúsculas;
#b) O nome com todas as letras minúsculas;
#c) Quantas letras ao to.do(sem considerar espaços);
#d) Quantas letras tem o primeiro nome;

nome = str(input('Digite um nome completo: ')).strip()
print('Analisando o nome...')
print('Seu nome em caixa alta: {}'.format(nome.upper()))
print('Seu nome em caixa baixa: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Quantas letras tem o primeiro nome: {}'.format(nome.find(' ')))
