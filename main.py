from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# controls animation 0 means no animation and you need to update the screen manually
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# second part is which key triggers the object's method
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
  time.sleep(ball.ball_speed)

  # scoreboard()
  # take set heading out of move because if in while loop just keeps heading at 45
  ball.move()
  screen.update()
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.wall_bounce()

  # detect collision with r_paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
    ball.paddle_bounce()

  if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.paddle_bounce()

  # if ball.xcor() > 400 or ball.xcor() < -400:
  #   ball.out()
  # KEEP these two separate for score keeping purposes
  if ball.xcor() > 400:
    ball.out()
    scoreboard.l_point()

  if ball.xcor() < -400:
    ball.out()
    scoreboard.r_point()

screen.exitonclick()
