import matplotlib.pyplot as plt
import math
#iniciada os arrays
x = []
y = []
raio = 5

# a^2=b^2+c^2
# a = raio logo
#  raio = raiz quadrada de a^2 + b^2

for c in range(1,10):
    x.append(c)

for q in x:
    y.append(math.sqrt(
    raio**2 +    q**2
    ))

print(x,y)


plt.scatter(x,y)
plt.show()