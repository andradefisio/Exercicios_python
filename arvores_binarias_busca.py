# -*- coding: utf-8 -*-
"""
Estrutura de dados: ÁRVORES

    Algumas aplicações necessitam de uma modelagem mais complexa, necessitando para isso de
estruturas de dados também mais complexas que as listas lineares.
Estas estruturas que apresentam uma complexidade maior (não lineares)  são denominadas de
árvores, grafos, etc...

    Motivação para usos destas estruturas:
        Problemas que podem ser tratados modelando-os através de árvores.
        
    As árvores binárias, por exemplo, são um tipo especial de grafo que não apresenta na sua
estrutura "ciclos". As árvores são ÓTIMAS PARA BUSCAS. 

CONCEITO

    Uma árvore T é um conjunto finito de elementos denominados NÓS ou VÉRTICES. 
    
                              ## ÁRVORE BINÁRIA ##

    Árvores com grau 2, ou seja, cd nó só pode ter no máximo 2 filhos. 
    
                        A  raiz
                      /   \            terminologia: filho esquerdo;
                     B    C                          filho direito;
                   /  \    \                         informação. 
                  D    E    F
    
    Uma árvore é dita "ARVORE BINÁRIA DE BUSCA" (ABB) ou tb denominadas 'árvores de pesquisa' ou 
'árvores ordenadas' se:
    
    * a chave (informação) de cd nó da subarvore da esquerda do nó R é menor que a chave do 
    nó R; 
    
    ** a chave (informação) de cd nó da subarvore da direita do nó R é maior que a chave do 
    nó R;
    
    *** as subárvores esquerda e direita também são ABB
  
                          D*  R1    
                      /      \            
                     B       F                          
                   /  \     /  \                         
                  A   C    E    G
                  
                       
                  
                          D*  R2
                      /      \            
                     A       F     # Esta não é uma ÁRVORE BINÁRIA DE BUSCA.      
                   /  \     /  \     B é > que A e está a sua esquerda.                      
                  B*  C    E    G

    São estruturas eficientes para busca de elementos pq se o elemento alvo é menor que o nó, 
percorre-se a subárvore da esquerda, se maior percorre-se a subárvore da direita. 

                          D*  R1    
                      /      \            
                     B       F                          
                   /  \     /  \                         
                  A   C    E    G
                  
                  Exemplo: Busca do elemnto 'E'. 
consulta 1        E > nó raiz D >> o elemento está a direita de D.
consulta 2        E < nó raiz F >> o elemnto, se fizer parte do conjunto, está à esquerda de F
consulta 3        E = E (E faz parte do conjunto)

obs.: é necessário que a árvore esteja balanceada (n.º nós à Esq = n.º nós a Dir.). Nestes casos, 
existem as árvores "AVL" ou "Rubro-negras". 




@author: andra
"""

