import turtle  as t
from random import choice , randint
the_turtle = t.Turtle()
the_turtle.speed(0)
the_turtle.width(1)
t.colormode(255)
l_r = [0,90,180,270]
def change_color ():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rgb = (r,g,b)
    return rgb
def draw_shape(number) :
    angle = 360 / number
    for i in range(number) :
       the_turtle.forward(100)
       the_turtle.right(angle)

def random_walk():
    for i in range(400) :
        the_turtle.color(change_color())
        the_turtle.forward(20)
        the_turtle.setheading(choice(l_r))      
def dashed_line():
    for i in range(10) :
        the_turtle.forward(5)
        the_turtle.penup()
        the_turtle.forward(5)
        the_turtle.pendown()
def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)) :
        the_turtle.circle(125)
        the_turtle.color(change_color())
        current_heading =  the_turtle.heading()
        the_turtle.setheading(current_heading + size_of_gap)
        

dashed_line()
for i in range(3,11):
    the_turtle.color(change_color())
    draw_shape(i)
random_walk()


spirograph(2)

    
    
   
    















screen = t.Screen()
screen.exitonclick()