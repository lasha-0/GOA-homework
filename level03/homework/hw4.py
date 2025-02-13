import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.speed(5)

t.penup()
t.goto(0, -100)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(0, 70)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(0, 130)
t.pendown()
t.color("darkgreen")
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()
t.goto(0, 150)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(5)
t.end_fill()

t.hideturtle()
screen.mainloop()