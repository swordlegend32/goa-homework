from turtle import *


width(10)

speed(10000)

# Function to Paint Background Green
def Paint_Background_Green():
    bgcolor("green")

#Call The Function To Paint The Background Green
Paint_Background_Green()

penup()
# put our house in the centre
goto(-100,-100)

pendown()



# Fuction To Draw house Walls
def Draw_House_Walls():
    # Reduce The Speed
    speed(5) 
    #Begin Fill
    begin_fill()

    color("blue")
    # a for loop wich loops from 1 to 4 running the code inside 4 times
    for x in range(0,4):
        forward(200)
        left(90)
    #End fill after the square was drawn
    end_fill()

def Draw_House_Door():
    penup()
    goto(-30,-90)
    pendown()
    color("yellow")
    left(90)
    #Begin Fill
    begin_fill()

    # a for loop wich loops from 1 to 3 running the code inside 3 times
    for x in range(1,5):
        # if x is divisable by 2 თუ x ორის ჯერადია
        if x % 2  == 0:
            forward(60)
            right(90)
        else: # id x isnt divisable by 2 თუ x არ არის ორის ჯერადი
             forward(120)
             right(90)
    #End fill after the door was drawn
    end_fill()


def Draw_House_Roof():
    #Choose The Color 
    color("red")
    #Place Pen in the right position
    penup()
    goto(0,280)
    pendown()
    left(150)
    # Start Filling
    begin_fill()
     # a for loop wich loops from 1 to 3 running the code inside 3 times
    for x in range(1,4):
        forward(200)
        left(120)
    # End Filling
    end_fill()

def Draw_House_Window():
    penup()
    goto(-30,50)
    pendown()
    color("yellow")
    right(150)

    # a for loop wich loops from 1 to 3 running the code inside 3 times
    for x in range(1,5):
        # if x is divisable by 2 თუ x ორის ჯერადია
        if x % 2  == 0:
            forward(60)
            right(90)
        else: # id x isnt divisable by 2 თუ x არ არის ორის ჯერადი
             forward(40)
             right(90)
    penup()
    goto(-0,50)
    pendown()
    forward(40)
    penup()
    goto(-30,70)
    pendown()
    right(90)
    forward(60)

#Call All Of The Functions To Draw The House
Draw_House_Walls()
Draw_House_Door()
Draw_House_Roof()
Draw_House_Window()



#Create The Window
exitonclick()



