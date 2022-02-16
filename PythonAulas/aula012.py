## CONDICOES ALINHADAS
print('='*40)
print('CRIANDO UMA CONDIÇÃO ALINHADA')
print('='*40)
nome = str(input('Qual o seu nome? '))
if nome == 'Tiago':
    print('Que nome bonito!')
elif nome == 'Lucas' or nome == 'João' or nome == 'Maria':
    print('Seu nome é bem conhecido no Brasil.')
elif nome in 'Ana Jéssica Juliana Mariana Vanessa':
    print('Que belo nome você tem!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))