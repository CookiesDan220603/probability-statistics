import itertools
E = [1,2,3,4]
k =3
P = [p for p in itertools.product(E, repeat=k)]
print(P)
print("there are ",len(P),"codes")
print("\n")
E = {'a','b','c','d'}
k =3
n = len(E)
permute_k = list(itertools.permutations(E,k))
print("%i-permutations of %s : " %(k,E))
for i in permute_k:
	print(i)
print("Size = ","%i!/(%i-%i)! = "%(n,n,k), len(permute_k))

print("\n")

choose_k = list(itertools.combinations(E,k))
print("%i-combinations of %s : "%(k,E))
for i in choose_k:
	print(i)
print("Number of combinations = %i!/(%i!(%i-%i)!) = %i"%(n,k,n,k,len(choose_k)))
