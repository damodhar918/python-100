from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

#TODO: Create a screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

#TODO: Create and move a paddle

r_paddle = Paddle(350,0)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


#TODO: Create another paddle
l_paddle = Paddle(-350,0)
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, "s")

#TODO: Create the ball and make it move

ball = Ball()

while True:
    screen.update()
    ball.move()
    time.sleep(0.1)
    #TODO: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
#TODO: Detect collision with paddle
#TODO: Detect when paddle misses
#TODO: Keep score



screen.exitonclick()