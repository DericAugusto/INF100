# Nome do aluno: Déric Augusto França de Sales
# Matrícula: ES96718
# Data: 29/03/2018
#  Este programa calcula o dia em que será domindo de páscoa em determinado ano que esteja entre 1582 a 2499.
#  Se o ano digitado estiver fora desse intervalo, um aviso é mostrado na tela.

while 1:

    ano = int(input('Digite um ano (1082 a 2499): '))

    if 1582<= ano <=1699:
        x=22
        y=2
    elif ano <=1799:
        x=23
        y=3
    elif ano <=1899:
        x=23
        y=4
    elif ano <=2099:
        x=24
        y=5
    elif ano <=2199:
        x=24
        y=6
    elif ano <=2299:
        x=25
        y=0
    elif ano <=2399:
        x=26
        y=1
    elif ano <=2499:
        x=2
        y=1
    else:
        x=y=0
        

    a= ano % 19
    b= ano % 4
    c= ano % 7
    d= ((19*a) + x) % 30
    e= (2*b+4*c+6*d+y) %7
    p=(22+d+e)

    print(p)
