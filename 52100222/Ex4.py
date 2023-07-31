import itertools
import numpy as np
def Cross(A,B):
	return {a + b for a in A for b in B}
Urn1 = Cross('M','1234')
Urn2 = Cross('P','123')
Urn3 = Cross('C','12')
Urn4 = Cross('L','1')
permute_1 = list(itertools.permutations(Urn1,4))
permute_2 = list(itertools.permutations(Urn2,3))
permute_3 = list(itertools.permutations(Urn3,2))
permute_4 = list(itertools.permutations(Urn4,1))
dif = (len(permute_1)*len(permute_2)*len(permute_3)*len(permute_4)) *np.math.factorial(4)
per = permute_1 + permute_2 +permute_3 + permute_4
# permute_k = list(itertools.permutations(Urn1+Urn2 + Urn3 +Urn4,4))
# print(len(permute_k))
permute_k = list(itertools.permutations(per,4))

print(permute_k)
print(dif)
print(per)