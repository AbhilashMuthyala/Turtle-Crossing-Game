from turtle import Turtle


FONT = ("Courier", 24, "normal")

#manages level and game over sequence

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        print("called")
        self.goto(-250,275)
        self.board_refresh()

    def board_refresh(self,level=1):
        self.clear()
        self.write(f" LEVEL: {level} ", move=False, align='center',font=('Courier', 20, 'normal'))

    def gameover(self):
        #self.clear()
        self.goto(0,0)
        self.write(f" GAMEOVER ", move=False, align='center',font=('Courier', 20, 'normal'))


