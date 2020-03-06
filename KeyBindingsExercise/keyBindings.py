import turtle

#created window
window = turtle.Screen()
window.title("Key Binding tests by Allen")
window.setup(width = 800, height= 800)
window.bgcolor("Black")
window.tracer(0)

#object/s inside window

__object__ = turtle.Turtle()
__object__.speed(0)
__object__.shape("circle")
__object__.color("white")
__object__.penup()
__object__.goto(0,0)


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


#key bindings

window.listen()
window.onkeypress(objectUp, "w")
window.onkeypress(objectDown, "s")
window.onkeypress(objectRight, "d")
window.onkeypress(objectLeft, "a")


#main loop
while True:
    window.update()