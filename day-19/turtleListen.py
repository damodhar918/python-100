from turtle import Turtle, Screen

mark = Turtle()
screen = Screen()


def move_forwards():
    mark.forward(10)
    

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()