#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL
#DE ACORDO COM A MÉDIA ATINGIDA
#- MEDIA ABAIXO DE 5.0: 'REPROVADO'
#- MEDIA ENTRE 5.0 E 6.9: 'RECUPERACAO'
#- MEDIA 7.0 OU SUPERIOR: 'APROVADO'

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = ((n1 + n2)/2)
print('Sua média foi: {}'.format(media))
if media < 5.0:
    print('Sua nota final foi muito abaixo da média, você foi REPROVADO!\n'
          'Estude mais na próxima!')
elif 5.0 < media < 6.9:
    print('Sua nota foi abaixo da média.\n'
          'Precisará fazer RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')

