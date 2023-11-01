from turtle import *
import time

title('türk bayraği')
setup(width=600,height=400)
bgcolor('red')

def renkkonum(renk,x,y):
    penup()
    goto(x,y)
    pendown()
    color(renk)
    begin_fill()
        
def yildiz():
    renkkonum('white',80,25)
    for i in range(5):
        forward(50)
        right(144)
        forward(50)
        right(-72)
    end_fill()

def hilal(cap):
    circle(cap)
    end_fill()
        
renkkonum('white', -110,-120)
hilal(130)
renkkonum('red',-70,-90)
hilal(100)
yildiz()
mainloop()

