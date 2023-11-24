import matplotlib.pyplot as plt

x=[]
y=[]

for n in range(-100,101):
    x = x + [n]
    print(x)

for n in x:
    y = int(x)**2-3

plt.bar(x, y)
plt.show()