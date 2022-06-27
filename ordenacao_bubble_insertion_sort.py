# -*- coding: utf-8 -*-
"""
                    ## Algoritmos de ORDENAÇÃO. ##
                    
    Organizar uma sequencia de elementos, de modo que se estabeleça uma relação
de ordem entre os elementos. 

ex.: diz-se que os elementos K1,K2,K3,K4,...,Kn estarão dispostos de modo que 

k1 <= k2 <= k3,..., <= kn (neste caso estão ordenados de maneira crescente)

        1. Algoritmo BUBBLE SORT
        
        Um dos métodos mais conhecidos e intuitivos. 
        Percorre-se o conjunto de elementos várias vezes. 
        A cd iteração, comparar cd elemento com o seu sucessor (v[i], com v[i+1]). 
Se a ordem estiver incorreta, trocá-los de lugar).

suponha o seguinte vetor:
    
v = (16,25,88,56,79,33)

    (16,25,88 *troca posição 56,79,33) >>  (16,25,56,88,79,33)
    (16,25,56,88 *troca posição 79,33) >>  (16,25,56,79,88,33)
    (16,25,56,79,88 *troca posição 33) >>  (16,25,56,79,33,88)  passo 1
    
    (16,25,56,79 *troca posição 33,88) >>  (16,25,56,33,79,88) passo 2
    
    (16,25,56 *troca posição 33,79,88) >>  (16,25,33,56,79,88) passo 3

para um vetor de n elementos, são necessárias (n - 1) iterações
neste exemplo, 6 elementos resultou em 5 iterações.

@author: andra
"""

# Implementação do algoritmo de ordenação BUBBLE SORT

def bubble_sort(v):
    for i in range(len(v) - 1):
        for j in range(len(v)-i-1):
            if(v[j] > v[j+1]):
                v[j],v[j+1] = v[j+1], v[j]


p =  [16,25,88,56,79,33]

bubble_sort(p)

print(p)
# [16, 25, 33, 56, 79, 88]


q = [45,534,63,669,88,98,774,255,999,966541,2,88896332,1115587,221,22,
     556547,8855221,12,25,47,896,212,5554,85521,5632,5]

bubble_sort(q)

q

q

# Out[20]: 
# [2,
#  5,
#  12,
#  22,
#  25,
#  45,
#  47,
#  63,
#  88,
#  98,
#  212,
#  221,
#  255,
#  534,
#  669,
#  774,
#  896,
#  999,
#  5554,
#  5632,
#  85521,
#  556547,
#  966541,
#  1115587,
#  8855221,
#  88896332]

# INSERTION SORT

def insertion_sort(v):
    for i in range(len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j-= 1
        v[j+1] = x

# x = [44,55,12,42,94,18,6,67]
# insertion_sort(x)
# x

