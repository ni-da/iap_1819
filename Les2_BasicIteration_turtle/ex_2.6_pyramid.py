import turtle

x = 4
wn = turtle.Screen()  # Creates a playground for turtles
tess = turtle.Turtle()

for i in range(x):
    tess.left(90)
    tess.forward(50)
    tess.right(90)
    tess.forward(50)

tess.left(180)
tess.forward(50)
tess.left(180)

for i in range(x):
    tess.forward(50)
    tess.right(90)
    tess.forward(50)
    tess.left(90)

wn.mainloop()  # Wait for user to close window
