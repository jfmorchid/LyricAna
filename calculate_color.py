# coding=utf-8
from __init__ import Predicting
import turtle

x=Predicting("Lyric.txt")
x=x[0]
print(x)
R=int(148*x[0]+119*x[2]+238*x[3]+255*x[4])/255
G=int(255*x[1]+136*x[2]+180*x[3]+48*x[4])/255
B=int(211*x[0]+255*x[1]+153*x[2]+34*x[3]+48*x[4])/255
print(R*255,G*255,B*255)
turtle.fillcolor(R,G,B)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.begin_fill()
for x in range(4):
    turtle.forward(80)
    turtle.left(90)
turtle.end_fill()
print(turtle.done())