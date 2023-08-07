from turtle import Turtle

class Ball(Turtle):
    
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    # set heading in initialization, only change if hits something
    self.setheading(45)
    # self.move()
    # self.x_move = 10
    # self.y_move = 10

  def move(self):
    # to slow it down either change how much the ball moves each time the while loop (in main) runs or pause so the while loop goes less frequently
    # newx = self.xcor() + self.x_move
    # newy = self.ycor() + self.y_move
    # self.goto(newx, newy)
    # below wouldnt let me change x and y cor independently of each other
    # self.setheading(45)
    self.forward(10)

  def wall_bounce(self):
    # if hits a top/bottom change y cor to neg
    # if hits paddle change x cor to neg
    # self.y_move *= -1
    self.setheading(-self.heading())
