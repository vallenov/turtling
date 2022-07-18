import turtle


def draw_circle():
    turtle.tracer(0, 0)
    turtle.left(90)
    for i in range(400):
        turtle.left(90)
        turtle.circle(i, i//200)
        turtle.fd(i)
    turtle.exitonclick()
