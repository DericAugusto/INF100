n = int( input('Digite o número de capivaras adultas que terão seus pesos medidos: ')) 
i = soma = 0

maior = 0
menor = 1000
while i < n:
    while True:
        peso = float (input('Digite um peso (kg): '))
        if peso < 30 or peso > 100:
            print('Peso inválido!')
        else: break
    soma = soma + peso
    if peso > maior: maior = peso
    if peso < menor: menor = peso
    i = i + 1

if n > 0:
    print('\nPeso médio: %.1f kg' % (soma/n))
    print('Menor peso:', menor, 'kg')
    print('Maior peso:', maior, 'kg')
