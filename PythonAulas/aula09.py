#FATIAMENTO
frase = '    Curso em Vídeo Python    '
# print(frase[:13])
print('Pulando a string em 2 em 2: {}'.format(frase[::2]))
print('Contador de letras em caixa alta: {}'.format(frase.upper().count('V')))
print('Contador de letras em caixa baixa: {}'.format(frase.lower().count('r')))
print('Quantas letras tem na frase, considerando os espaços: {}'.format(len(frase)))
print('Quantas letras tem na frase, desconsiderando os espaços: {}'.format(len(frase.strip())))
print('Substituindo a palavra Python por Android:\n{}'.format(frase.replace('Python', 'Android')))
print('Verificando se uma palavra está na frase: {}'.format('Curso' in frase))
print('Verificando a posição de uma frase :{}'.format(frase.find('Curso')))

#CRIANDO UMA LISTA
frase1 = 'Curso em Vídeo Python'
print('lista: {}'.format(frase1.split()))
dividido = frase1.split()
print('Mostrando apenas a primeira palavra da frase1: {}'.format(dividido[0]))
print('Pegando a primeira palavra da frase1, mostrando apenas algumas letras: {}'.format(dividido[2][3]))
