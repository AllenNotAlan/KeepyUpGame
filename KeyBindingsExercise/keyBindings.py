import turtle
from random import randint

#created window
window = turtle.Screen()
window.title("Key Binding tests by Allen")
window.setup(width = 800, height= 800)
window.bgcolor("Black")
window.tracer(0)

#object/s inside window

__object__ = turtle.Turtle()
__object__.shape("square")
__object__.color("white")
__object__.speed(0)
__object__.shapesize(stretch_wid=0.5, stretch_len=5)
__object__.penup()
__object__.goto(0,-200)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(randint(-350,350),randint(-100,350))
ball.dy = -0.15
ball.dx = -0.15
b = ball.pos()


xball = 0
yball = 0

player_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))


#gravity
gravity = 0.0001


#functions to move object

def objectUp():
    y = __object__.ycor()
    y += 20
    __object__.sety(y)

def objectDown():
    y = __object__.ycor()
    y -= 20
    __object__.sety(y)

def objectRight():
    x = __object__.xcor()
    x += 20
    __object__.setx(x)

def objectLeft():
    x = __object__.xcor()
    x -= 20
    __object__.setx(x)


# def isCollision(ball,__object__):

#     if (ball.xcor() >= (__object__.xcor() - 20)) and (ball.xcor() <= (__object__.xcor() + 20)) and (ball.ycor() >= (__object__.ycor()-20)) and (ball.ycor() <= (__object__.ycor()+20)):
#         return True
#     else:
#         return False


#key bindings

window.listen()
window.onkeypress(objectUp, "w")
window.onkeypress(objectDown, "s")
window.onkeypress(objectRight, "d")
window.onkeypress(objectLeft, "a")


#main loop
while True:

    window.update()

    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1 #this reverses the ball direction

    #ball reset when hits the bottom axis
    if ball.ycor() < -390:
        ball.goto(randint(-350,350),randint(100,350))
        ball.dy = -0.15
        player_score = 0
        pen.clear()
        pen.write("Score: {}".format(player_score), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1 #this reverses the ball direction

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1 #this reverses the ball direction

    if (ball.xcor() >= (__object__.xcor() - 40)) and (ball.xcor() <= (__object__.xcor() + 40)) and (ball.ycor() >= (__object__.ycor()-20)) and (ball.ycor() <= (__object__.ycor()+20)):
        ball.dy *=-1
        ball.dx *= randint(-2,2)
        player_score += 1
        pen.clear()
        pen.write("Score: {}".format(player_score), align="center", font=("Courier", 24, "normal"))
        