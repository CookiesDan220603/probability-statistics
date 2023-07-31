#ex1
import random
def simualtor_dice1a(n):
    count =0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if (die1  == die2 ):
            count +=1
    print(count/n)
print("Ex1a")
simualtor_dice1a(10000)
def simualtor_dice1b(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if(die2 != die1):
            count +=1
    print(count/n)
print("Ex1b")
simualtor_dice1b(10)
def simulator_dice1c(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if(die1%2==0 and die2%2==0):
            count +=1
    print(count/n)
print("Ex1c")
simulator_dice1c(10)
def simulator_dice1d(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if(die1%2!=0 and die2%2!=0):
            count +=1
    print(count/n)
print("Ex1d")
simulator_dice1d(10)
def simulator_dice1e(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if((die1%2!=0 and die2%2==0)or (die1%2==0 and die2%2!=0)):
            count +=1
    print(count/n)
print("Ex1e")
simulator_dice1e(10)
def simulator_dice1f(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if(die1==die2==6):
            count +=1
    print(count/n)
print("Ex1f")
simulator_dice1f(10)
def simulator_dice1g(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if(die2+die1>10):
            count +=1
    print(count/n)
print("Ex1g")
simulator_dice1g(10000)
#ex2
import itertools
def cross(A,B):
    return {a+b for a in A for b in B}
def combos(items , n):
    return {' '.join(combo) for combo in itertools.combinations(items , n)}
Urn = cross('B','12') | cross('R','123') | cross('W','12345')
#Ex2a
U3 = combos(Urn,3)
alla = 0
for s in U3:
    if (s.count('B')==3 or s.count('R')==3 or s.count('W')==3):
        alla+=1
print("Ex2a : " +str(alla/len(U3)))
#Ex2b
alla = 0
for s in U3:
    if (s.count('B')==s.count('R')==s.count('W')==1):
        alla+=1
print("Ex2b : " +str(alla/len(U3)))
#Ex2c
alla = 0
for s in U3:
    if (s.count('B')==2 or s.count('R')==2 or s.count('W')==2):
        alla+=1
print("Ex2c : " +str(alla/len(U3)))
#Ex2d
alla = 0
for s in U3:
    if (s.count('R')==2 and s.count('W')==1):
        alla+=1
print("Ex2d : " +str(alla/len(U3)))
#Ex2e
alla = 0
for s in U3:
    if (s.count('W')==3):
        alla+=1
print("Ex2e : " +str(alla/len(U3)))

#Ex3
from itertools import product
Ranks = {1,2,3,4,5,6,7,8,9,10,'J','Q','K'}
Suits={'♡', '♢', '♣', '♠'}
Cards= list(product(Ranks,Suits))
def simulator_poker1(n):
    for j in range(n):
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for i in range(4):
            index = random.randint(0,51)
            if Cards[index][1]=='♡':
                count1+=1
            if Cards[index][1]=='♢':
                count2+=1
            if Cards[index][1]=='♣':
                count3+=1
            if Cards[index][1]=='♠':
                count4+=1
        if(count1==4 or count2==4 or count3==4 or count4==4):
            count5+=1
    print("Ex3a : "+str(count5/n))
simulator_poker1(100)
def simulator_poker2(n):
    for j in range(n):
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for i in range(4):
            index = random.randint(0,51)
            if Cards[index][1]=='♡':
                count1+=1
            if Cards[index][1]=='♢':
                count2+=1
            if Cards[index][1]=='♣':
                count3+=1
            if Cards[index][1]=='♠':
                count4+=1
        if(count1==count2==count3==count4==1):
            count5+=1
    print("Ex3b : "+str(count5/n))
simulator_poker2(100)
def simulator_poker3(n):
    for j in range(n):
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for i in range(4):
            index = random.randint(0,51)
            if Cards[index][1]=='♡':
                count1+=1
            if Cards[index][1]=='♢':
                count2+=1
            if Cards[index][1]=='♣':
                count3+=1
            if Cards[index][1]=='♠':
                count4+=1
        if((count1+count2)==4 or(count3+count4)==4):
            count5+=1
    print("Ex3c : "+str(count5/n))
simulator_poker3(100)
def simulator_poker4(n):
    count=0
    for j in range(n):
        a =[]
        for i in range(4):
            index = random.randint(0,51)
            a.append(Cards[index][0])
        
        if(a[0]==a[1]==a[2]==a[3]):
            count+=1
    print("Ex3d : "+str(count/n))
simulator_poker4(100)
def simulator_poker5(n):
    count=0
    for j in range(n):
        a =[]
        for i in range(4):
            index = random.randint(0,51)
            value = str(Cards[index][0])
            if(value.isnumeric()):
                a.append(Cards[index][0])

        if(len(a)==4):
            count+=1
    print("Ex3e : "+str(count/n))
simulator_poker5(100)
def simulator_poker6(n):
    count=0
    for j in range(n):
        a =[]
        for i in range(4):
            index = random.randint(0,51)
            value = str(Cards[index][0])
            if(value.isnumeric()==False):
                a.append(Cards[index][0])

        if(len(a)==4):
            count+=1
    print("Ex3f : "+str(count/n))
simulator_poker6(100)

#Ex4
Urn = cross('W','12') | cross('B','123') | cross('R','1234')
U3 = combos(Urn,3)
count1=0
for s in U3:
    if(s.count('W')==1 and s.count('B')==1 and s.count('R')==1):
        count1+=1
        print(s)
print("Ex4d : " + str(count1/len(U3)))

#Ex5
def Ex5(n):
    count1 =0
    for i in range(n):
        a = []
        for j in range(5):
            index = random.randint(0,51)
            a.append(str(Cards[index][0]))
        a.sort()
        if(a[0]-a[1]==-1 and a[1]-a[2]==-1 and a[2]<a[3]and a[3]<a[4]):
            count1+=1
    print("Ex5 : " + str(count1/n))

#Ex6
import numpy as np
E = {0,1,2,3,4,5}
k = 3
f = list()
j =0
permute_k = list(itertools.product(E,repeat = k))
for i in permute_k:
	m = np.array(i)
	if(m[0]!=0):
		n =m[0]*100 + m[1]*10 + m[2]
		f.append(n)
		j+=1
print("Size = ",len(f))
#b
k = 4
permute_k = list(itertools.permutations(E,k))
f = list()
j =0
for i in permute_k:
	m = np.array(i)
	if(m[0]!=0 and m[0]!=m[1] and m[1]!=m[2] and m[2]!=m[3]):
		n =m[0]*1000 + m[1]*100 + m[2]*10 +m[3]
		f.append(n)
		j+=1
print("Size = ",len(f))
