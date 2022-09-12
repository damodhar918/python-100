from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")  # Title of the game
screen.tracer(0)  # Turn off the animation

#TODO: Create a snake body
snake = Snake()

#TODO Turn the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")    
screen.onkey(snake.right, "Right")
    
#TODO Create a snake movement
while True:
    screen.update()
    time.sleep(0.09)
    snake.move()
    
    
    
screen.exitonclick()