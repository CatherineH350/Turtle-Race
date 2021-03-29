import turtle

cameraMan = turtle.Turtle()
cameraMan.shape("triangle")

cameraMan.penup()
cameraMan.goto(-200, 200)
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
  cameraMan.forward(15)
  cameraMan.right(90)