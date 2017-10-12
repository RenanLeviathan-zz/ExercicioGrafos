# -*- coding: utf-8 -*-
'''
Representação de grafos
Autores: Israël e Renan
'''
#matriz de adjacências (tanto orientados como não orientados)

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

#matriz de incidência para grafos direcionados  
def matriz_inc_d(vertices):
    matrix=[]
    print("Insira letras ou numeros como nomes de arcos")
    arcos=[x for x in input().split()]
    row=[]
    for i in range(len(arcos)):
        for j in range(len(vertices)):
            ans=int(input("Sentido do arco '{}' no vertice {}: \n1 para saída\n-1 entrada\n0 ausência de arcos".format(arcos[i],vertices[j])))
            row.append(ans)
        matrix.append(row)
        row=[]
    return matrix

#matriz de incidencia para grafos não direcionados
def matriz_inc_i(vertices):
    matrix=[]
    print("Insira letras ou numeros como nomes de arestas")
    arestas=[x for x in input().split()]
    row=[]
    for i in range(len(arestas)):
        for j in range(len(vertices)):
            ans=int(input("\n1 se houver aresta\n0 se não houver".format(arestas[i],vertices[j])))
            row.append(ans)
        matrix.append(row)
        row=[]
    return matrix
    
def lista_adj(vertices):
    lista={}
    for i in vertices:
        opt=1
        adj=[]
        while opt==1:
            v=int(input("adjacentes a {}\n".format(i)))
            adj.append(v)
            opt=int(input("Adicionar vizinhos\n1 para sim e 0 para não\n?"))
        lista[i]=adj
    return lista
            
def mostrar_matriz(matrix):
    for i in matrix:
        print(i)
        
def mostrar_lista(lista):
    for i in lista:
        print(i)
        
print("Vértices do grafo:")
vertices=[int(x) for x in input().split()]
opt=int(input("Escolha o tipo de representação:\n1 matriz de adjacência\n2 matriz de incidência\n3 lista de adjacências"))
matrix=[]
if opt == 1:
    matrix=matriz_adj(vertices)
elif opt == 2:
    o=int(input("\n1 direcionado\n1 não direcionado: "))
    if o==1:
        matrix=matriz_inc_d(vertices)
    else:
        matrix=matriz_inc_i(vertices)
else:
    lista=listaAdj(vertices)

mostrar_matriz(matrix)
mostrar_lista(lista)