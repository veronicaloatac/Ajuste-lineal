import numpy as np
import matplotlib.pyplot as plt
import pylab

n = 50 # numero de pontos
x = np.arange(-n/2,n/2,1,dtype=np.float64)

m = np.random.uniform(0.3,0.5,(n,))
b = np.random.uniform(5,10,(n,))

y = m*x + b 

z = np.polyfit(x,y,1) 
p = np.poly1d(z)

xs = np.arange(-n/2,n/2,1,dtype=np.float64)
ys = [p(x) for x in xs]

plt.plot(x, y, 'o', label='data')
plt.plot(xs, ys, label='fitted curve')
plt.ylabel('y')
plt.xlabel('x')
plt.savefig('ajuste_lineal.png')