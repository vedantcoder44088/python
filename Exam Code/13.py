import turtle

t = turtle.Turtle()
t.color('red')
t.fillcolor('yellow')
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
turtle.done()