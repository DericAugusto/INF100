import numpy as np

while True:
    n = int(input('Qual o tamanho da turma? '))
    if n > 0: break

notas = np.empty(n)

maior = 0
for i in range(0,n):
    while True:
        notas[i] = float(input('Informe a nota do aluno %d (0..250): ' % (i+1)))
        if notas[i] < 0 or notas[i] > 250:
            print('Valor incorreto.')
        else: break
    if notas[i] > maior:
        maior = notas[i]

fator = 100 / maior

print('\nAluno   Nota Original    Nota Normalizada')
for i in range(0,n):
    print('%3d%13.1f%20.1f' % (i+1, notas[i], notas[i]*fator))

