import matplotlib.pyplot as plt
import numpy as np

data = [
    [21.0,	0.6267,	0.6492]
    [34.8,	0.5985,	0.6214]
    [39.9,	0.5872,	0.6107]
    [45.0,	0.5765,	0.6004]
    [50.0,	0.5658,	0.5895]
    [54.9,	0.5555,	0.5800]
    [59.9,	0.5453,	0.5696]
    [64.9,  0.5326, 0.5595]
]

x = [1950, 1970, 1990, 2010]
num = [2.519, 5.692, 5.263, 6.972]
x = np.array(x)
y = np.array(num)

# 多项式拟合(x,y,次数)
f1 = np.polyfit(x, y, 3)
p1 = np.poly1d(f1)
t = np.linspace(1950, 2010)

plot1 = plt.plot(x, y, 's', label="original values")
plot2 = plt.plot(t, p1(t), 'r', label="polyfit values")

plt.xlabel("year")
plt.ylabel('hhh')
plt.title("title")
plt.legend()
# y轴刻度
plt.yticks([0, 2, 4, 6, 8, 10])
plt.show()
