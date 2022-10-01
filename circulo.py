import matplotlib.pyplot as plt
import math

x=[]
y=[]

raio = 1
ang= 360

for c in range(0,ang):
    x.append(math.cos(c) *raio)
    y.append(math.sin(c) *raio)

plt.scatter(x,y)
plt.show()