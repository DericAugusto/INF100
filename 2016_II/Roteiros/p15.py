from ilha import Ilha
import numpy as np

"""
Ilha:
exibe( pausa ) -> exibe a ilha, pausando um certo número de segundos
getAltitudes() -> retorna a matriz de altitudes da ilha
setAltitudes( matriz ) -> redefine a matriz de altitudes da ilha, passando "matriz" como parametro
"""

def reduzMatriz( M, a ):
    linhas, colunas = M.shape
    maior = 0
    for i in range(0, linhas):
        for j in range(0, colunas):
            M[i][j] = max( 0, M[i][j] - a )
            maior = max( maior, M[i][j] )
    return maior
    
def reduzMatriz2( M, a ):
    M -= a
    M[ M < 0 ] = 0
    return np.max( M )
    
il = Ilha()

il.exibe( 1 )

matriz = il.getAltitudes()

while True:
    maior = reduzMatriz( matriz, 1 )
    if maior == 0: break
    il.setAltitudes( matriz )
    il.exibe( 1 )
        
''' Perguntas e respostas da Parte 3:

Pergunta 1:
Ao alterar o tempo de espera para um tempo desprezível, você notou
alguma alteração significativa no tempo de execução do programa usando
a função reduzMatriz() ou a função reduzMatriz2()?

Resposta 1:
Não. O tempo permaneceu praticamente o mesmo, independente da função usada.

Pergunta 2:
Baseado na Resposta 1 acima, na sua opinião, onde reside a maior carga
de processamento do programa? Na redução da matriz ou na exibição da
imagem? Justifique.

Resposta 2:
Observamos que, mesmo usando a função reduzMatriz2(), que parece ser BEM
eficiente, e com um tempo de espera de 0,01s, ainda assim a troca das
imagens leva um tempo considerável. Isso nos leva a crer que a exibição da
imagem em si é que possui a maior carga de processamento.

'''
