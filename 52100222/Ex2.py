import itertools
import numpy as np
A = {1,2,3,4,5}
k = 3
permute_k = list(itertools.permutations(A,k))
print("%i-permutations of %s : " %(k,A))
f = list()
j =0
for i in permute_k:
	m = np.array(i)
	if(m[0]!=0):
		n =m[0]*100 + m[1]*10 + m[2]
		f.append(n)
		j+=1
for i in f:
	print(i)
print("Size = ",len(f))