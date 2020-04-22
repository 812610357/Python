b_str = str(12345)  # 把其他形式转化为字符串
print(b_str)  # 打印字符串
print(type(b_str))  # 打印b_str的数据类型
print(len(b_str))  # 返回字符串的长度
b_str = eval(b_str)  # 把字符串转化为数值型，一般用于输入数值
print(type(b_str))
print(hex(123))  # 将整数转化为十六进制小写字符串
print(oct(123))  # 将整数转化为八进制小写字符串
print(chr(65))  # 将Unicode编码转化为字符
print(ord('A'))  # 将字符转化为Unicode编码
