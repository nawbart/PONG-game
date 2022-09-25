import turtle

width, height = turtle.Screen().window_width(), turtle.Screen().window_height()
print(width, height)
#screen
sc = turtle.Screen()
sc.setup(width, height)
sc.title('PONG GAME')
sc.bgcolor('black')

#left pad
left = turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("grey")
left.shapesize(6, 1)
left.penup()
left.goto(-width/2 + 30, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.shapesize(2)
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = 6


def go_up():
    y = left.ycor()
    y += 20
    left.sety(y)


def go_down():
    y = left.ycor()
    y -= 20
    left.sety(y)


sc.listen()
sc.onkeypress(go_up, "Up")
sc.onkeypress(go_down, "Down")

while True:
    sc.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > width/2 - 90:
        ball.dy *= -1

    if ball.xcor() > width / 2 - 30:
        ball.dx *= -1

    if ball.ycor() < -width/2 + 90:
        ball.dy *= -1

    if ball.xcor() < -width / 2 + 30:
        ball.dx *= -1