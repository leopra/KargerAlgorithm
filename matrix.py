import random
import numpy


def parseFileCoords(filename):
    with open('./datasets/' + filename, 'r') as f:
        lines = f.readlines()
        n=len(lines)
        ### creazione matrice ####
        adjmatrix = numpy.zeros(shape=(n,n))

        for line in lines:
            adj = line.strip().split()
            vertice=int(adj[0])-1
            for i in range(1, len(adj)):
                edge=int(adj[i])-1
                adjmatrix[vertice][edge]= 1
            
        print(adjmatrix)

    return adjmatrix


#parseFileCoords('input_random_1_6.txt')


def ListEdge(filename):
    with open('./datasets/' + filename, 'r') as f:
        lines = f.readlines()
        nodes=len(lines)
        ### creazione lista archi ######
        adjlist=[]
        for line in lines:
            element = line.strip().split()
            node=element[0]
            for i in range(1, len(element)):
                edge=element[i]
                if node < edge:
                    arco= (node, edge)
                else:
                    arco= (edge, node)
                adjlist.append(arco)

        ## eliminazione archi doppi #####
        adjlist= list(set(adjlist))
        #print(len(adjlist))
        #print(adjlist)

    return adjlist, nodes

def changeEdge(lista, nodea, nodeb):
    new= nodea + '-' + nodeb ## nuovo nodo 
    for i in range(0, len(lista)):
            tupla=lista[i]
            if tupla[0]==nodea or tupla[0]==nodeb:
                lista[i]= (new, tupla[1])
            elif tupla[1]==nodea or tupla[1]==nodeb:
                lista[i]= (new, tupla[0])
    return lista

def Contraction(filename):
    edges, nodes= ListEdge(filename) #lista archi #
    while nodes>2:
        x= random.choice(edges) ## estrazione casuale arco ##
        nodea= x[0]
        nodeb= x[1]
        #### rimuovere arco selezionato e gli eventuali duplicati ####
        while x in edges:
            edges.remove(x)
        nodes=nodes-1
        ### sostituire con nuovo nodo e riposizionare gli archi corretti ###
        edges=changeEdge(edges, nodea, nodeb)  
        
    print('Final result: ', len(edges))


Contraction('input_random_20_75.txt')


