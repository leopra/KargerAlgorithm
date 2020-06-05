import random

random.seed(42)

def parseFileCoords(filename):
    adjmatrix = dict()
    with open('./datasets/' + filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            adj = line.strip().split(' ')
            adjmatrix[adj[0]] = adj[1:]

    return adjmatrix


def FullContraction(adjmatrix):
    while len(adjmatrix) > 2: #index could be wrong

        #choose 2 random items from the key of the dictionary
        #nodea,nodeb = random.sample(list(adjmatrix.keys()), 2)
        
        nodea = random.sample(list(adjmatrix.keys()), 1)[0]
        nodeb = random.sample(adjmatrix[nodea], 1)[0]
        
        #delete those elements
        x = adjmatrix.pop(nodea, None)
        y = adjmatrix.pop(nodeb, None)
        #create a new node with all the connections (except the ones between the 2 initial nodes)
        adjmatrix[nodea + '-' + nodeb] = [i for i in x+y if i != nodea and i != nodeb]

        #this could be changed with a dictionary of correspondences
        for nods in adjmatrix[nodea + '-' + nodeb]:
            adjmatrix[nods] = list(map(lambda x: nodea + '-' + nodeb if x == nodea or x== nodeb else x, adjmatrix[nods]))
    
    print(adjmatrix)

a = parseFileCoords('input_random_40_200.txt')
FullContraction(a)