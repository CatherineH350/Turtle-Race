import turtle
import random

#Fuctions: a group of related statements that perform a specific task. Fuctions help us breakdown our program into sections. 
#DRY: Don't Repeat Yourself
#Formula: 
#def fuctionName (parameters)
#  BODY
#  optional 'return' statement

catherine = turtle.Turtle()
coolKid = turtle.Turtle()
turtleJr = turtle.Turtle()
yay = turtle.Turtle()
coder = turtle.Turtle()

def drawTrack(length):

  cameraMan = turtle.Turtle()
  cameraMan.shape("triangle")

  cameraMan.penup()
  cameraMan.goto(-175, 140)
  cameraMan.speed(0)
  cameraMan.right(90)

  for i in range(length):
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


def createTurtles():
  catherine.shape("turtle")
  catherine.penup()
  catherine.goto(-200, 110 )
  catherine.color("#F2A8C6")

  coolKid.shape("turtle")
  coolKid.penup()
  coolKid.goto(-200, 70)
  coolKid.color("#E8C192")

  turtleJr.shape("turtle")
  turtleJr.penup()
  turtleJr.goto(-200, 30)
  turtleJr.color("#92E8A3")

  yay.shape("turtle")
  yay.penup()
  yay.goto(-200, -10)
  yay.color("LightSlateBlue")

  coder.shape("turtle")
  coder.penup()
  coder.goto(-200, -50)
  coder.color("DarkOrchid")

#Create 4 other turtles with different colors; set their locations

def startRace():
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


drawTrack(16) #fuction call
createTurtles()
startRace()