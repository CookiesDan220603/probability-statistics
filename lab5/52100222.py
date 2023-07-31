#Ex1
import random,collections,math
import numpy as np
def Ex1_lab5():
    x = np.random.choice([0,1,2,3,4,5],3650,p=[0.1,0.2,0.3,0.2,0.15,0.05])
    #a
    X = set(x)
    print(X)
    #b
    P = []
    for i in X:
        P.append((x==i).sum()/len(x))
    print(P)
    #c
    EX = 0
    for x in X:
        EX = EX + (x*P[x-1])
    print(EX)
    VarX = 0
    for x in X:
        VarX = VarX + (x-EX)*(x-EX)*P[x-1]
    print(VarX)
    SD = math.sqrt(VarX)
    print(SD)
    #d
    Pd = 0
    for i in range(3,6):
        print(i)
        Pd = Pd + P[i]
    print(Pd)


def Ex2_lab5():
    #1 is face
    #0 is number
    x=[]
    #a
    for i in range(10000):
        x.append(random.randint(0,2))
    #b
    X = set(x)
    print(X)
    #c
    P = [x.count(i)/len(x) for i in X]
    print(P)
    #d
    EX = 0
    for x in X:
        EX = EX + (x*P[x-1])
    print(EX)
    VarX = 0
    for x in X:
        VarX = VarX + (x-EX)*(x-EX)*P[x-1]
    print(VarX)
    SD = math.sqrt(VarX)
    print(SD)
    #e
    Pd = 0
    for i in range(1,3):
        Pd = Pd + P[i]
    print(Pd)
    

Ex1_lab5()
print("----------------")
Ex2_lab5()
