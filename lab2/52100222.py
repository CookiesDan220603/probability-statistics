#Ex1
import random
def simualtor_dice1(n):
    count =0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if (die1 % 2 == 0 and die2 % 2 ==0):
            count +=1
    print(count/n)
print("Ex1")
simualtor_dice1(10)
#Ex2
def simualtor_dice2(n):
    count =0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if ((die1 % 2 == 1 and die2 % 2 ==0) or (die1 % 2 == 0 and die2 % 2 ==1)):
            count +=1
    print(count/n)
print("Ex2")
simualtor_dice2(10)
#Ex3
def simualtor_dice3(n):
    count =0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if (die1 == die2 and die1 %2 ==0):
            count +=1
    print(count/n)
print("Ex3")
simualtor_dice3(10)
#Ex4
def simualtor_dice4(n):
    count =0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if ((die1 == 1 and die2==6) or (die1==6 and die2 ==1)):
            count +=1
    print(count/n)
print("Ex4")
simualtor_dice4(10000)
#Ex5
def simualtor_dice5(n):
    count =0
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if ((die1 + die1)>6):
            count +=1
    print(count/n)
print("Ex5")
simualtor_dice5(10000)
#Ex6
from itertools import product
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))


def simualtor_poker1(n):
    count =0
    count2=0
    for j in range(n):
        for i in range(5):           
            index = random.randint(0,51)
            # print(Cards[index])
            if Cards[index][1]=='♡' :
                count2 +=1
        if count2 ==5:
            count+=1
    print(count/n)
print("Ex6")
simualtor_poker1(3)
#Ex7
def simualtor_poker2(n):
    count =0
    count1=0
    count2=0
    count3=0
    count4=0
    for j in range(n):
        for i in range(4):
            index = random.randint(0,51)
            if Cards[index][1]=='♡' :
                count1+=1
            if Cards[index][1]=='♢' :
                count2+=1
            if Cards[index][1]=='♣' :
                count3+=1
            if Cards[index][1]=='♠' :
                count3+=1
        if count1==count2 and count1 == count3 and count3==count4 and count1==1:
            count+=1
    print(count/n)
print("Ex7")
simualtor_poker2(10000)
#Ex8
import itertools
def combos(items , n):
    return {' '.join(combo) for combo in itertools.combinations(items , n)}

def cross(A, B):
#The set of ways of concatenating one item from collection A with one from B.
    return {a + b for a in A for b in B}
urn = cross('W','12345678') | cross('B','123456') | cross('R','123456789')
U6 = combos(urn, 6)
all=0
for s in U6:
    if s.count('W') == 2 and s.count('B') ==2 and s.count('R') ==2:
        all+=1
print("Ex8")
print(all/(len(U6)))
