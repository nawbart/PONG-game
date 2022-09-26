import turtle

score = 0
width, height = turtle.Screen().window_width(), turtle.Screen().window_height()

#screen
sc = turtle.Screen()
sc.setup(width, height)
sc.title('PONG GAME')
sc.bgcolor('white')

#left pad
left = turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("grey")
left.shapesize(6, 1)
left.penup()
left.goto(-width/2+50, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.shapesize(2)
ball.penup()
ball.goto(0,0)
ball.dx = 7
ball.dy = 1

#wynik
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write(f"Score : 0", align="center",
             font=("Courier", 24, "normal"))


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
        score += 1
        sketch.clear()
        sketch.write(f"Score : {score}", align="center",
                     font=("Courier", 24, "normal"))
        ball.dx *= -1.1


    if ball.ycor() < -width/2 + 90:
        ball.dy *= -1

    if ball.xcor() < -width / 2 + 30:
        #ball.dx *= -1
        ball.setpos(0,0)


    if (ball.xcor() < -width/2 + 60 and ball.xcor() > -width/2 + 40) and (ball.ycor() < left.ycor() + 40 and ball.ycor() > left.ycor() - 40):
        ball.dx *= -1
