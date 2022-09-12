from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = 'center'

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(0, 290)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


