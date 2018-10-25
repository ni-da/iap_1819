import turtle

wn = turtle.Screen()  # Creates a playground for turtles
tess = turtle.Turtle()
tess.speed(1)

tess.penup()
tess.left(90)
tess.forward(50)

tess.pendown()
for i in range(4):
    tess.forward(100)
    tess.left(90)

tess.penup()
tess.left(40)
tess.forward(90)
tess.left(-40)

tess.pendown()
for i in range(4):
    tess.forward(50)
    tess.left(90)

wn.mainloop()  # Wait for user to close window
