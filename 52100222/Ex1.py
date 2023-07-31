import itertools
import numpy as np
E = [0,1,2,3,4,5,6,7,8,9]
k = 4
permute_k = list(itertools.permutations(E,k))
print("%i-permutations of %s : " %(k,E))
f = list()
j =0
for i in permute_k:
	m = np.array(i)
	if(m[0]!=0):
		n =m[0]*1000 + m[1]*100 + m[2]*10 + m[3]
		f.append(n)
		j+=1
for i in f:
	print(i)
print("Size = ",len(f))