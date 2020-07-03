import numpy as np
import matplotlib.pyplot as plt
from statistics import mean 

f = open('ResultKarger100.txt')
content = f.readlines()
f.close()

f = open('ResultKargerLeo2.txt')
content1 = f.readlines()
f.close()

results = []
num=0
for i in content:
     a ,opt,real,d = i.strip().split()
     results.append((num, ((float(real) - float(opt))/float(opt))*100))
     num += 1

print(results)

fig = plt.figure()
langs = list(range(1,len(results)+1))
students = [res[1] for res in results]
plt.bar(langs,students)
plt.xticks(list(range(1,len(results)+1)))

plt.show()
