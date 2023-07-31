import matplotlib.pyplot as plt
import math
def pmf_bernoulli(p,x):
    if (x == 1):
        return p
    return 1-p
def plot_pmf_bernoulli(p):
    X = [0,1]
    P_bernoulli = [pmf_bernoulli(p,x) for x in X]
    plt.plot(X,P_bernoulli,'o')
    plt.title('PMF of Bernoulli(p=%.2f)'%(p))
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()
# print(pmf_bernoulli(0.5,1))
# plot_pmf_bernoulli(0.5)
def nperk (n,k):
    return (math.factorial(n))/((math.factorial(k))*((math.factorial(n-k))))
def pmf_binom(k,n,p):
    return nperk(n,k)*p**k*(1-p)**(n-k)
def plot_pmf_binom(n,p):
    K = list(range(0,n+1))
    P_binom = [pmf_binom(k,n,p) for k in K]
    plt.plot(K,P_binom,'-o')
    axes = plt.gca()
    axes.set_xlim([0,n])
    axes.set_ylim([0,1.1*max(P_binom)])

    plt.title('PMF of Bin(%i, %.2f)'%(n,p))
    plt.xlabel('Number k of successes')
    plt.ylabel('Probability of k success')
    plt.show()
# print(pmf_binom(4,15,0.5))
# plot_pmf_binom(15,0.5)
def pmf_poisson(k,lam):
    return ((lam**k)*((math.e)**(-lam)))/math.factorial(k)

def plot_pmf_poisson(n,lam):
    K = list(range(0,n+1))
    P_poisson = [pmf_poisson(k,lam) for k in K]
    plt.plot(K,P_poisson,'-o')
    plt.title('PMF of Poisson(%i)'%lam)
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()
# print(pmf_poisson(10,5))
# plot_pmf_poisson(25,5)
def pmf_geo(p,x):
    return p*(1-p)**(x-1)
def plot_pmf_geo(n,p):
    K = list(range(0,n+1))
    P_geo = [pmf_geo(p,k) for k in K]
    plt.plot(K,P_geo,'-o')
    plt.title('PMF of Geo(%0.2f)'%p)
    plt.xlabel('n')
    plt.ylabel('Probability')
    plt.show()
# print(pmf_geo(0.3,5))
# plot_pmf_geo(10,0.3)
#Ex1a
print("Ex1")
print(pmf_binom(2,5,0.1))
#Ex1b
plot_pmf_geo(5,0.1)
#Ex2a
print("Ex2")
print(pmf_poisson(2,3))
#Ex2b
plot_pmf_poisson(5,3)
#Ex3a
print("Ex3")
print(pmf_geo(0.4,3))
plot_pmf_geo(10,0.4)