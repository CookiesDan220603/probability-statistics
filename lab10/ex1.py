import  random
import math
def flipping_dice(n):
    flips = [random.randint(1, 2) for i in range(n)]
    return flips
def nperk (n,k):
    return (math.factorial(n))/((math.factorial(k))*((math.factorial(n-k))))
def pmf_binom(k,n,p):
    return nperk(n,k)*p**k*(1-p)**(n-k)
def pp_pmf_binom(n,p):
    K = list(range(0,n+1))
    P_binom = list([pmf_binom(k,n,p) for k in K])
    return P_binom
def expectation(n,p):
    return n*p
def variance(n,p):
    return expectation(n,p)*(1-p)
def stdev(n,p):
    return math.sqrt(variance(n,p))
a = flipping_dice(1000)
b = [a.count(1),a.count(2)]
c = pp_pmf_binom(1000,0.5)
E = expectation(1000,0.5)
var = variance(1000,0.5)
std = stdev(1000,0.5)

