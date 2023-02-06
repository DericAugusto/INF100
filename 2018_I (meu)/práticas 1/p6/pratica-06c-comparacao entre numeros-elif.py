# Déric Augusto França de Sales
#ES96718
#10/04/2018
#Este programa lê três números inteiros e mostra na tela uma mensagem indicando qual é o menor,
#qual é o maior, e se existem dois números iguais, três números iguais, ou se os três são distintos.

print('Entre com três números inteiros quaisquer:')
n1 = int (input())
n2 = int (input())
n3 = int (input())


if n1<n2 and n1<n3 and n2<n3:
    print('Menor valor: %d'%n1)
    print('Maior valor: %d'%n3)
    print('Os números são todos distintos')
elif n1<n2 and n1<n3 and n3<n2:
    print('Menor valor: %d'%n1)
    print('Maior valor: %d'%n2)
    print('Os números são todos distintos')
elif n2<n1 and n2<n3 and n1<n3:
    print('Menor valor: %d'%n2)
    print('Maior valor: %d'%n3)
    print('Os números são todos distintos')
elif n2<n1 and n2<n3 and n3<n2:
    print('Menor valor: %d'%n2)
    print('Maior valor: %d'%n2)
    print('Os números são todos distintos')
elif n3<n1 and n3<n2 and n2<n1:
    print('Menor valor: %d'%n3)
    print('Maior valor: %d'%n1)
    print('Os números são todos distintos')
elif n3<n1 and n3<n2 and n1<n2:
    print('Menor valor: %d'%n3)
    print('Maior valor: %d'%n2)
    print('Os números são todos distintos')

elif n1==n2==n3:
    print('Menor valor: %d'%n1)
    print('Maior valor: %d'%n1)
    print('Os três números são idênticos')
    
elif n1==n2:
    if n1<n3:
        print('Menor valor: %d'%n1)
        print('Maior valor: %d'%n3)
        print('Existem dois números idênticos')
    elif n3<n1:
        print('Menor valor: %d'%n3)
        print('Maior valor: %d'%n1)
        print('Existem dois números idênticos')

elif n1==n3:
    if n1<n2:
        print('Menor valor: %d'%n1)
        print('Maior valor: %d'%n2)
        print('Existem dois números idênticos')
    elif n2<n1:
        print('Menor valor: %d'%n2)
        print('Maior valor: %d'%n1)
        print('Existem dois números idênticos')

elif n2==n3:
    if n1<n3:
        print('Menor valor: %d'%n1)
        print('Maior valor: %d'%n3)
        print('Existem dois números idênticos')
    elif n3<n1:
        print('Menor valor: %d'%n3)
        print('Maior valor: %d'%n1)
        print('Existem dois números idênticos')






    
