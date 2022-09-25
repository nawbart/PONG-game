import turtle

width, height = turtle.Screen().window_width(), turtle.Screen().window_height()
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


while True:
    sc.update()