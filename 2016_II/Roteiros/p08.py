import random

print("Jogo 'Adivinhe meu Número'\n")

limite_superior = int( input('Entre com o limite superior para o sorteio (> 0): '))
while limite_superior <= 0:
    limite_superior = int( input('Entre com o limite superior para o sorteio (> 0): '))

# iniciar gerador de números aleatórios para que a sequência fique
# diferente cada vez que o programa é executado.
random.seed()
# gerar valor aleatório n entre 0 e limite_superior
n = random.randint( 0, limite_superior )

print('Acabei de sortear um número entre 0 e %d.Tente adivinha-lo:' % limite_superior )

tentativas = 0
chute = -1
while chute != n:
    chute = int( input('\n--> '))
    tentativas = tentativas + 1
    if n > chute:
        print('Maior que ', chute, '.', sep='')
    elif n < chute:
        print('Menor que ', chute, '.', sep='')

print('Você acertou em', tentativas, 'tentativa(s)!\n')
