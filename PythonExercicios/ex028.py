# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUÁRIO TENTAR
# DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU

n = int(input('Adivinhe qual foi o número pensando pelo computador de 0 a 5: '))
if n == 4:
    print('Parabéns, Você venceu!')
elif n > 5:
    print('Valor inválido, tente novamente!')
else:
    print('Infelizmente não foi dessa vez, você perdeu!')