from turtle import *
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("Black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)
         

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
     
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

game_is_on = True

while game_is_on:
     time.sleep(0.1)
     screen.update()
     ball.move()

     if ball.ycor()>300 or ball.ycor()<-300:
          ball.collision_with_walls()

     if ball.distance(r_paddle) < 40 and ball.xcor() > 340:
          ball.collision_with_paddles()
     if ball.distance(l_paddle) < 40 and ball.xcor() < -340:
          ball.collision_with_paddles()

screen.exitonclick()