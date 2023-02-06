# Nome do aluno: Déric Augusto França de Sales
# Matrícula: ES96718
# Data: 29/03/2018
#  Este programa faz a média de 4 pesos.
#  Se um dos pesos digitados não correnponder à condição a ser atendida,
#se não for maior que 0, esse peso será desconsiderado na média e um aviso de 'peso inválido' será exibido na tela

while 1:
    soma=0
    n=0

    c1=float(input('Peso da Capivara 1: '))
    if c1>0:
        soma= soma + c1
        n+=1 #n=n+1
    else:
        print('Peso Inválido!')
        
    c2=float(input('Peso da Capivara 2: '))
    if c2>0:
        soma=soma + c2
        n+=1
    else:
        print('Peso Inválido!')
        
    c3=float(input('Peso da Capivara 3: '))
    if c3>0:
        soma=soma + c3
        n+=1
    else:
        print('Peso Inválido!')
        
        
    c4=float(input('Peso da Capivara 4: '))
    if c4>0:
        soma=soma + c4
        n+=1
    else:
        print('Peso Inválido!')

    print()

    if n==0:
        print('Nenhum peso válido fornecido')
    else:
        print(' (considerando %d pesos válidos)'% n)
        media= soma/n
        print('Peso médio: %4.1f kg\n'% media)











    
