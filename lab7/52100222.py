import matplotlib.pyplot as plt
import math
def generator_data(a,b,size):
    n = (b-a)/(size-1)
    result = []
    s = a
    while s<b:
        result.append(s)
        s = s + n
    if len(result) < size:
        result.append(b)
    return result
# X = generator_data(4,6,100)
# print(X)
def pmf_uniform_cont(a,b):
    return 1/(b-a)
# print(pmf_uniform_cont(3,5))
def plot_omf_uniform_cont(a,b):
    X = generator_data(a,b,100)
    if b!=a:
        P = [pmf_uniform_cont(a,b) for x in X]
        plt.plot(X,P,'-')
        plt.plot([a,a], [0,1/(b-a)],'g--')
        plt.plot([b,b],[0,1/(b-a)],'g--')
        plt.title("PDF of Uniform continuous distribution(%0.2f,%0.2f)"%(a,b))
        plt.show()
# plot_omf_uniform_cont(4,6)
def pmf_normal(x,mu,sigma):
    
    pmf = (1/math.sqrt(2*math.pi*(sigma**2)))*(math.exp(-0.5*((x-mu)/sigma)**2))
    return pmf

def cdf_normal(x,mu,sigma):
    return 0.5*(1+math.erf((x-mu)/(sigma*math.sqrt(2))))

def plot_pmf_normal(mu,sigma):
    X = generator_data(mu-4*sigma,mu+4*sigma,1000)
    P_normal = [pmf_normal(x,mu,sigma) for x in X]
    plt.plot(X,P_normal,'-')
    plt.title('PMF of normal(%0.2f,%0.2f)'%(mu,sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()
# plot_pmf_normal(0,1.5)
#EX1
def plot_cdf_normal(mu,sigma):
    X = generator_data(mu-4*sigma,mu+4*sigma,1000)
    P_normal = [cdf_normal(x,mu,sigma) for x in X]
    plt.plot(X,P_normal,'-')
    plt.title('CDF of normal(%0.2f,%0.2f)'%(mu,sigma))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
plot_cdf_normal(0,1.5)
#EX2
EX3 = cdf_normal(12,10,1) - cdf_normal(9,10,1)
print(EX3)
