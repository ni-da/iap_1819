import turtle

wn = turtle.Screen()  # Creates a playground for turtles
wn.bgcolor("beige")  # Set the window background color
wn.title("Hello, Tess!")  # Set the window title

tess = turtle.Turtle()  # Create a turtle, assign to alex
tess.pensize(3)
for c in ["yellow", "red", "purple", "blue"]:
    tess.color(c)
    tess.forward(50)
    tess.left(90)

wn.mainloop()  # Wait for user to close window
