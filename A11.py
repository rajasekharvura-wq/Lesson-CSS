import turtle

# creating canvas
turtle.Screen().bgcolor("Pink")

sc = turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
    board.forward(100)
    board.right(90)
turtle.done()