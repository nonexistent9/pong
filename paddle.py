from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self,position):
          super().__init__()
          self.color("White")
          self.shape("square")
          self.shapesize(5,1)
          self.penup()
          self.goto(position)

    def move_up(self):
        if self.ycor()<250:
            newy = self.ycor() + 20
            self.goto(self.xcor(),newy)

    def move_down(self):
        if self.ycor() > -250:
            newy = self.ycor() - 20
            self.goto(self.xcor(),newy)
