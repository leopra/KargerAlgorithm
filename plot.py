import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


##### bar plot con media #####
def plotBar():
    labels=['6', '10', '25', '50', '75', '100', '125', '150', '175', '200']
    time=[]
    with open('TimeFullContraction.txt', 'r') as f:
        lines = f.readlines()
        count=1
        media=0
        for line in lines:
            t = line.strip().split()
            if count==3:
                media=media/4
                time.append(media)
                count=0
                media=0
            else:
                media+=float(t[1])
                count+=1
    print(time)
    print(len(time))
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

#plotBar()

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

plotTime()