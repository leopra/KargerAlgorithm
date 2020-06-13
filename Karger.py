import Contraction as c
import math
import time

MAX= 9223372036854775807

def defineK(n):
    k= ((n*n)/2)* math.log(n)
    print(round(k))
    return round(k)

def karger(filename, k):
    #timeinit = time.time()
    min= MAX
    while k>0:
        if time.time() > timeinit + 600:
            break
        print(k)
        edges=c.FullContraction(filename)
        if edges<min:
            min=edges
        k=k-1
    print(min)
    return min


listfile=['input_random_20_75.txt']
string=""
f=open('ResultKarger1.txt', 'w+')
#for i in range(0, len(listfile)):
start_time = time.time()
min= karger('input_random_20_75.txt', defineK(75))
print("time : %s seconds " % (time.time() - start_time))
string+= 'input_random_20_75.txt' + '  ' +  str((time.time() - start_time)) + '  ' + str(min) + '\n'
f.write(string)
f.close