from turtle import *

bgcolor("cyan")


def draw_rectangle(Size,Position,Fill:bool,Color:str,Fillcolor:str):

    setheading(0)

    if Fill:
        begin_fill()

    penup()
    goto(Position[0] - Size[0] / 2,Position[1] + Size[1] / 2) 
    pendown()

    color(Color)
    fillcolor(Fillcolor)

    for x in range(1,5):
        if x % 2 == 0:
            forward(Size[1])
        else:
            forward(Size[0])
        right(90)
    end_fill()

def draw_triangle(Size,Position,Fill:bool,Color:str,Fillcolor:str):

    setheading(0)

    if Fill:
        begin_fill()

    penup()
    goto(Position[0] - Size[0] / 2,Position[1] + Size[1] / 2) 
    pendown()

    color(Color)
    fillcolor(Fillcolor)

    for x in range(0,4):
        if x % 3 == 0:
            forward(Size[1])
        else:
            forward(Size[0])
        left(120)
    end_fill()

speed(100000)

def draw_castle(x,y):
    penup()
    goto(x,y)
    pendown()
    draw_rectangle([100,400],[-300,0],True,"gray","darkgray")

    draw_rectangle([20,40],[-350,220],True,"gray","darkgray")
    draw_rectangle([20,40],[-300,220],True,"gray","darkgray")
    draw_rectangle([20,40],[-250,220],True,"gray","darkgray")

    draw_rectangle([500,300],[0,-50],True,"gray","darkgray")

    draw_rectangle([100,400],[300,0],True,"gray","darkgray")

    draw_rectangle([20,40],[350,220],True,"gray","darkgray")
    draw_rectangle([20,40],[300,220],True,"gray","darkgray")
    draw_rectangle([20,40],[250,220],True,"gray","darkgray")

    draw_rectangle([125,100],[0,150],True,"gray","darkgray")

    draw_triangle([150,75],[75,162],True,"grey","lightgreen")

    draw_rectangle([150,150],[0,-120],True,"gray","black")

draw_castle(0,0)

exitonclick()
