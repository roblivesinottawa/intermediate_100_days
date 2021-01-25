from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# create a Player class 
class Player(Turtle):
    # this initializes the class
    def __init__(self):
        # this class inherits everything from the parent class
        super().__init__()
        # create turtle player
        # self.speed(0)
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.go_to_start()
        # this will turn the turtle north
        self.setheading(90)

# create a method that will move the turtle upwards, the move distance is stored in a variable
    def move_up(self):
        self.forward(MOVE_DISTANCE)

# create another method that will bring turtle back to the starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

# create a method that will check if turtle has crossed successfully
    def end_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    
