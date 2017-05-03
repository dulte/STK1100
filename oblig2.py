import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, bernoulli


def uniform(low, high, n,N):

    mean = (high+low)/2.0
    var = (high-low)**2/12.0

    dist = np.random.uniform(low, high, (N,n))
    meanX = np.mean(dist, axis = 1)
    Z = np.sqrt(n)*(meanX - mean)/np.sqrt(var)
    return Z

def gamma(alpha, beta, n,N):
    mean = alpha*beta
    var = alpha*beta**2
    dist = np.random.gamma(alpha,beta,(N,n))
    meanX = np.mean(dist, axis = 1)
    Z = np.sqrt(n)*(meanX - mean)/np.sqrt(var)
    return Z


def bernoulli(p,n,N):
    mean = p
    var = p*(1-p)
    dist = np.random.binomial(1,p,(N,n))
    meanX = np.mean(dist, axis = 1)
    Z = np.sqrt(n)*(meanX - mean)/np.sqrt(var)
    return Z




N = 10000.
n = 5.
alpha = 0.5
beta = 1
p = 0.75



width = 0.25
lower = -3
upper = 3
numBins = int((upper - lower)/(width)) + 1


interval = np.array([-10**10, -2.5,-2,-1.5,-1,-0.5, 0, 0.5, 1 ,1.5, 2, 2.5 , 10**10])
standard = np.zeros(len(interval)-1)

relative_freq = np.zeros(len(interval)-1)

for n in [5,15,50]:
    Zs = [uniform(-1,1,n,N),gamma(alpha,beta,n,N),bernoulli(p,n,N)]
    Z_names = ["Uniform", "Gamma", "Bernoulli"]

    for Z,name in zip(Zs,Z_names):

        for k in range(int(len(interval))-1):
            standard[k] = norm.cdf(interval[k+1]) - norm.cdf(interval[k])
            relative_freq[k] = (np.sum(Z<interval[k+1])-np.sum(Z<interval[k]))/float(len(Z))



        percentiles = norm.ppf(np.linspace(0.5/float(N),(N-0.5)/float(N),int(N)))
        sorted_Zs = np.sort(Z)


        print "Data for %s Distribution, n = %g:" %(name,n)
        print "-----------------------------"

        plt.hist(Z,bins = numBins, range = (lower,upper))
        plt.title("Distribution of the Normalized Mean for the %s Distribution for n=%g" %(name,n))
        plt.xlabel("Standarized Mean")
        plt.ylabel("Count")
        plt.show()
        plt.clf()

        plt.plot(percentiles,sorted_Zs)
        plt.title("Normal Probability Plot for %s Distribution for n = %g"%(name,n))
        plt.xlabel("Percentile")
        plt.ylabel("Z")
        plt.show()
        plt.clf()

        print "Sannsynlighetene for en standarnormalfordelt variabel:"
        print standard
        print "Relativ frekvenser for Z_n for %s fordeling:" %name
        print relative_freq
        print "Relativ forskjell mellom relative frekvenser for Z_n og en standarnormalfordelt variabel:"
        print np.abs(relative_freq - standard)/standard
        print "                         "
