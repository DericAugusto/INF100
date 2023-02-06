# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o que o programa faz)

import math
import projetil

g = 9.80665

v0 = float (input("Entre com o valor de v0 (km/h): "))
teta = float (input("Entre com o valor de teta (graus): "))

v0 = v0 / 3.6
teta = math.radians( teta )
x_max = v0 ** 2 * math.sin( 2 * teta ) / g
y_max = (v0 * math.sin( teta )) ** 2 / (2 * g)

print('Alcance máximo = %.3f metros' % x_max )
print('Altura máxima = %.3f metros' % y_max )

projetil.grafico_projetil( v0, teta, x_max, y_max )
