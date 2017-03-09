import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.misc import factorial


y = np.linspace(0,10,11)

N = 200
p = 0.02


P = binom.pmf(y,N,p)


x = np.linspace(0,10,11)
poisson = 4**(x)*np.exp(-4)/factorial(x)




plt.title("Fordelingen til Y, med Poisson")
plt.xlabel("Y")
plt.ylabel("p(y)")
plt.plot(y,P)
plt.plot(x,poisson,"r")

plt.legend(["Binomial","Poisson"])
plt.show()
