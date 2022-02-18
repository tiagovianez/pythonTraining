#FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA 'CONTAGEM REGRESSIVA' PARA ESTOURO DE FOGOS DE ARTIFÍCIO, INDO DE
#10 ATÉ 0, COM UMA PAUSA DE '1 SEGUNDO' ENTRE ELES.
import time
from time import sleep
print('=-'*20)
print('PREPARADOS PARA A QUEIMA DE FOGOS DE ARTIFÍCIO?')
print('=-'*20)
print('A queima de fogos inicia em...')
for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
print('BOOOOMMM!')