# Déric Augusto França de Sales
#ES96718
#15/05/2018
#  O programa lê uma quantidade n de valores inteiros para dentro de um arranjo.
# Em seguida, o programa analisa os elementos inseridos dentro desse arranjo,
# observando se são pares ou ímpares. Enquanto o programa analisa os elementos 
# que estão dentro do arranjo, ele cria novos arranjos, um para os números pares 
# e outro para os números ímpares. No final, o programa printa os valores pares 
# e ímpares que foram inseridos no primeiro arranjo, através dos dois novos
# arranjos preenchidos.

import numpy as np
n=0
I=[]
P=[]

while n<=0:
    n=int(input('Entre com o valor de n: '))

print('Digite cada valor inteiro em uma linha:')

A=np.zeros(n)

for i in range (0,len(A)):
    A[i]= int(input(''))

for i in range (0,len(A)):
    if (A[i] %2==0): 
        P.append(A[i])
        
    else:
        I.append(A[i])
        
print('')

print('Valores ímpares: ',end=(''))

for i in range (0,len(I)):
    print('%d'%I[i],end=(' '))
    
print('\nValores pares:   ',end=(''))

for i in range (0,len(P)):
    print('%d'%P[i],end=(' '))
        
    
    
