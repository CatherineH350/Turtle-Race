import turtle
import random

cameraMan = turtle.Turtle()
cameraMan.shape("triangle")

cameraMan.penup()
cameraMan.goto(-175, 140)
cameraMan.speed(0)
cameraMan.right(90)

for i in range(16):
  cameraMan.write(i)
  cameraMan.forward(10)
  cameraMan.pendown()
  cameraMan.forward(200)
  cameraMan.penup()
  cameraMan.right(180)
  cameraMan.forward(210)
  cameraMan.right(90)
  cameraMan.forward(20)
  cameraMan.right(90)
cameraMan.hideturtle()

catherine = turtle.Turtle()
catherine.shape("turtle")
catherine.penup()
catherine.goto(-200, 110 )
catherine.color("#F2A8C6")

coolKid = turtle.Turtle()
coolKid.shape("turtle")
coolKid.penup()
coolKid.goto(-200, 70)
coolKid.color("#E8C192")

turtleJr = turtle.Turtle()
turtleJr.shape("turtle")
turtleJr.penup()
turtleJr.goto(-200, 30)
turtleJr.color("#92E8A3")

yay = turtle.Turtle()
yay.shape("turtle")
yay.penup()
yay.goto(-200, -10)
yay.color("LightSlateBlue")

coder = turtle.Turtle()
coder.shape("turtle")
coder.penup()
coder.goto(-200, -50)
coder.color("DarkOrchid")

#Create 4 other turtles with different colors; set their locations

catherine.pendown()
coolKid.pendown()
turtleJr.pendown()
yay.pendown()
coder.pendown()

for i in range(40):
  catherine.forward(random.randint(1,15))
  coolKid.forward(random.randint(1,15))
  turtleJr.forward(random.randint(1,15))
  yay.forward(random.randint(1,15))
  coder.forward(random.randint(1,15))
