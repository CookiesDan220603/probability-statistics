def cross(A,B):
	return {a+b for a in A for b in B}
urn = cross('W','12345678') | cross('B','123456') | cross('R','123456789')
print(urn)
urn1 = cross('W','12345678')
urn2 = cross('B','123456')
urn3 = cross('R','123456789')
import itertools
U6 = list(itertools.combinations(urn,3))

print(U6)
print(len(U6))
#b
U1 = list(itertools.combinations(urn1,3))
U2 = list(itertools.combinations(urn2,3))
U3 = list(itertools.combinations(urn3,3))
dif = len(U6) - len(U1)- len(U2) - len(U3)
print(dif)
dem =0;
#c
for s in U6:
	if s[0][0] == 'W' and s[1][0] == 'R':
		print(s)
		dem+=1
print(dem)

