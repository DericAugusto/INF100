import turtle as Tut
import fechadura

while True:
    matricula = int( input("Digite o número de sua matrícula (1 a 9999999): "))
    if 1 <= matricula <= 9999999:
        break

fechadura.contorno( Tut, matricula )

# Escreva seu código abaixo desta linha

while matricula > 0:
    d = matricula % 10
    matricula = matricula // 10
    Tut.forward( 40 )
    if d % 2 == 0:
        Tut.right( 90 )
        Tut.forward( d*10 )
        Tut.backward( d*10 )
        Tut.left( 90 )
    else:
        Tut.left( 90 )
        Tut.forward( d*10 )
        Tut.backward( d*10 )
        Tut.right( 90 )

# A linha a seguir deve ser a última do programa. Favor não alterá-la
Tut.Screen().exitonclick()
