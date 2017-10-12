# -*- coding: utf-8 -*-
'''
Grau do vértice solicitado
Autores: Israël e Renan
'''
def ler_grafo():
    print("Insira os vértices do seu grafo:")
    vertices=[int(x) for x in input().split()]
    graph={}
    print("Na representação de matriz de adjacências: 1 para presença de aresta ou arco\n0 para ausência de aresta ou arco\n")
    print([" {} ".format(x) for x in vertices])
    for i in vertices:
        linhas={}
        ent=[int(x) for x in input("{}:".format(i)).split()]
        for x in enumerate(ent):
            linhas[vertices[x[0]]]=x[1]
        graph[i]=linhas
    return graph

def grau_vertice(grafo):
    q=int(input("Escolha o vértice cujo grau quer saber"))
    cont=0
    e=0#grau de entrada
    s=0#grau de saída
    o=input("Tipo de grafo:\n o orientado\n n não orientado\n")
    if o=='n':
        for i in graph[q].values():
            if i==1:
                cont+=1
        print("Grau do vértice {}: {}".format(q,cont))
    elif o=='o':
        #calcula o grau de saída do vértice q
        for i in graph[q].values():
            if i==1:
                s+=1
                
        
        #calcula o grau de entrada
        for i in graph.values():
            if i[q]==1:
                e+=1
            
        print("=============================\n\
        Grau de saída do vértice {}: {}\n\
        Grau de entrada do vértice {}: {}".format(q,s,q,e))
    
graph=ler_grafo()
grau_vertice(graph)