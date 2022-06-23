# -*- coding: utf-8 -*-
"""
@author: andrade
"""

# A linguagem de programação python, assim como outras, como por exemplo a linguagem R,
# são ditas linguagens "orientadas à objetos". O que seria um objeto?

# Um objeto seria a formalização pela qual compreendemos algo no 
# escopo, no domínio de um problema, ou de uma situação, de um grupo de seres vivos ...
 
# Um objeto reflete a capacidade do sistema de **GUARDAR INFORMÇÕES** sobre um elemento 
# *ABSTRAÍDO*, **INTERAGIR** com este objeto, ou ambas. 

# Em ciência de dados, engenharia de computação, ...  muito se fala em "ABSTRAÇÃO". 
# O que seria abstração ou abstraído? 
# Conforme definição da wikipedia, a 'abstração' "é a habilidade de concentrar nos 
# aspectos essenciais de um contexto qualquer, ignorando característas menos 
# importantes ou acidentais" ( https://pt.wikipedia.org/wiki/Abstra%C3%A7%C3%A3o_(ci%C3%AAncia_da_computa%C3%A7%C3%A3o ).
# Em modelagem orientada a objetos, uma CLASSE seria a abstração de entidades no domínio 
# do sistema de software.

# Exemplos CLASSES no mundo real:
    # 1) Imaginem a abstração referente à classe ANIMAIS. Quando a palavra, a expressão animais 
    # nos é apresentada imprimimos um significado à ela, de maneira que logo nos remetemos a alguns seres
    # vivos que apresentam certas características que são esenciais, peculiares e fazem com que
    # nosso pensamento nos remeta à estes seres. Então, há várias entidades na classe de animais
    # que compões 'subclasses' da classe ANIMAIS, como Anfíbios, Répteis, Peixes e Mamíferos. 
    # Dentro destas subclasses existem os "seres humanos" (subclasse mamíferos), Lambari (subclasse peixes), 
    # que são instâncias ou OBJETOS da classe animais. 
    
    # 2) Imaginem a classe "VEÍCULOS". Quando nos deparamos com esta expressão,
    # sem mencionar qual veículo, a principal característica que pode nos vir à cabeça poderia ser 
    # a existência de um motor.  
    # Nosso cérebro pode nos remeter a um conjunto de entidades que usam motores p/ realização de deslocamentos.
    # A partir da 'raiz', do 'nó' "VEÍCULOS" 'derivamos' outras subclasses de entidades
    # como as subclasses das Motos, Carros, Caminhões, Tratores, Aviões... 
    
    # Ex.: o objeto carro seria um instância da classe VEÍCULOS. 
    # Os objetos apresentam certas características denominadas ATRIBUTOS (ex.: cor=prata; modelo=corsa; ano=2002; fabricante:chevrolet).
    # Além disso, podemos interagir com este objeto pois ele desempenha algumas funções, e possui MÉTODOS {acelerar(); frear(); virar()...}

# Na ciência de dados, normalmente as rotinas acontecem e se processam de maneira que armazenamos informações (inputs), processamos essa info 
# para então obtermos um resultado, desfecho ou outra informação derivada do processamento anterior (seria o output). 

# E como são armazenadas e processadas estas informações? As linguagens python e R são ferramentas que podem desempenhar esta tarefa (armazenar, processar e 
# emitir um resultado)

# Vamos pensar numa estrutura para armazenar um conjunto de elementos. Esses elemntos, valores são empilhados (conceito de "pilha")
#   * novos elementos sempre entram no topo da pilha
#   * o único elemento que se pode retirar da pilha em um dado momento é o elemento
#    do topo da pilha;

# Principais usos: modelagem de situações nas quais é necessário "guardar para mais tarde"
# varios elementos e lembrar sempre do último elemento armazenado. 

# Operações/métodos usuais:
    # - push(): "empilha em elemento na pilha"
    # - pop(): "desempilha o elemento no topo da pilha"
    # - top(): "acessa o elemento no topo da pilha, sem desempilhá-lo"
    # - empty(): " verifica se a pilha está vazia "
    
# ex.:

class Pilha():  # essa classe "estoca" um conjunto de elementos. 
    def __init__(self):  # "self" faz uma referencia ao pp objeto que será instanciado
        self.data = []
        
    def push(self, x):  # adiciona elementos na lista (na sequencia de inserção)
        self.data.append(x)
        
    def pop(self): # método que permite, se o comprimento da lista for > 0 (lista não vazia) "desempilhar" o último elemento inserido
        if len(self.data) > 0:
            return self.data.pop(-1)
    
    def top(self): # acessa o último elemento
        if len(self.data) > 0:
            return self.data.top[-1]
    
    def empty(self):
        return not len(self.data) > 0
    
    def get(self): # name_object.get()" retorna todos elementos da lista
        return self.data
    
    def __repr__(self): # para representar a lista. 
        return str(self.data)
        
objeto = Pilha()  #instanciado um objeto > "objeto"

objeto.push(2) # adicionando 2
objeto.push(4) # adicionando 4
objeto.push(6) # adicionando 6

objeto.get()
# Out[120]: [2, 4, 6]

objeto.pop()
# Out[121]: 6

objeto.empty()
# Out[122]: False    Existem elementos em objeto 


# Ex.1:
    
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def minhaFuncao(x):
        print('Olá, meu nome é ' + x.nome)

pessoa1 = Pessoa('Antonio', 46)
pessoa1.minhaFuncao()
# Olá, meu nome é Antonio

















    
    
    
    
    
    
    
    
    
    
    
