import turtle


def draw_square():
    turtle.tracer(0, 0)
    for i in range(400):
        turtle.right(90)
        turtle.forward(i)
    turtle.exitonclick()
