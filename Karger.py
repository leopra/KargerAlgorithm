import Contraction as c

MAX= 9223372036854775807

def karger(filename, k):
    min= MAX
    while k>0:
        edges=c.FullContraction(filename)
        if edges<min:
            min=edges
        k=k-1
    print(min)
    return min

karger('input_random_7_10.txt', 10000)