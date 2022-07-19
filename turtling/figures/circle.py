import turtle


def draw_circle():
    turtle.speed(20)
    turtle.left(90)
    for i in range(0, 400, 3):
        turtle.circle(i)
        turtle.right(90)
        turtle.fd(((3.14*(i+2))-(3.14*i))//2)
        turtle.left(90)
    turtle.exitonclick()
