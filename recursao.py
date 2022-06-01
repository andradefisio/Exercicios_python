# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:01:31 2022

@author: andra
"""

# Recursão

# Uma função é dita recursiva quando é definida em seus próprios termos, direta ou
# indiretamente. Por exemplo, podemos modificar a função abaixo, que imprime 
# os elementos de uma lista,
# para que seja recursiva:
    
def imprime(l):
    for i in range(len(l)):
        print(l[i])

l = ['joão', 'marcelo', 'laura', 'pedro']

imprime(l)

# transformando a fç "imprime" em recursiva

def imprime_recurs(l, i=0):
    if i<len(l):
        print(l[i])
        imprime_recurs(l,i+1)

L2 = ['cachorro', 'gato', 'pássaro', 'girafa']
imprime_recurs(L2)

# Como usar?

# Exemplo: problema do fatoria:
    
# 1) Definir o problema de forma recursiva, ou
# seja, em termos dele mesmo
# • n! = n * (n – 1)!

# 2) Definir a condição de término (ou condição
# básica)
# • n = 0

# 3) A cada chamada recursiva, deve-se tentar
# garantir que se está mais próximo de
# satisfazer a condição de término
# • A cada chamada, n é decrementado

# Defina uma função recursiva para calcular o fatorial de um número:
    
def fat(n):
    if n == 0:
        return 1
    else:
        resultado = n * fat(n-1)
        return resultado
fat(3)
fat(2)
# Out[11]: 2

fat(3)
# Out[12]: 6

fat(5)
# Out[13]: 120


def f1(n): 
    if n >= 1: 
        return 1 
    else: 
        return n * f1(n - 1) 
 
print(f1(4)) 

'''
Exercício
Implementar uma função recursiva para calcular o n-ésimo termo da sequência de
Fibonacci.
Considere os três pontos definidos para o problema: 
    
1) f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2) p/ n>=2
    
2) n=0 ou n=1
    
3) n deve ser decrementado a cada chamada
'''
def fibonacci_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        resultado = fibonacci(n-1) + fibonacci(n-2)
        return resultado
    
fibonacci_rec(5)  
#Out[23]: 5  
  
fibonacci_rec(6) 
#Out[24]: 8

# Calculo da sequencia de fibonacci pela iteração:
    
def fibonacci_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n + 1):
        res = a + b
        a, b = b, res
    return res

# Há uma diferença calculando o valor de fibonacci na sequência usando o método
# recursivo e pelo método iterativo



# Definição da fç Fibonacci com "Memoização":
    
m = dict()
def fibonacci_memoizacao(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fibonacci_memoizacao(n - 1) + fibonacci_memoizacao(n - 2)
        return m[n]


# Calculando o tempo de processamento
import time

n = 35
start = time.time()

print(fibonacci_rec(n))
print('Recursive: {} seconds'.format(time.time() - start))
# 9227465
# Recursive: 3.5555269718170166 seconds

start = time.time()
print(fibonacci_it(n))
print('Iterative: {} seconds'.format(time.time() - start))
# 9227465
# Iterative: 0.0 seconds

start = time.time()
print(fibonacci_memoizacao(n))
print('Memoization: {} seconds'.format(time.time() - start))
# 9227465
# Memoization: 0.0 seconds





## =========================================================================##

# Recursão II
