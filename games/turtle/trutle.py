import time
import turtle
from turtle import Turtle
from random import randint
import ctypes
import subprocess
import threading
window = turtle.Screen()
window.title("TURTLE RACE")
turtle.speed(0)
turtle.penup()
turtle.setpos(-190, 200)
turtle.write("TURTLE RACE", font=("Arial", 40, "bold"))
turtle.penup()

turtle.setpos(-400, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

score = 0
stamp_size = 20
square_size = 15
finish_line = 290

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()
turtle.setheading(90)
    
for i in range(10):
    turtle.setpos(finish_line, (150 -(i * square_size * 2)))
    turtle.stamp()
    
for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) -(j * square_size * 2)))
    turtle.stamp()

for e in range(10):
    turtle.setpos(finish_line - square_size , ((150 - square_size) -(e * square_size * 2)))
    turtle.stamp()
    
turtle.hideturtle()


turtle1 = Turtle()
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,140)
turtle1.pendown()

for turn in range(10):
  turtle1.right(36)

turtle2 = Turtle()
turtle2.color("green")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,90)
turtle2.pendown()

for turn in range(10):
  turtle2.left(36)

turtle3 = Turtle()
turtle3.color("pink")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,40)
turtle3.pendown()
turtle3.speed(10)

for turn in range(10):
  turtle3.right(36)

turtle4 = Turtle()
turtle4.color("red")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-10)
turtle4.pendown()

for turn in range(10):
  turtle4.right(36)

turtle5 = Turtle()
turtle5.color("blue")
turtle5.shape("turtle")
turtle5.penup()
turtle5.goto(-250,-60)
turtle5.pendown()

for turn in range(10):
  turtle5.right(36)

turtle6 = Turtle()
turtle6.color("orange")
turtle6.shape("turtle")
turtle6.penup()
turtle6.goto(-250,-110)
turtle6.pendown()

for turn in range(10):
  turtle6.right(36)


red_circle_1 = turtle.Turtle()
red_circle_1.speed(1)
red_circle_1.up()
red_circle_1.goto(0,120)
red_circle_1.color("red")
red_circle_1.shape("circle")


red_circle_2 = turtle.Turtle()
red_circle_2.speed(1)
red_circle_2.up()
red_circle_2.goto(0,90)
red_circle_2.color("red")
red_circle_2.shape("circle")


green_circle_1 = turtle.Turtle()
green_circle_1.speed(1)
green_circle_1.up()
green_circle_1.goto(0,60)
green_circle_1.color("green")
green_circle_1.shape("circle")
green_circle_1.pensize(100)

red_circle_1.ht()
red_circle_2.ht()
green_circle_1.ht()


for i in range(145):
    turtle1.forward(randint(1,6))
    turtle2.forward(randint(1,6))
    turtle3.forward(randint(1,6))
    turtle4.forward(randint(1,6))
    turtle5.forward(randint(1,6))
    turtle6.forward(randint(1,6))

turtle.setpos(-140, -180)
turtle.write("Game Over", font=("italic", 40, "bold"))    