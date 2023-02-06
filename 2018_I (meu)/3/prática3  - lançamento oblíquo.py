# Nome do aluno: Déric Augusto França de Sales
# Matrícula: ES96718
# Data: 29/03/2018
# Este programa faz o cálculo do alcance e altura máxima de um projeto em lançamento oblíquo
# Ele também premedita o alcance e altura máxima a 45º e 90º repectivamente


import math
g = 9.80665

print('Cálculo de Lançamento de Projétil')
print('---------------------------------')
print()

v0=int(input('Entre com o valor de v0 (km/h):')) #integer = inteiro
teta=int(input('Entre com o valor de teta (graus):'))

tetarad = math.radians(teta)
v0 = v0 / 3.6
xreal= ((v0**2)*(math.sin(2*tetarad)))/ g
yreal= ((v0)*(math.sin(tetarad)))/2*g

xmax= ((v0**2)*(math.sin(2*(math.radians(45)))))/ g
ymax= ((v0)*(math.sin((math.radians(90)))))/2*g
    
print('Alcance atingido = %d'%xreal)
print('Altura atingida = %d'%yreal)
print('Alcance máximo (considerando o lançamento a 45º) = %4.2f'%xmax)
print('Altura máxima (considerando o lançamento a 90º) = %4.2f'%ymax)
