# Turtle India Flag

import turtle

wn = turtle.Screen()
wn.title("India Flag")
print(wn.screensize())

pt = turtle.Turtle()
pt.color('#000080')
pt.speed(0)
pt.width(2)

pt.begin_fill()
for i in range(1,361):
    if i%10 == 0:
        hd = pt.heading()
        pt.left(90)
        pt.forward(30)
        pt.right(180)
        pt.penup()
        pt.forward(30)
        pt.pendown()
        pt.right(90)
        pt.setheading(hd)
    pt.forward(0.25)
    pt.right(1)
pt.end_fill()

# Draw Circle Around chakra
center_x,center_y = pt.position()
pt.penup()
pt.setheading(90)
pt.backward(14.32)
pt.setheading(180)
pt.forward(50)
pt.right(90)
pt.pendown()
for i in range(1,361):
    pt.right(1)
    pt.forward(0.87)
pt.penup()
pt.setposition(center_x,center_y)


pt.setheading(180)

# Saffron Box
pt.fillcolor('#ff9933')
pt.forward(250)
pt.color('black')
x,y = pt.position()
pt.right(90)
pt.forward(60)
pt.pendown()
pt.fillcolor('#ff9933')
pt.begin_fill()
pt.forward(150)
pt.right(90)
pt.forward(500)
pt.right(90)
pt.forward(150)
pt.right(90)
pt.forward(500)
pt.end_fill()

# Green Box
pt.fillcolor('#138808')
pt.setposition(x,y)
pt.left(90)
pt.forward(90)
pt.begin_fill()
pt.forward(150)
pt.left(90)
pt.forward(500)
pt.left(90)
pt.forward(150)
pt.left(90)
pt.forward(500)
pt.end_fill()
pt.setposition(x,y)
pt.penup()
pt.setheading(0)
pt.penup()
pt.forward(500)
pt.pendown()
pt.left(90)
pt.forward(60)
pt.left(180)
pt.forward(150)
pt.ht()

wn.exitonclick()
