import turtle

from turtle import*


turtle.hideturtle()

def square_brush(x,y):
    turtle.begin_fill()
    fillcolor('blue')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+10,y)
    turtle.goto(x+10,y+10)
    turtle.goto(x,y+10)
    turtle.goto(x,y)
    turtle.penup()
    turtle.end_fill()


def circle_brush(x):
    turtle.begin_fill()
    fillcolor('red')
    turtle.circle(x)
    turtle.end_fill()

def switch_color():
    turtle.color('yellow')

def switch_color2():
    turtle.color('green')
    
    
    

    
circle_brush(50)
turtle.circle(20)
turtle.onscreenclick(square_brush)
turtle.getscreen().onkeypress(circle_brush, "up")
turtle.getscreen().onkeypress(switch_color, "y")
turtle.getscreen().onkeypress(switch_color2, "g")
    
        
        
turtle.getscreen().listen()
turtle.mainloop()
