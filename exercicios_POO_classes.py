# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:17:09 2022

@author: andra
"""


# SEMANA 02
# 
# PROGRAMAÇÃO ORIENTADA A OBJETO (POO)

# Exercícios do livro "Pense Python", disponivel em https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html?highlight=chamar 

# 1) Escreva uma função distancia que recebe dois Point s como parâmetros e retorna a distância euclidiana entre eles.
import math # para usar a fç sqrt (raiz quadrada)

class Point:
    
    def __init__(self, initX, initY):
        
        self.x = initX
        self.y = initY
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def reflect_x(self):
        return ((self.x),(self.y) * (-1))
    
    def slope_from_origin(self):
        return((self.y)/(self.x))
    
    def get_line_to(p1,p2):
        yDif_p1 = p2.getY() - p1.getY()
        xDif_p2 = p2.getX() - p1.getX()
        
        a = (yDif_p1)/(xDif_p2)
        b = p2.getY()- (p2.getX()*a)
        
        return (a,b)
    

def distancia(ponto1,ponto2):
    xdif = ponto2.getX() - ponto1.getX()
    ydif = ponto2.getY() - ponto1.getY()
    
    dist = math.sqrt(xdif**2 + ydif**2)
    return dist
    
p = Point(7,6)
q = Point(3,4)
print(distancia(p,q))        



# 2) Crie um método reflect_x na classe Point que retorna um novo Point, que é a reflexão do ponto no eixo x. Por exemplo, Point(3, 5).reflect_x() é (3, -5)

# ver linhas 31,32
a = Point(3,5)
b = Point(-3,-4)

print(a.reflect_x())
print(b.reflect_x())



# 3) Crie um método slope_from_origin que retorna a inclinação da linha que liga o ponto à origem.
    
    def slope_from_origin(self):
        return((self.y)/(self.x))
 

# Por exemplo,
# >>> Point(4, 10).slope_from_origin()
# 2.5

Point(10, 800).slope_from_origin()

# Quais os casos onde esse método falha? Resposta: qdo y = 0
Point(-4,-10).slope_from_origin()
Point(4,-10).slope_from_origin()
Point(-4,10).slope_from_origin()
Point(0,0).slope_from_origin() # neste ponto ocorre uma falha ou 
Point(0,5).slope_from_origin() # neste ponto ocorre uma falha  
Point(4,4).slope_from_origin()




# 4) A equação de uma reta é “y = ax + b”, (ou talvez “y = mx + c”). Os coeficientes a e b são suficientes para descrever a linha.
# Escreva um método na classe Point que recebe outra instância de Point e calcula a equação da reta que liga os dois pontos.
# O método deve retornar os dois coeficientes na forma de um tuple com dois valores. 

# Por exemplo,
# >>> print(Point(4, 11).get_line_to(Point(6, 15)))
# >>> (2, 3)
# Isso nos diz que a equação da linha que liga os dois pontos é “y = 2x + 3”. Quais os casos onde esse método falha?

# É sabido que, SE o gráfico de uma função é uma reta, ENTÃO a função é do primeiro grau. Pela função dada “y = ax + b”,
# temos que o "a" seria o coeficiente angular desta reta, e o "b" o ponto no qual a reta toca o eixo das ordenadas ou Y, qdo x = 0. 
#     def get_line_to(p1,p2):
#         yDif_p1 = p2.getY() - p1.getY()
#         xDif_p2 = p2.getX() - p1.getX()
        
#         a = (yDif_p1)/(xDif_p2)
#         b = p2.getY()- (p2.getX()*a)
        
#         return (a,b)
# # Teste:
# Resposta
# In [21]:print(Point(4,11).get_line_to(Point(6, 15)))
# (2.0, 3.0)




# 5) Dados quatro pontos sobre uma circunferência, encontre o ponto centro da circunferência. Quando a sua função falha?

# Dica: Você deve saber como resolver o problema geometricamente antes de fazer qualquer coisa relacionada a programação.
# Você não pode programar uma solução para um problema se você não entende o que você quer que o computador faça.

