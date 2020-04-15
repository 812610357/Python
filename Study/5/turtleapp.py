import turtle
turtle.setup(800, 600)  #绘图窗体位置和大小设置
turtle.color("blue")  #画笔颜色
turtle.pensize(5)  #画笔大小
turtle.circle(20, steps=6)  #画外接圆半径为20的正六边形
turtle.penup()  #抬起画笔
turtle.goto(-200, 100)  #移动到绝对坐标
turtle.pendown()  #放下画笔
turtle.seth(0)  #转到绝对角度
turtle.fd(200)  #向前走
turtle.circle(50, 270)  #走圆弧
turtle.left(180)  #向左原地旋转
turtle.bk(200)  #向后走
turtle.right(240)  #向右原地旋转
turtle.done()