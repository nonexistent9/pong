from turtle import *
from paddle import Paddle


screen = Screen()
screen.bgcolor("Black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)
         

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
     

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

game_is_on = True
while game_is_on:
     screen.update()

screen.exitonclick()