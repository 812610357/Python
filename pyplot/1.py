import matplotlib.pyplot as plt
import numpy as np

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
# plt.title("title")
plt.legend()
# y轴刻度
plt.yticks([0, 2, 4, 6, 8, 10])
plt.show()
