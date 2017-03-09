import numpy as np
import matplotlib.pyplot as plt

dodlighet = np.loadtxt("dodlighet.txt",skiprows = 1)
qk = dodlighet[:,1]/1000.


Fx=1-np.cumprod(1-qk[35:])

print len(Fx)



px=Fx-np.append(np.array([0]),Fx[:-1])
x = np.linspace(35,71,37)
print x




E = 100000./(1.03**35)*1.0/(1-1/1.03)*np.sum((1-(1.0/1.03)**(x-34))*px[35:])

x = np.linspace(0,71,72)
print x[35:]

Eg = 1.0/(1-1/1.03)*(1-np.sum((1/1.03)**(x[:35]+1)*px[:35]) - np.sum((1/1.03)**35 * px[35:]))

print "Gjennomsnitt utbetalt: %g" %E
print "E[g(x)] = %g" %Eg

print "Premie som maa betales: %g" %(E/Eg)

plt.plot(px)
plt.show()
