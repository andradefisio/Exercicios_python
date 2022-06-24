# -*- coding: utf-8 -*-
"""
Tema: Conceito de Filas

Definição: 
    A fila é uma estrutura para armazenar dados que funciona da seguinte forma:
        # Novos elementos sempre entram no fim da fila;
        # O único elemento que pode ser retirado da fila é o primeiro elemento. 

Para que serve?
Armazenar um CONJUNTO ORDENADO de elementos, no qual o primeiro a entrar tb
será o primeiro a sair. 

@author: andrade
"""

class Fila():
    def __init__(self):
        self.data = []
        
    def inserir(self,x):
        self.data.append(x)
    
    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)
    
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):
        return not len(self.data) > 0
    
    def __repr__(self):
        return str(self.data)
    
f =  Fila()
f    

f.inserir(5)     
f.inserir(10) 
f.inserir(15) 
f.inserir(20)        
        
f.empty()        
f.top()        
f.remover()
f.remover()

f
