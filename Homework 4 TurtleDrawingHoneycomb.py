#Tegan Broderick
#CS110A Homework 4: Turtle Drawing
#Honeycomb Generator
#This program draws hexagons to create a honeycomb image. It asks the user to choose two primary colors, which are assigned to two of the hexagons.

import turtle
turtleScreen = turtle.Screen()
print ("Welcome to the honeycomb generator")
color1 = input("Please choose a primary color:")
color2 = input("Please choose another primary color:")
print ("Please click on the result tab to see the honeycomb you have created")
# The above instruction is intended for users of repl.it

#turtle1 honeycomb
turtle1 = turtle.Turtle()
for i in range (6):
  turtle1.forward(40)
  turtle1.left(60)

#turtle2 honeycomb
turtle2 = turtle.Turtle()
turtle2.color(color1)
turtle2.right(90)
turtle2.up()
turtle2.forward(37)
turtle2.down()
turtle2.left(90)
turtle2.up()
turtle2.forward(62)
turtle2.down()

for i in range (6):
  turtle2.forward(40)
  turtle2.left(60)

#turtle3 honeycomb
turtle3 = turtle.Turtle()
turtle3.color("Purple")
turtle3.right(90)
turtle3.up()
turtle3.forward(37)
turtle3.down()
turtle3.right(90)
turtle3.up()
turtle3.forward(22)
turtle3.down()

for i in range (6):
  turtle3.forward(40)
  turtle3.right(60)

turtle3.left(180)

#turtle4 honeycomb
turtle4 = turtle.Turtle()
turtle4.color("Orange")
turtle4.up()
turtle4.forward(124)
turtle4.down()

for i in range (6):
  turtle4.forward(40)
  turtle4.left(60)

#turtle5 honeycomb
turtle5 = turtle.Turtle()
turtle5.color(color2)
turtle5.left(180)
turtle5.up()
turtle5.forward(84)
turtle5.down()

for i in range (6):
  turtle5.forward(40)
  turtle5.right(60)

turtle5.left(180)

#turtle6 honeycomb
turtle6 = turtle.Turtle()
turtle6.color("Green")
turtle6.up()
turtle6.forward(40)
turtle6.left(60)
turtle6.forward(43)
turtle6.right(60)
turtle6.down()

for i in range (6):
  turtle6.forward(40)
  turtle6.left(60)

#For output 1:
#Please choose a primary color: Red
#Please choose another primary color: Yellow

#For output 2:
#Please choose a primary color: Blue
#Please choose another primary color: Red
