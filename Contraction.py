import random
import numpy
import time

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

def FullContraction(filename):
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


#### test per prima domanda#####
listfile=['input_random_1_6.txt', 'input_random_2_6.txt','input_random_3_6.txt', 'input_random_4_6.txt', 'input_random_5_10.txt', 'input_random_6_10.txt', 'input_random_7_10.txt',
'input_random_8_10.txt', 'input_random_9_25.txt', 'input_random_10_25.txt', 'input_random_11_25.txt', 'input_random_12_25.txt', 'input_random_13_50.txt', 
'input_random_14_50.txt', 'input_random_15_50.txt', 'input_random_16_50.txt', 'input_random_17_75.txt', 
'input_random_18_75.txt', 'input_random_19_75.txt',  'input_random_20_75.txt', 'input_random_21_100.txt', 'input_random_22_100.txt', 'input_random_23_100.txt', 'input_random_24_100.txt', 
'input_random_25_125.txt', 'input_random_26_125.txt', 'input_random_27_125.txt', 'input_random_28_125.txt', 
'input_random_29_150.txt', 'input_random_30_150.txt', 'input_random_31_150.txt', 'input_random_32_150.txt', 
'input_random_33_175.txt', 'input_random_34_175.txt', 'input_random_35_175.txt', 'input_random_36_175.txt', 'input_random_37_200.txt', 
'input_random_38_200.txt', 'input_random_39_200.txt', 'input_random_40_200.txt']

string=""
f=open('TimeFullContraction.txt', 'w+')
for i in range(0, len(listfile)):
    print(i)
    start_time = time.time()
    FullContraction(listfile[i])
    string+= listfile[i] + '  ' +  str((time.time() - start_time)) + '\n'
    print("time : %s seconds " % (time.time() - start_time))
f.write(string)
f.close

