#REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
#- EQUILÁTERO: TODOS OS LADOS IGUAIS
#- ISÓSCELES: DOIS LADOS IGUAIS
#- ESCALENO: TODOS OS LADOS DIFERENTES
s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Podemos formar um triângulo! ')
    if s1 == s2 == s3:
        print('E o triângulo formado é um EQUILÁTERO!\n'
              'Pois possui todos os lados iguais.')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('O trângulo formado é um ISÓSCELES!\n'
              'Pois possui dois lados iguais.')
    else:
        print('O triângulo formado é um ESCALENO!\n'
              'Pois as medidas dos seus lados são todas DIFERENTES.')
else:
    print('Não podemos formar um triângulo!')
