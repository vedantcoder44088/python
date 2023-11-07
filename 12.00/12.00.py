import turtle


screen = turtle.Screen()
screen.bgcolor("lightyellow")


square_turtle = turtle.Turtle()
square_turtle.color("blue")
square_turtle.fillcolor("lightblue")
square_turtle.begin_fill()


for _ in range(4):
    square_turtle.forward(100)
    square_turtle.right(90)

square_turtle.end_fill()

turtle.hideturtle()
turtle.done()


import turtle


screen = turtle.Screen()
screen.bgcolor("lightyellow")


rectangle_turtle = turtle.Turtle()
rectangle_turtle.color("red")
rectangle_turtle.fillcolor("pink")
rectangle_turtle.begin_fill()


for _ in range(2):
    rectangle_turtle.forward(150)
    rectangle_turtle.right(90)
    rectangle_turtle.forward(80)
    rectangle_turtle.right(90)

rectangle_turtle.end_fill()


turtle.hideturtle()
turtle.done()



import turtle


screen = turtle.Screen()
screen.bgcolor("lightyellow")


star_turtle = turtle.Turtle()
star_turtle.color("green")
star_turtle.fillcolor("lightgreen")
star_turtle.begin_fill()


for _ in range(5):
    star_turtle.forward(100)
    star_turtle.right(144)

star_turtle.end_fill()
turtle.hideturtle()
turtle.done()
