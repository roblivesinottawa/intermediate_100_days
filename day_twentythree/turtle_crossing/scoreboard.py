from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        # create a new attribute that will keep the score
        self.level = 1
        self.hideturtle()
        self.penup()
        # define the position of the scoreboard
        self.goto(-280, 250)
        self.update_scoreboard

# define a method that can be called by other methods to update the scoreboard
    def update_scoreboard(self):
        # this will prevent the score from bring overwritten 
        self.clear()
        self.write(f"Level: {self.level}",align="left", font=FONT)   

# define a method that will handle the increase of level
    def increase_level(self):
        self.level += 1
        self.update_scoreboard


# create a method that will show game over on the screen
    def game_over(self):
        # this will center the message
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT) 



    
