a_list = ['hahaha', 'good', 1, 4, [3, 4]]  # 创建列表
print(a_list[1], a_list[-2])  # 读取列表数据
print(a_list[2:-1], a_list[3:])  # 列表切片，左闭右开
print(a_list[::2])  # 起始和终止都可以缺省，可以设置步长
print('id=', id(a_list), sep='')
a_list = a_list + [-1]  # 用“+”添加元素，会创建一个新列表，而不是直接添加这样子操作速度慢
print('id=', id(a_list), sep='')
a_list.append(['as', 56])  # 直接在原列表上添加一个元素，不会修改地址，操作速度快
print(a_list)
a_list.extend([12, 'a'])  # 添加一串元素也不会修改地址
print('id=', id(a_list), sep='')
print(a_list)
a_list.remove(-1)  # 删除指定元素
print(a_list)
print(a_list.pop(-3))  # 删除并返回对应编号上的元素，缺省为最后一位
print(a_list)
del a_list[0:2:1]  # 删除指定区间内的元素，或指定编号元素，也可以指定步长
print(a_list)
del a_list  # 删除整个列表
