from turtle import Turtle
import random
import time

class Ball(Turtle):
    
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    # self.setheading(45)
    self.x_move = 10
    self.y_move = 10
    self.ball_speed = 0.1

  def move(self):
    # to slow it down either change how much the ball moves each time the while loop (in main) runs or pause so the while loop goes less frequently
    newx = self.xcor() + self.x_move
    newy = self.ycor() + self.y_move
    self.goto(newx, newy)

  def wall_bounce(self):
    # if hits a top/bottom change y cor to neg
    self.y_move *= -1
    # self.y_move += random.randint(-5, 5)

  def paddle_bounce(self):
    # if hits paddle change x cor to neg
    self.x_move *= -1
    # self.ball_speed *= 0.99
    # self.x_move += random.randint(-5, 5)

  def out(self):
    self.goto(0,0)
    time.sleep(1)
    self.x_move *= -1
    # self.ball_speed = 0.1
    
