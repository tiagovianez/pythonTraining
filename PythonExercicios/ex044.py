#ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU "PREÇO NORMAL" E
#A "CONDIÇÃO DE PAGAMENTO":
#- À VISTA "DINHEIRO/CHEQUE": 10% DE DESCONTO - 1
#- À VISTA NO "CARTÃO": 5% DE DESCONTO - 2
#- EM ATÉ "2X NO CARTÃO": PREÇO NORMAL - 3
#- "3X OU MAIS" NO CARTÃO: 20% DE JUROS - 4
p = float(input('Qual o preço do produto? '))
c = float(input('Escolha uma opção (número) referente a sua condição de pagamento\n'
                '1 - À VISTA "DINHEIRO/CHEQUE": 10% DE DESCONTO\n'
                '2 - À VISTA NO "CARTÃO": 5% DE DESCONTO\n'
                '3 - EM ATÉ "2X NO CARTÃO": PREÇO NORMAL\n'
                '4 - 3X OU MAIS" NO CARTÃO: 20% DE JUROS\n'
                ': '))
if c == 1:
    np = (p * 0.9)
    print('O valor desse produto com desconto de 10% ficará: R$ {:.2f}'.format(np))
elif c == 2:
    np = (p * 0.95)
    print('O valor desse produto com desconto de 5% ficará: R$ {:.2f}'.format(np))
elif c == 3:
    print('Divido em 2x, o valor do produto será o mesmo: R$ {:.2f}'.format(p))
else:
    np = ((p * 0.2)+p)
    print('Divido em 3x ou mais, o valor total do produto será: R$ {:.2f}'.format(np))
