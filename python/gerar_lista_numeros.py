import numpy as np

x =list(np.random.randint(low=1,high=500000,size=99999999))

#Complexidade Constante O(k) Constant Time
def constante(x:list) -> list:
    return x

constante(x)

#Complexidade O(n) Linear Time
def iterador_normal(x:list) -> list:
    contador = len(x)
    while(contador > 0):
     contador -= 1
    return x
iterador_normal(x)

#Complexidade O(n2) Quadratic Time
def iterador_anidado(x:list) -> list:
    contador_externo = len(x)//1000
    contador_interno = len(x)//1000

    while(contador_externo > 0):
        contador_externo -= 1
        for i in range(contador_interno): 
            i
    return x
iterador_anidado(x)


#Complexidade O(log(n))Logarithmic Time
def iterador_multiplicado(x:list) -> list:
    iterador = len(x)
    incremento = 1
    while(iterador > 0):
        iterador -= incremento
        incremento *= (incremento + 1)
    return x
iterador_multiplicado(x)

#Complexidade O(log(n)) Logarithmic Time
def iterador_dividido(x:list) ->list:
    iterador = -len(x)
    incremento = 1
    while(iterador < 0):
        iterador /= incremento
        incremento += 1
    return x
iterador_dividido(x)

#Complexidade O(log(log(n))) Logarithmic from Logarithmic Time
import math
def iterador_incremento_exponencial(x:list) -> list:
    iterador = len(x)
    incremento = 1
    while(iterador > 0):
        iterador -= pow(incremento, 2)
        incremento += 1
    return x
iterador_incremento_exponencial(x)

#Cálculo da Complexidade Algorítmica do Exemplo
y =list(np.random.randint(low=1,high=500000,size=999))

def calculo_bit_o_ejemplo(y:list) ->str:
    iterador = -len(y) # k
    incremento = 1 # k
    q_list = y # k
    while(iterador < 0): # log(n)
        iterador /= incremento # k
        incremento += 1 # k
    for p in y: # n
        for q in y: # n -> n * n
            for r in y: # n -> n * n * n
                r
    return "La Complejidad es n*n*n, n cubo"
calculo_bit_o_ejemplo(y)