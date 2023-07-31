def cross(A,B):
	return {a+b for a in A for b in B}
urn = cross('W','12345678') | cross('B','123456') | cross('R','123456789')
print(urn)
import itertools
U6 = list(itertools.combinations(urn,6))
# for s in U6:
# 	print(s)
# print(len(U6))
for s in U6:
	if s[0][0]=='R' and s[-1][0]=='R':
		print(s)