# -*- coding: utf-8 -*-
"""
Fixação de conteúdos.

Estrutura de dados: LISTAS

    Normalmente se diz que o conceito de LISTA é uma generalização das Pilhas e 
Filas. Entre Pilhas e Listas, a mudança significativa está na maneira ou na ordem
que os elementos são inseridos e acessados, retirados da estrutura (que também
são listas). 

# Pilhas: no caso das pilhas, os últimos elementos a entrarem na lista são os 
primeiros a saírem (LIFO - "Last Inside, First outside").

# Filas: já nas filas, analogamente a uma fila de caixa de banco ou num caixa de
supermercado, os primeiros elementos a entraram na fila serão também os primeiros
a saírem. (FIFO - "First Inside, First Outside")

    Na linguagem python, criar uma variável do tipo:
        l = [__,__,__,__]
        
        já é interpretado como um variável ou estrutura do tipo "list"

Funções normalmente usadas para manipular listas:
    append(), len(), pop(), top() ...
    
Em determinadas situações, aplicações, podem ser necessárias algumas alterações 
específicas nas listas, como armazenar os elementos de maneira que eles fiquem
ordenados segundo uma "lei de ordenação", e não ordenados pela ordem que foram 
inseridos. 
    Existem 4 maneiras de implementar listas:
        >> Sequencial x Encadeada;
        >> Estática ou Dinâmica.

1. Sequencial: os elementos são inseridos numa "sequencia física" na memória, 
permitindo acesso aos mesmos por meio de índices.
Permite acesso direto aos elementos, mas pode prejudicar o uso da memória.

    As listas podem variar segundo outros aspectos:
        * Ordenada vs. não ordenada: por exemplo através da fç sort() - ordena os elementos.
        * linear vs. não-linear: árvores binárias (grafos)
        * Homogênea vs. heterogêneas: armazena dados c/ elementos de != tipos (float, integer, str)

ex.: l[1] >> acessa o 2.º elemento da lista


2. Encadeada: os elementos são alocados na memória segundo uma sequencia lógica
Usa-se um ponteiro ( --> ) para o primeiro elemnto e cada elemento possue um ponteiro
para o próximo elemento (grafos?)

Otimiza a alocação de memória mas perde-se acesso direto aos elementos intermediários


3. Alocação estática: TODA MEMÓRIA é alocada, MESMO SEM SER UTILIZADA;
MAIS SIMPLES. 


4. Alocação dinâmica: a memória é alocada À MEDIDA QUE FOR UTILIZADA.
Usada quando NÃO SABEMOS QTOS ELEMENTOS SERÃO ARMAZENADOS
PYTHON USA ESTA ABORDAGEM. 


@author: antonio_andrade
"""

