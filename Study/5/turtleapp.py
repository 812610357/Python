import turtle
turtle.setup(800, 600)  #绘图窗体位置和大小设置
turtle.color("blue")  #画笔颜色
turtle.pensize(10)  #画笔大小
turtle.penup()  #抬起画笔
turtle.goto(-200, 100)  #移动到绝对坐标
turtle.pendown()  #放下画笔
turtle.fd(200)  #向前走
turtle.circle(50, 270)  #走圆弧
turtle.seth(90)  #转到绝对角度
turtle.bk(200)  #向后走
turtle.right(240)  #向右原地旋转
for i in range(6):
    turtle.fd(50)
    turtle.left(60)  #向左原地旋转
turtle.done()