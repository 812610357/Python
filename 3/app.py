import os
m = int(input("n="))
sum, n = 0, 1
while n <= m:
    sum = sum + n
    n = n + 1
print("sum=%d" % sum)
os.system("pause")

for i in range(1000, 10000):
    a = i // 100  # 取前两位数
    b = i % 100  # 取后两位数
    if (a + b) ** 2 == i:
        print(i)
