from turtle import Turtle 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.dx = 10
        self.dy = 10

    def move(self):    
            newx = self.xcor() + self.dx
            newy = self.ycor() + self.dy
            self.goto(newx,newy)
           
    def collision_with_walls(self):
            self.dy*=-1

    def collision_with_paddles(self):
          self.dx*=-1.1

    def score(self):
          self.goto(0,0)
          self.dx*=-1.1
