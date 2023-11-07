import turtle


class Shape:
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)

# Main program
if __name__ == "__main__":

    screen = turtle.Screen()


    my_turtle = turtle.Turtle()

    shapes = [Square() for _ in range(4)]
    for shape in shapes:
        shape.draw()


    screen.exitonclick()