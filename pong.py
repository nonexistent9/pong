from turtle import *

def move_up():
        if right_stick.ycor()<250:
            newy = right_stick.ycor() + 10
            right_stick.goto(right_stick.xcor(),newy)


def move_down():
    if right_stick.ycor() > -250:
        newy = right_stick.ycor() - 10
        right_stick.goto(right_stick.xcor(),newy)
        print(right_stick.ycor())

screen = Screen()
screen.bgcolor("Black")
screen.title("Pong")
screen.setup(width=800,height=600)


right_stick = Turtle()
right_stick.color("White")
right_stick.shape("square")
right_stick.shapesize(5,1)
right_stick.penup()
right_stick.goto(350,0)

screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")










screen.exitonclick()