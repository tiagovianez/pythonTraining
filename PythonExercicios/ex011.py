#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
l = int(input('Digite a largura: '))
a = int(input('Digite sua altura: '))
area = l * a
ql = 2 * area
print('A área da parede é: {}m²\n'
      'A quantidade de tinta utilizada foi: {} litros\n'.format(area, ql))