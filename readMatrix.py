import random
import math 
import sys 

#random.seed(42)

#to make the algorithm faster COULD USE IF WORKED a randomdict https://github.com/robtandy/randomdict

def parseFileCoords(filename):

    adjmatrix = dict()
    with open('./datasets/' + filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            adj = line.strip().split(' ')
            adjmatrix[int(adj[0])] = [int(x) for x in adj[1:]]

    #print(list(adjmatrix.items()))
    return adjmatrix

def FullContraction(dictionary):
    
    adjmatrix = dictionary.copy()
    #free id for new node that contract 2 nodes
    nodecounter = len(adjmatrix)
    #i save the merges in case i need some info
    merges= { }

    while len(adjmatrix) > 2: #index could be wrong
        nodecounter += 1

        #choose 2 random items from the key of the dictionary
        #nodea,nodeb = random.sample(list(adjmatrix.keys()), 2)
        
        nodea = random.sample(list(adjmatrix.keys()), 1)[0]
        nodeb = random.sample(adjmatrix[nodea], 1)[0]
        
        #delete those elements
        x = adjmatrix.pop(nodea)
        y = adjmatrix.pop(nodeb)

        #create a new node with all the connections (except the ones between the 2 initial nodes)
        adjmatrix[nodecounter] = [i for i in x+y if i != nodea and i != nodeb]
        merges[nodecounter] = (nodea,nodeb)

        for nods in adjmatrix[nodecounter]:
            #rename all occurences of nodea and nodeb with new node nodecounter
            adjmatrix[nods] = list(map(lambda x: nodecounter if x == nodea or x== nodeb else x, adjmatrix[nods]))

    keys= list(adjmatrix.keys())
    return len(adjmatrix[keys[0]])


def KargerAlg(adjmatrix, k):
    minum = math.inf
    for i in range(k):
        temp = FullContraction(adjmatrix)
        if temp < minum:
            minum = temp
        print('calculating ', i)
    return minum


a = parseFileCoords('input_random_18_75.txt')

print('KARGER: ', KargerAlg(a, int(sys.argv[1])))