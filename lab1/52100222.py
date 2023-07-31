#Exercise 5
import itertools

def cross(A, B):
#The set of ways of concatenating one item from collection A with one from B.
    return {a + b for a in A for b in B}
urn = cross('M', '1234')
urn2=cross('L', '123') 
print(urn)
print(urn2)
for i in list(itertools.combinations(urn,3)):
  for j in list(itertools.combinations(urn2,2)):
      print(i+j)
s=len(list(itertools.combinations(urn,3)))+len(list(itertools.combinations(urn2,2)))
print(s)
#Exercise 6
#a
import itertools
def cross(A, B):
#The set of ways of concatenating one item from collection A with one from B.
    return {a + b for a in A for b in B}
urn = cross('S', '123456789'+'JQK') | cross('P', '123456789'+'JQK') | cross('D', '123456789'+'JQK')| cross('H', '123456789'+'JQK')
urn=list(urn)+["S10","P10","D10","H10"]
nhom5=list(itertools.combinations(urn,5))
poker_5=nhom5
len_poker_5=len(nhom5)
print(len_poker_5)
count=0
a=[]
for s in nhom5:
  count=0
  for i in s:
    for j in s:
      if(i[0]==j[0] and i[1]!=j[1]):
        count=count+1
  if(count==6):
    a.append(s)
#b
three_of_a_kind=a
len_three_of_a_kind=len(a)
print(len(a))



#bai6
import itertools
def cross(A, B):
#The set of ways of concatenating one item from collection A with one from B.
    return {a + b for a in A for b in B}
urn = cross('S', '123456789'+'JQK') | cross('P', '123456789'+'JQK') | cross('D', '123456789'+'JQK')| cross('H', '123456789'+'JQK')
urn=str(urn)+"S10"+"P10"+"D10"+"H10"
print(urn)
nhom5=list(itertools.combinations(urn,5))
count=0
a=[]
for s in nhom5:
  count=0
  for i in s:
    for j in s:
      if(i[0]==j[0] and i[1]!=j[1]):
        count=count+1
  if(count==3):
    a.append(s)
print(len(a))
print(a)