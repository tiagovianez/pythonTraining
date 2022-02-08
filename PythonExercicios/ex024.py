#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
#Removendo os espaços do ínicio e fim
cidade = str(input('Digite o nome da cidade: ')).strip()
print('Analisando o nome da cidade...')
print('O nome da cidade tem SANTO? {}'.format(cidade[:5].upper() == 'SANTO'))
