from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        """
        Create a turtle at the start of the level
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.to_begining()


    def move(self):
        """
        Method for moving turtle
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)
        # if self.at_end():
        #     self.to_begining()

    def at_end(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def to_begining(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
