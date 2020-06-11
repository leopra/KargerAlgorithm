import Contraction as c
import math
import time

MAX= 9223372036854775807

def defineK(n):
    k= ((n*n)/2)* math.log(n)
    print(round(k))
    return round(k)

def karger(filename, k):
    timeinit = time.time()
    min= MAX
    while k>0:
        if time.time() > timeinit + 10:
            break
        edges=c.FullContraction(filename)
        if edges<min:
            min=edges
        k=k-1
    print(min)
    return min

start_time = time.time()
karger('input_random_17_75.txt', defineK(75))
print("time : %s seconds " % (time.time() - start_time))