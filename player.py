from turtle import Turtle,Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# turtle player

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.position = -280
        self.goto(0,self.position)
        self.setheading(90)
        self.reset()

    def moveup(self):
        self.position += 5
        self.sety(self.position)

    def move(self):
        screen = Screen()
        screen.listen()
        screen.onkeypress(self.moveup,'Up')

    def reset(self):
        self.position = -280
        self.goto(0, self.position)
        self.setheading(90)




