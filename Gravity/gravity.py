import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = -1


gravity = -0.01


while True:
    
    ball.sety(ball.ycor() + ball.dy)
