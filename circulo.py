import matplotlib.pyplot as plt
import math


a=[]
b=[]

na=[]
nb=[]
r=100
for c in range(0,r):
    a.append(c)
    b.append( math.sqrt( (r-c)**2 + r**2)  )

for c in a:
    na.append(-1*c)
for c in b:
    nb.append(-1*c)







plt.scatter(0,0)
plt.scatter(a,b)
plt.scatter(b,a)
plt.scatter(na,b)
plt.scatter(b,na)
plt.scatter(nb,a)
plt.scatter(a,nb)
plt.scatter(na,a)
plt.scatter(a,na)
plt.scatter(b,nb)
plt.scatter(nb,b)
plt.scatter(na,nb)
plt.scatter(nb,na)
plt.show()