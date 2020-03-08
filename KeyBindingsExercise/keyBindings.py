import turtle

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
__object__.goto(0,0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = -0.15
ball.dx = -0.15


#gravity
gravity = 0.0001


#functions to move object

def objectUp():
    y = __object__.ycor()
    y += 10
    __object__.sety(y)

def objectDown():
    y = __object__.ycor()
    y -= 10
    __object__.sety(y)

def objectRight():
    x = __object__.xcor()
    x += 10
    __object__.setx(x)

def objectLeft():
    x = __object__.xcor()
    x -= 10
    __object__.setx(x)

def jump():
    y = __object__.ycor()
    y += 20
    y -= 10
    __object__.sety(y)


#key bindings

window.listen()
window.onkeypress(objectUp, "w")
window.onkeypress(objectDown, "s")
window.onkeypress(objectRight, "d")
window.onkeypress(objectLeft, "a")
window.onkeypress(jump, "e")


#main loop
while True:
    window.update()

    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1 #this reverses the ball direction

    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1 #this reverses the ball direction

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1 #this reverses the ball direction

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1 #this reverses the ball direction