a_str = 'Hello World!'  # 定义一个字符串
print(str.lower(a_str))  # 全小写
print(str.upper(a_str))  # 全大写
print(a_str.upper())  # 全大写
print(a_str.upper())  # 全小写
# 如上<a>.<b>(...)等价于str.<b>(<a>,...),一下均以<a>.<b>(...)形式举例
print(a_str.count('l'))  # 对指定字符计数，可以指定范围，缺省为start=0, end=-1，即整个字符串
