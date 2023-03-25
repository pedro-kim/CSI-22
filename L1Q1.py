import turtle

s = turtle.getscreen()

t = turtle.Turtle()

for i in range(0, 5):
    # Position the turtle:
    t.penup()
    t.goto(10 + 10 * i, 10 + 10 * i)
    # Draw the square:
    t.pendown()
    t.right(90)
    t.forward(20 + 20 * i)
    t.right(90)
    t.forward(20 + 20 * i)
    t.right(90)
    t.forward(20 + 20 * i)
    t.right(90)
    t.forward(20 + 20 * i)
