# -*- coding: utf-8 -*-
'''
Representação de grafos
Autores: Israël e Renan
'''
def matriz_adj(vertices):
    matrix=[]
    row=[]
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            ans=int(input("vertices entre {} e {}? \n1 sim \n\n0 não".format(vertices[i],vertices[j])))
            row.append(ans)
        matrix.append(row)
        row=[]
    return matrix
    
def matriz_incid(vertices):
    arestas=
print("Vértices do grafo:")
vertices=[int(x) for x in input().split()]
opt=input("Escolha o tipo de representação:\n1 matriz de adjacência\n2 matriz de incidência\n3 lista de adjacências")
matrix=[]
if opt == 1:
    matrix=matriz_adj(vertices)
elif opt == 2:
    matrix=matriz_incid(vertices)