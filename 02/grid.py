import turtle

i = 25

turtle.penup()
turtle.goto(-250, 250)

while(i > 0):
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

    i -= 1

    if(i % 5 == 0 & i != 25):
        turtle.backward(500)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)

turtle.exitonclick()
    
