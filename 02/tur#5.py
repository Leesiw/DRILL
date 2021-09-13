import turtle

def up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)


def right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def down():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

turtle.shape('turtle')
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(right, 'd')
turtle.onkey(left, 'a')
turtle.listen()
