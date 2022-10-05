import matplotlib.pyplot as plt
alt=0
x=[]
y=[]
#primeira volta
for c in range(0,2):
    x.append(alt)
y.append(alt)
alt+=2
y.append(alt)
#looping
for c in range(0,100):
    for o in range(0,2):
        x.append(alt)
    y.append(alt)
    alt=(alt*2)*-1
    y.append(alt)

print(x,y)
plt.plot(x, y)
plt.show()
