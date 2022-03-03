#DESENVOLVA UM PROGRAMA QUE LEIA O 'NOME', 'IDADE', E O 'SEXO' DE '4 PESSOAS'. NO FINAL DO PROGRAMA, MOSTRE:
# > A 'MEDIA DE IDADE' DO GRUPO
# > QUAL É O NOME DO HOMEM 'MAIS VELHO'
# > QUANTAS MULHERES TÊM 'MENOS DE 20' ANOS
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher20 = 0
for d in range(1, 5):
    print('==== {}ª PESSOA ===='.format(d))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if d == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Fm' and idade < 20:
        tot_mulher20 += 1
media_idade = (soma_idade / 4)
print('A média da idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(tot_mulher20))
