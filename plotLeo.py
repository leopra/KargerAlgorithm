import numpy as np
import matplotlib.pyplot as plt
from statistics import mean 

f = open('ResultKargerLeo.txt')
content = f.readlines()
f.close()

f = open('ResultKargerLeo2.txt')
content1 = f.readlines()
f.close()

content = content + content1

def nodfromname(name):
    idx = name.find('.')
    num = ''
    idx += -1 
    while (name[idx] != '_'):
        num += name[idx]
        idx += -1    
    return (int(num[::-1]))


dizio = dict()
dizio[6]=[]
dizio[10]=[]
j=25
while j < 201:
    dizio[j]=[]
    j +=25

for i in content:
     a,b,c = i.strip().split()
     num = nodfromname(a)
     dizio[num].append(float(c))

#plot
n_groups = len(dizio)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

# rects1 = plt.bar(index, [10*x for x in range(len(dizio))], bar_width,
# alpha=opacity,
# color='b',
# label='Frank')

rects2 = plt.bar(index + bar_width, [mean(x) for x in dizio.values()], bar_width,
alpha=opacity,
color='g',
label='Tempo Medio Soluzione Ottima')

plt.xlabel('graphs')
plt.ylabel('time')
plt.title('Optimal Solution time Plot')
plt.xticks(index + bar_width, ('6','10','25', '50', '75', '100', '125', '150', '175', '200'))
plt.legend()

plt.show()
