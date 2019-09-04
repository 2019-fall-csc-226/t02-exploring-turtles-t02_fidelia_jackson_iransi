#Jennifer Bertrina Micheala

import turtle
wn = turtle.Screen()
JB = turtle.Turtle()


JB.shape('turtle')
JB.color('blue')

head = 0
pen = 5

JB.setheading(head)
JB.pensize(pen)
JB.pendown()
JB.left(90)
JB.forward(180)
JB.left(90)
JB.forward(45)
JB.left(45)
JB.forward(90)
JB.left(-90)
JB.forward(90)
JB.left(45)
JB.forward(45)
JB.left(90)
JB.forward(180)


JB.penup()
JB.left(90)
JB.forward(250)
JB.left(90)
JB.pendown()
JB.forward(180)
JB.right(90)

JB.forward(90)
JB.right(90)
JB.forward(90)
JB.right(90)
JB.forward(90)
JB.forward(-120)
JB.left(90)
JB.forward(90)
JB.right(90)
JB.forward(100)


wn.mainloop()
