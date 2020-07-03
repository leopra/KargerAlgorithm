import random
import numpy
import time
import math
import Contraction as c 
import sys

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

def FullContraction(edges,nodes):
    edges = edges.copy()
    nodes = nodes.copy()
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


#### test per prima domanda#####
listfile=['input_random_1_6.txt', 'input_random_2_6.txt','input_random_3_6.txt', 'input_random_4_6.txt', 'input_random_5_10.txt', 'input_random_6_10.txt', 'input_random_7_10.txt',
'input_random_8_10.txt', 'input_random_9_25.txt', 'input_random_10_25.txt', 'input_random_11_25.txt', 'input_random_12_25.txt', 'input_random_13_50.txt', 
'input_random_14_50.txt', 'input_random_15_50.txt', 'input_random_16_50.txt', 'input_random_17_75.txt', 
'input_random_18_75.txt', 'input_random_19_75.txt',  'input_random_20_75.txt', 'input_random_21_100.txt', 'input_random_22_100.txt', 'input_random_23_100.txt', 'input_random_24_100.txt', 
'input_random_25_125.txt', 'input_random_26_125.txt', 'input_random_27_125.txt', 'input_random_28_125.txt', 
'input_random_29_150.txt', 'input_random_30_150.txt', 'input_random_31_150.txt', 'input_random_32_150.txt', 
'input_random_33_175.txt', 'input_random_34_175.txt', 'input_random_35_175.txt', 'input_random_36_175.txt', 'input_random_37_200.txt', 
'input_random_38_200.txt', 'input_random_39_200.txt', 'input_random_40_200.txt']

def getrealresult(filename):
    a = 'output' + filename[5:]
    f = open('./datasets/' + a, 'r')
    r = f.readline().strip()
    f.close()
    return int(r)

def defineK(n):
    k= ((n*n)/2)* math.log(n)
    print(round(k))
    return round(k)


# string=""
# f=open('TimeFullContraction.txt', 'w+')

def KargerAlg(filename, k):
    found= False
    gotten = -1
    minum = math.inf
    REAL = getrealresult(filename)
    for i in range(k):
        temp = c.FullContraction(filename)
        if REAL == temp and found == False:
            gotten = time.time()
            print('TROVATA', gotten)
            found = True
            return temp, gotten
        if temp < minum:
            minum = temp

    return minum, gotten

def nodfromname(name):
    idx = name.find('.')
    num = ''
    idx += -1 
    while (name[idx] != '_'):
        num += name[idx]
        idx += -1
        
    return (int(num[::-1]))

f=open('ResultKarger100.txt', 'w+')

for i in range(0, len(listfile)):
    k = 'NOT_FOUND'
    print(listfile[i], ' ', nodfromname(listfile[i]))
    REAL = getrealresult(listfile[i])
    start_time = time.time()
    partialresult, solvetime = KargerAlg(listfile[i], 10)
    print('solved: ', solvetime)
    end = time.time()
    print("time : %s seconds " % (end - start_time))
    
    if (REAL != partialresult):
        print('NOT FOUND')
    else:
        print("time first_solution: %s seconds " % (solvetime - start_time))
        k = 'found'



    f.write(listfile[i] + '  ' + str(REAL) + '  ' + str(partialresult) + '  ' + str(k) + '\n')


f.close()