import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[1,3,4,5,6,7]
m=['k','l','l','k','j','l']

mapping = {'j' : 'o', 'k': 'x', 'l': '+'}

for i in range(len(x)):
    plt.scatter(x[i], y[i], marker=mapping[m[i]])
plt.show()