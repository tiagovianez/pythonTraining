d = int(input('Quantos dias alugados? '))
km = float(input('Quantos KMs rodados? '))
cd = 60
kmr = 0.15
aluguel = (cd * d) + (kmr * km)
print('O custo total a pagar é de R${:.2f}'.format(aluguel))
