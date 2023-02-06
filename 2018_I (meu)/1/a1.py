# Nome do aluno: Júlia Stefani Thomazini Pizzol
# Matrícula: 96718
# Data: 06/03/2018
# O programa faz a tartaruga se mover até o seu alimento.

import turtle as Tut
import p01_maze as m

matricula = 96718  # Coloque aqui (novamente) seu número de matrícula

m.build_maze( Tut, matricula )

# Adicione seu código abaixo desta linha
Tut.right(90)
Tut.fd(50)
Tut.left(90)
Tut.fd(100)
Tut.right(90)
Tut.fd(150)
Tut.right(90)
Tut.fd(100)
Tut.left(90)
Tut.fd(200)
Tut.left(90)
Tut.fd(200)
Tut.left(90)
Tut.fd(150)
Tut.right(90)
Tut.fd(100)
Tut.right(90)
Tut.fd(100)
Tut.left(90)
Tut.fd(150)
Tut.right(90)
Tut.fd(100)


# Seu código não deve passar desta linha

Tut.Screen().exitonclick()
