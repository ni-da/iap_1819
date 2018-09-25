import turtle

x = 4
wn = turtle.Screen()  # Creates a playground for turtles
tess = turtle.Turtle()
tess.speed(1)

turns = 360 / x
lineLength = 300 / x
for i in range(x):
    tess.forward(lineLength)
    tess.left(turns)

wn.mainloop()  # Wait for user to close window
