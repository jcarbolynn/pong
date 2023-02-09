from turtle import Turtle
# UP = 90
# DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
  
  def __init__(self, xcor, ycor):
    super().__init__()
    self.color("white")
    self.shape("square")
    self.shapesize(stretch_wid = 5, stretch_len = 1)
    self.penup()
    self.goto(xcor, ycor)

  def up(self):
    self.sety(self.ycor() + 10)
    # dont do this or else the paddle changes orientations
    # # if self.xcor() < 280:
    #   self.setheading(UP)
    #   self.forward(MOVE_DISTANCE)

  def down(self):
    self.sety(self.ycor() - 10)
    
  
