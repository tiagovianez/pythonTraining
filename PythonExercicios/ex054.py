#CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO
#ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
count_majority = 0
count_minority = 0
import datetime
date = datetime.date.today()
yn = int(date.strftime('%Y'))
for c in range(1, 8):
    an = int(input('Ano de nascimento da {}º pessoa: '.format(c)))
    age = int(yn - an)
    if age >= 21:
        count_majority += 1
    else:
        count_minority += 1
print('Ao todo tivemos {} pessoas maiores de idade\n'
      'E também tivemos {} pessoas menores de idade'.format(count_majority, count_minority))

