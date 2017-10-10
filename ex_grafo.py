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
    
def matriz_inc_d(vertices):
    matrix=[]
    arestas=[x for x in input.split()]
    row=[]
    for i in range(len(arestas)):
        for j in range(len(vertices)):
            ans=int(input("Sentido do arco: \n1 para saída\n-1 entrada\n0 ausência de arcos"))
            row.append(ans)
        matrix.append(row)
        row=[]
    return matrix

def mostrar_matriz(matrix):
    for i in matrix:
        print(i)
        
print("Vértices do grafo:")
vertices=[int(x) for x in input().split()]
opt=int(input("Escolha o tipo de representação:\n1 matriz de adjacência\n2 matriz de incidência\n3 lista de adjacências"))
matrix=[]
if opt == 1:
    matrix=matriz_adj(vertices)
elif opt == 2:
    matrix=matriz_inc_d(vertices)

mostrar_matriz(matrix)