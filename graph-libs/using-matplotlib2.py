from pylab import *

import numpy as np

x = linspace(0, 5, 10)
y = x ** 2

print(x)
print(y)

figura = plt.figure()

eixos = figura.add_axes([.1, .1, .8, .8])

eixos.plot(x, y, 'r')

eixos.set_xlabel('eixo-x')
eixos.set_ylabel('eixo-y')
eixos.set_title('Grafico de Linha')

plt.scatter(np.arange(50), np.random.randn(50))
plt.show()

figura1 = plt.figure()
ax1 = figura1.add_subplot(1, 2, 1)
ax1.plot(np.random.randn(50), color='r')

ax2 = figura1.add_subplot(1, 2, 2)
ax2.scatter(np.arange(50), np.random.randn(50))
plt.show()
