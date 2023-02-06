# Nome do aluno: Déric Augusto França de Sales
# Matrícula: ES96718
# Data: 14/04/2018

# Este programa calcula o MDC (Máximo Divisor Comum) para distintos pares de números naturais. Para cada par de números
# lido, o programa mostra o MDC e pede que o usuário entre com um novo par de números. O programa
# termina quando o valor 0 (zero) é digitado para o primeiro número. Cada vez que o número digitado
# é negativo (ou zero para o segundo número), o programa solicita que o número seja digitado novamente.

i = 0
n1= -1
n2= -1
while i==0:
    print('Cálculo do MDC de dois números')
    while n1<0:
        n1 = int(input('Digite o primeiro número natural (0 para sair):'))

    if n1==0:
        break

    else:

        while n2<=0:
            n2 = int(input('Digite o segundo número natural:'))
        
        
        
        if n1 == n2:
            print('O máximo divisor comum é %d' %n1)
            print ()
            n1= -1
            n2= -1
            
        else:
            while n1 !=n2:
                while n1 > n2:
                    n1= n1 - n2
                while n1 < n2:
                    n2= n2 - n1
            print ('O máximo divisor comum é %d' %n1)
            print ()
            n1= -1
            n2= -1
           
    
