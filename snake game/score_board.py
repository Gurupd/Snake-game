from turtle import Turtle 
FONT=("Courier",24,"normal")
ALIGNMENT="center"
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"score:{self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over",align=ALIGNMENT,font=FONT)

    def increase(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

        
