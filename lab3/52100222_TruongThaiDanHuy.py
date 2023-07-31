from fractions import Fraction
from itertools import product
import random
import itertools
def P(event,space):
    return Fraction(len(event&space),len(space))
# Ex1
Gender = {'M','F'}
S = {s for s in itertools.product(Gender,repeat = 3)}
#a
print(S)
#b
print(len(S))
#c
B = {s for s in S if 'F' in s}
print(B)
#d
A= {s for s in B if s.count('F')==3}
print(A)
#e
print(P(A,B))
#Ex2
S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam')
, ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]
#a
A = [s for s in S if 'Thanh' in s]
print(A)
#b
B =[s for s in S if 'Nữ' in s]
print(B)
# #c
A_B = []
for i in A :
    for j in B:
        if i == j:
            A_B.append(i)
print(A_B)
#d
P_B = Fraction(len(B),len(S))
print(P_B)
P_A = Fraction(len(A),len(S))
print(P_A)
P_A_B = fractions =(Fraction(len(A_B),len(S)))
print(P_A_B)
#e
print(P_A_B/P_B)

#3
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
#a
Card = list(product(Ranks,Suits))
#b
B_list = list(itertools.combinations(Card,3))
B = random.choice(B_list)
print(B)
#c
A1=[]
for s in B_list:
    count =0
    for j in s:
        if(j[0] =='K'):
            count +=1
    if(count ==1 or count ==2):
        A1.append(s)
print(A1)
#d
A2=[]
for s in B_list:
    count =0
    for j in s:
        if(j[0] =='K'):
            count +=1
    if(count >=1):
        A2.append(s)
print(A2)
#e
print(len(A1)/len(B_list))
print(len(A2)/len(B_list))
