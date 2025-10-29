import turtle
from time import sleep

t = turtle.Turtle()

def Draw_Shape:
   t.foward(50)
   t.right(90)

t.beginfill()

for i in range(4):
   Draw_Shape

t.endfill()