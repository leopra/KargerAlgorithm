import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


##### line plot con media #####
def plotLine():
    labels=['6', '10', '25', '50', '75', '100', '125', '150', '175', '200']
    time=[9.78708267211914e-05, 0.00012624263763427734, 0.0009779930114746094, 0.011298954486846924, 0.04109221696853638,0.11278682947158813 , 0.28355300426483154,
    0.5602636337280273, 1.0336890816688538, 1.8040754795074463]
    
    index = np.arange(10)
    bar_width = 0.15
    opacity = 0.8

    plt.plot(time, linestyle='--', marker='o', color='r', label="FullContraction")

    y_pos = np.arange(len(labels))
    plt.rcParams["figure.figsize"] = (14,10)
    plt.ylabel('Tempo in secondi ')
    plt.xlabel('Dimensione Grafo')
    plt.xticks(y_pos, labels)
    plt.legend()
    plt.show()

plotLine()

##### line plot con media per karger #####
def plotKarger():
    labels=['6', '10', '25', '50', '75']
    time=[0.00215238332748413, 0.0123276114463806, 0.944083213806152, 53.0861380696297,
    487.797095239162]
    
    index = np.arange(5)
    bar_width = 0.15
    opacity = 0.8

    plt.plot(time, linestyle='--', marker='o', color='r', label="FullContraction")

    y_pos = np.arange(len(labels))
    plt.rcParams["figure.figsize"] = (10,10)
    plt.ylabel('Tempo in secondi ')
    plt.xlabel('Dimensione Grafo')
    plt.xticks(y_pos, labels)
    plt.legend()
    plt.show()

plotKarger()

##### line plot numero ripetizioni FulContraction #####
def plotIt():
    labels=['6', '10', '25', '50', '75', '100', '125', '150', '175', '200']
    ripetizioni=[]
    with open('NumContraction.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            t = line.strip().split()
            ripetizioni.append(t[1])

    print(ripetizioni)
    index = np.arange(10)

    plt.plot(ripetizioni, linestyle='--', marker='o', color='b')

    y_pos = np.arange(len(labels))
    plt.rcParams["figure.figsize"] = (14,10)
    plt.ylabel('Iterazioni totali')
    plt.xlabel('Dimensione Grafo')
    plt.xticks(y_pos, labels)
    plt.show()

#plotIt()

def b_plot(p, labels, groups, a, xy):
    # create plot
    #fig, ax = plt.subplots()
    ax=a
    index = np.arange(groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, p, bar_width, alpha=opacity,color='r')

    y_pos = np.arange(len(labels))
    if xy==1:
        plt.xlabel('Dimensione')
        plt.ylabel('Time')
    plt.xticks(y_pos, labels, fontsize=8)
    plt.tight_layout()


def plotTime():
    t1, t2, t3, t4, t5 = [], [], [], [], []
    x1= ['6', '6', '6', '6', '10', '10', '10', '10']
    x2= ['25', '25', '25', '25', '50', '50', '50', '50']
    x3= ['75', '75', '75', '75', '100', '100', '100', '100']
    x4= ['125', '125', '125', '125', '150', '150', '150', '150']
    x5= ['175', '175', '175', '175', '200', '200', '200', '200']
    labels= []
    count= 1
    with open('TimeFullContraction.txt') as f:
        lines = f.readlines()
        for line in lines:
            value= line.split()
            if count<9:
                t1.append(float(value[1]))
            elif count>8 and count<17:
                t2.append(float(value[1]))
            elif count>16 and count<25:
                t3.append(float(value[1]))
            elif count>24 and count<33:
                t4.append(float(value[1]))
            elif count>32:
                t5.append(float(value[1]))
            count+=1

    ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
    b_plot(t1, x1, 8, ax1, 1)
    ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
    b_plot(t2, x2, 8, ax2, 0)
    ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
    b_plot(t3, x3, 8, ax3, 0)
    ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)
    b_plot(t4, x4, 8, ax4, 1)
    ax5 = plt.subplot2grid((2,6), (1,3), colspan=2)
    b_plot(t5, x5, 8, ax5, 0)
    plt.show()

#plotTime()