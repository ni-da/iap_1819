import turtle

wincol = input("Say a window color: ")
wn = turtle.Screen()  # Creates a playground for turtles
wn.bgcolor(wincol)  # Set the window background color
wn.title("Hello, Tess!")  # Set the window title

tesscol = input("Say a window color: ")
tesspensize = int(input("Tess pen size: "))

tess = turtle.Turtle()  # Create a turtle, assign to alex
tess.color(tesscol)  # Tell tess to change her color
tess.pensize(tesspensize)  # Tell tess to set her pen width

tess.forward(50)  # Tell alex to move forward by 50 units
tess.left(120)  # Tell alex to turn by 90 degrees
tess.forward(50)  # Complete the second side of a rectangle

wn.mainloop()  # Wait for user to close window
