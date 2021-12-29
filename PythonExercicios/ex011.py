#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
ql = (area / 2)
print('Sua parede tem a dimensão de {}x{}\n'
      'Sua área é de {:.2f}m²\n'
      'A quantidade de tinta a ser utilizada é {:.2f} litros\n'.format(l, a, area, ql))