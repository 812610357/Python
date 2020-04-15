import os
for i in range(1, 10):
    for j in range(1, i+1):
        print("%dx%d=%-2d " % (i, j, i * j), end=' ')
    print("")
os.system("pause")
letter, number, other = 0, 0, 0
for char in input("请输入一串字符:"):
    if char >= '0' and char <= '9':
        number = number+1
        continue
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        letter = letter + 1
        continue
    other = other + 1
print("这串字符中含有")
print("数字%d个" % number)
print("字母%d个" % letter)
print("其他字符%d个" % other)
os.system("pause")
