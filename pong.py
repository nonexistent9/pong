from turtle import *

"""def move_up():
        if right_stick.ycor()<250:
            newy = right_stick.ycor() + 10
            right_stick.goto(right_stick.xcor(),newy)

def move_down():
    if right_stick.ycor() > -250:
        newy = right_stick.ycor() - 10
        right_stick.goto(right_stick.xcor(),newy)"""

screen = Screen()
screen.bgcolor("Black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)

class Paddle():
     def __init__(self, ypos, xpos):
          self.ypos = ypos
          self.xpos = xpos
          stick = Turtle()
          stick.color("White")
          stick.shape("square")
          stick.shapesize(5,1)
          stick.penup()
          stick.goto(self.ypos,self.xpos)

     
          
     
    

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
     





#screen.listen()
#screen.onkey(move_up,"Up")
#screen.onkey(move_down,"Down")

game_is_on = True
while game_is_on:
     screen.update()

screen.exitonclick()