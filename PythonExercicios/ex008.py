#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite uma distância em metros: '))
cm = 100 * m
mm = 1000 * m
print('O valor é equivalente a {}cm\nE em milimetros o valor é equivalente a {}mm'.format(cm, mm))