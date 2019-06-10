import matplotlib as mpl
import matplotlib.pyplot as plt
import random as rand

mpl.__version__

plt.plot([1, 3, 5], [2, 5, 7])
plt.show()

x = rand.sample(range(0,10),10)
y = rand.sample(range(0,10),10)

x1 = list(map(lambda x: x - 1, x))
y2 = list(map(lambda y: y - 1, y))

plt.plot(x, y, label='Legenda da serie')
plt.xlabel('Eixo x - Variavel 1')
plt.ylabel('Eixo y - Variavel 2')
plt.title('Testando Matplotlib 3.0.2')

plt.legend()
plt.show()


plt.bar(x, y, label='Serie 1', color='r')
plt.bar(x1, y2, label='Serie 2', color='y')
plt.legend()
plt.show()

idades = [22, 65, 45, 55, 21, 22, 34, 42, 41, 4, 99, 101, 120, 122, 130, 111, 115, 80, 75, 54, 44, 64, 13, 18, 48]
ids = [x for x in range(len(idades))]
print(ids)
plt.bar(ids, idades)
plt.show()

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
#plt.hist(idades, bins, histtype='bar', rwidth=0.8)
plt.hist(idades, bins, histtype='stepfilled', rwidth=0.8)
plt.show()

x2 = [rand.sample(range(0, 10), 10)]
y2 = [rand.sample(range(0, 10), 10)]
plt.scatter(x2, y2, label = 'Pontos', color='r', marker='o', s=100)
plt.legend()
plt.show()
