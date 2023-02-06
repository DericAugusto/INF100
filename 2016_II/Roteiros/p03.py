soma = 0  # essa variável armazenará a soma dos pesos válidos lidos
n = 0  # essa variável armazenará a quantidade de pesos válidos lidos

peso = float (input('Peso da capivara 1: '))
if peso > 0:
    soma = soma + peso
    n = n + 1
else:
    print('Peso inválido!')

peso = float (input('Peso da capivara 2: '))
if peso > 0:
    soma = soma + peso
    n = n + 1
else:
    print('Peso inválido!')

peso = float (input('Peso da capivara 3: '))
if peso > 0:
    soma = soma + peso
    n = n + 1
else:
    print('Peso inválido!')

peso = float (input('Peso da capivara 4: '))
if peso > 0:
    soma = soma + peso
    n = n + 1
else:
    print('Peso inválido!')

if n == 0:
    print("\nNenhum peso válido fornecido.")
else:
    print("\nPeso médio: %5.1f kg\n(considerando %d pesos válidos)" % (soma/n, n))
   
