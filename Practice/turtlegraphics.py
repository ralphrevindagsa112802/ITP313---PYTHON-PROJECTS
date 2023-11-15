import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle Graphics")
tortol = turtle.Pen()

tortol.pencolor('red')
tortol.forward(200)
tortol.left(120)
tortol.forward(200)
tortol.left(120)
tortol.forward(200)
tortol.left(120)
for i in range(4):
    tortol.pencolor('green')
    tortol.forward(200)
    tortol.right(90)


tortol.pencolor('black')
tortol.goto(30, -90)
for i in range(4):
    tortol.pencolor('violet')
    tortol.forward(40)
    tortol.right(90)

tortol.pencolor('violet')
tortol.goto(70, -90)
tortol.pencolor('black')
tortol.goto(120, -90)
for i in range(4):
    tortol.pencolor('violet')
    tortol.forward(40)
    tortol.right(90)


turtle.done()

