import numpy as np
from random import random
import matplotlib.pyplot as plt
from matplotlib import rc
from preprocessing import fromListOfMatrixToListOfVectors
from simplexEmbedding import SimplexEmbedding
from dephasedEmbedding import DephasedEmbedding

'
def Depolarised3to1PORAC(theta):
    s = 1/np.sqrt(2)*np.array([[1, 1/np.sqrt(2)*np.sin(theta), 1/np.sqrt(2)*np.sin(theta), np.cos(theta)],
                                   [1, 1/np.sqrt(2)*np.sin(theta), 1/np.sqrt(2)*np.sin(theta),-np.cos(theta)],
                                   [1, 1/np.sqrt(2)*np.sin(theta),-1/np.sqrt(2)*np.sin(theta), np.cos(theta)],
                                   [1, 1/np.sqrt(2)*np.sin(theta),-1/np.sqrt(2)*np.sin(theta),-np.cos(theta)],
                                   [1,-1/np.sqrt(2)*np.sin(theta), 1/np.sqrt(2)*np.sin(theta), np.cos(theta)],
                                   [1,-1/np.sqrt(2)*np.sin(theta), 1/np.sqrt(2)*np.sin(theta),-np.cos(theta)],
                                   [1,-1/np.sqrt(2)*np.sin(theta),-1/np.sqrt(2)*np.sin(theta), np.cos(theta)],
                                   [1,-1/np.sqrt(2)*np.sin(theta),-1/np.sqrt(2)*np.sin(theta),-np.cos(theta)]])
    e = 1/np.sqrt(2)*np.array([[1, 0, 0, 1],
                               [1, 0, 0,-1],
                               [1, 0, 1, 0],
                               [1, 0,-1, 0],
                               [1, 1, 0, 0],
                               [1,-1, 0, 0]])
    u = np.array([np.sqrt(2), 0, 0, 0])
    mms = np.array([1/np.sqrt(2), 0, 0, 0])
    return s.T, e.T, u, mms

def Dephased3to1PORAC(theta, basis):
    s = 1/np.sqrt(2)*np.array([[1, 1/np.sqrt(2)*np.sin(theta), 1/np.sqrt(2)*np.sin(theta), np.cos(theta)],
                                   [1, 1/np.sqrt(2)*np.sin(theta), 1/np.sqrt(2)*np.sin(theta),-np.cos(theta)],
                                   [1, 1/np.sqrt(2)*np.sin(theta),-1/np.sqrt(2)*np.sin(theta), np.cos(theta)],
                                   [1, 1/np.sqrt(2)*np.sin(theta),-1/np.sqrt(2)*np.sin(theta),-np.cos(theta)],
                                   [1,-1/np.sqrt(2)*np.sin(theta), 1/np.sqrt(2)*np.sin(theta), np.cos(theta)],
                                   [1,-1/np.sqrt(2)*np.sin(theta), 1/np.sqrt(2)*np.sin(theta),-np.cos(theta)],
                                   [1,-1/np.sqrt(2)*np.sin(theta),-1/np.sqrt(2)*np.sin(theta), np.cos(theta)],
                                   [1,-1/np.sqrt(2)*np.sin(theta),-1/np.sqrt(2)*np.sin(theta),-np.cos(theta)]])
    e = 1/np.sqrt(2)*np.array([[1, 0, 0, 1],
                               [1, 0, 0,-1],
                               [1, 0, 1, 0],
                               [1, 0,-1, 0],
                               [1, 1, 0, 0],
                               [1,-1, 0, 0]])
    u = np.array([np.sqrt(2), 0, 0, 0])
    if basis == 1:
        mem = 1/np.sqrt(2)*np.array([[1, 0, 0, 1],
                                     [1, 0, 0,-1]])
    elif basis == 2:
        mem = 1/np.sqrt(2)*np.array([[1, 0, 1, 0],
                                     [1, 0,-1, 0]])
    elif basis == 3:
         mem = 1/np.sqrt(2)*np.array([[1, 1, 0, 0],
                                      [1,-1, 0, 0]])
    else:
        theta=np.random.random()*np.pi/2;
        phi=np.random.random()*np.pi;
        mem = 1/np.sqrt(2)*np.array([[1, np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)],
                                     [1,-np.sin(theta)*np.cos(phi),-np.sin(theta)*np.sin(phi),-np.cos(theta)]])
    return s.T, e.T, u, mem.T

def AnalyticalRobustness(x):
    return (x-2/3)/(x-1/2)

def Depolarised3to1PORACPlot():
    plt.rcParams['font.size'] = 22
    x = np.zeros(51)
    y = np.zeros(51)
    for k in range(51):
        x[k] = k*np.pi/100
#        x[k] = (1/24*(12+4*(np.sqrt(2)*np.sin(k*np.pi/100)+np.cos(k*np.pi/100))))
        states,effects,unit,mms = Depolarised3to1PORAC(k*np.pi/100)
        y[k] = SimplexEmbedding(states,effects,unit,mms)[0]
    x2 = np.linspace(2/3,1/2*(1+1/np.sqrt(3)),100)
    plt.ylabel(r"Robustness to dephasing" + "\n" + r"w.r.t. Z-axis")
    plt.xlabel(r'$\theta$') 
    return plt.plot(x, y, "ob"), plt.plot(x2, AnalyticalRobustness(x2),color='red')

def Dephased3to1PORACPlot():
    plt.rcParams['font.size'] = 22
    x = np.zeros(51)
    y = np.zeros(51)
    for k in range(51):
 #       x[k] = k*np.pi/100
        x[k] = (1/24*(12+4*(np.sqrt(2)*np.sin(k*np.pi/100)+np.cos(k*np.pi/100))))
        states,effects,unit,axis = Dephased3to1PORAC(k*np.pi/100,1)
        y[k] = DephasedEmbedding(states,effects,unit,axis)
    plt.ylabel(r"Robustness to dephasing" + "\n" + r"w.r.t. Z-axis")
    plt.xlabel(r'Success rate') 
    return y, plt.plot(x, y, "ob")

def MinDephased3to1PORACPlot():
    plt.rcParams['font.size'] = 22
    x = np.zeros(50)
#    y = np.zeros(51)
    y1 = np.zeros(50)
#    y_aux2 = np.zeros((2,30))
    y_aux3 = np.zeros((3,50))
#    y_aux4 = np.zeros((4,30))
    y_aux5 = np.zeros((5,50))
    y_aux10 = np.zeros((13,50))
    y_aux20 = np.zeros((23,50))
    y_aux100 = np.zeros((103,50))
    for k in range(50):
  #      x[k] = k*np.pi/100
        x[k] = (1/24*(12+4*(np.sqrt(2)*np.sin(k*np.pi/100)+np.cos(k*np.pi/100))))
        states,effects,unit,axis = Dephased3to1PORAC(k*np.pi/100,1)
        y1[k] = DephasedEmbedding(states,effects,unit,axis)
        for j in range(3):
            states,effects,unit,axis = Dephased3to1PORAC(k*np.pi/100,j+1)
            r = DephasedEmbedding(states,effects,unit,axis)
            y_aux3[j][k] = r
        for j in range(5):
            states,effects,unit,axis = Dephased3to1PORAC(k*np.pi/100,j+1)
            r = DephasedEmbedding(states,effects,unit,axis)
            y_aux5[j][k] = r
        for j in range(13):
            states,effects,unit,axis = Dephased3to1PORAC(k*np.pi/100,j+1)
            r = DephasedEmbedding(states,effects,unit,axis)
            y_aux10[j][k] = r
        for j in range(23):
            states,effects,unit,axis = Dephased3to1PORAC(k*np.pi/100,j+1)
            r = DephasedEmbedding(states,effects,unit,axis)
            y_aux20[j][k] = r
        for j in range(103):
            states,effects,unit,axis = Dephased3to1PORAC(k*np.pi/100,j+1)
            r = DephasedEmbedding(states,effects,unit,axis)
            y_aux100[j][k] = r
    y3 = np.min(y_aux3, axis=0)
    y5 = np.min(y_aux5, axis=0)
    y10 = np.min(y_aux10, axis=0)
    y20 = np.min(y_aux20, axis=0)
    y100 = np.min(y_aux100, axis=0)
    plt.ylabel(r"Robustness to dephasing" + "\n" + r"(min. $X,Y,Z$)")
    plt.xlabel(r'Success rate') 
    plt.plot(x, y3, "ob",label="$X,Y,Z$")
#    plt.plot(x, y5, "ob", linewidth=2, label="$X,Y,Z+2$")
#    plt.plot(x, y10, "-r",label="$X,Y,Z+10$") 
#    plt.plot(x, y20, "--b", label="$X,Y,Z+20$")
#    plt.plot(x, y100, ":g", label="$X,Y,Z+100$")
#    plt.legend(loc="center left", fontsize=13, handlelength=2, labelspacing=0)
    return plt.show()

def ManyStates(n):
    states = 1/np.sqrt(2)*np.array([1,1,0]);
    effects = 1/np.sqrt(2)*np.array([1,1/np.sqrt(2),1/np.sqrt(2)]);
    for k in range(2*n):
        states = np.append(states,np.array([1/np.sqrt(2),1/np.sqrt(2)*np.cos((k+1)*np.pi/n),1/np.sqrt(2)*np.sin((k+1)*np.pi/n)]));
        effects = np.append(effects,np.array([1/np.sqrt(2),1/np.sqrt(2)*np.cos((k+1)*np.pi/n+np.pi/4),1/np.sqrt(2)*np.sin((k+1)*np.pi/n+np.pi/4)]));
    s = np.array_split(states,states.size/3);
    e = np.array_split(effects,states.size/3);
    #effects = 1/np.sqrt(2)*np.array([[1, 1, 0],
    #                                 [1,-1,0],
    #                                 [1, 0, 1],
    #                                 [1, 0,-1]]);
    unit = np.array([np.sqrt(2),0,0]);
    mms = np.array([1/np.sqrt(2),0,0]);
    return np.array(s).T, np.array(e).T, unit, mms

def PlotManyStates():
    plt.rcParams['font.size'] = 22
    x = np.zeros(40);
    y = np.zeros(40);
    for k in range(38):
        s,e,u,mms = ManyStates(k);
        x[k] = s.shape[1]-1;
        y[k] = SimplexEmbedding(s,e,u,mms)[0];
    plt.ylabel(r"Robustness to" + "\n" + "depolarisation")
    plt.xlabel(r"Number of preparations/measurement"+"\n"+"outcomes")
    plt.yticks(np.arange(0,0.55,0.1))
    return plt.plot(x,y,"ob")