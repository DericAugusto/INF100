# Déric Augusto França de Sales
#ES96718
#08/05/2018
# O programa lê o número de alunos, a nota de cada aluno e escreve na tela uma tabela mostrando o número do 
#  aluno, a nota original, e a nota normalizada. 
#   A nota normalizada corresponde à nota do aluno multiplicada a uma rasão de 100 dividido pela maior nota entre os alunos.

import numpy as np

while 1:
    a = int(input('Qual o tamanho da sua turma? '))
    if a>0:
        break

v = np.empty(a)

maior=0

for i in range (0,a):
    z = float(input('Informe a nota do aluno %d (0..250): '%(i+1)))
    while z<0 or z>250:
        print ('Valor incorreto')
        z = float(input('Informe a nota do aluno %d (0..250): '%(i+1)))
    v[i] = z
    if z > maior:
        maior = z

f = 100/ maior

print('\nAluno   Nota Original   Nota Normalizada')

for i in range (0,a):
    print('%3d   %10.1f    %15.1f' %(i+1,v[i],v[i]*f))
