import turtle
import math
import random


# Written by Johnson Nguyen
# This was one of the first code I've ever written assigned from one of my Labs at the University of Minnesota
def race():
  #initializing 3 turtle objects
  a = turtle.Turtle()
  b = turtle.Turtle()
  c = turtle.Turtle()
  #Defining the shape of the objects
  a.shape("Turtle")
  b.shape("Turtle")
  c.shape("Turtle")
  #Change coordinate System
  turtle.setworldcoordinates(0,0,1000,1000)
  #Sets the color of the turtles
  a.pencolor("green")
  b.pencolor("red")
  c.pencolor("yellow")
  
