import turtle as t
t.setup(800, 600)
t.color("yellow", "red")  #画笔为黄色，填充为红色
t.pensize(5)
t.begin_fill()  #开始填充
for i in range(5):  #画五角星
    t.fd(300)
    t.right(144)
t.end_fill()  #结束填充
t.done()
