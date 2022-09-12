from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")  # Title of the game
screen.tracer(0)  # Turn off the animation

# Create a snake body

snake = Snake()
    
# Create a snake movement
while True:
    screen.update()
    time.sleep(0.2)
    snake.move()

        
        
        

    
    
    
    
    
    
    
    
screen.exitonclick()