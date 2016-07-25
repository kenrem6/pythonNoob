#!/usr/bin/env python3
# -*- coding utf-8 -*-

from turtle import Turtle, Screen

# --- Create objects---
screen = Screen()
tut1 = Turtle()
tut2 = Turtle()

# --- INIT turtles ---
tut1.penup()
tut1.shape("circle")
tut1.shapesize(5)
tut1.color("red")

tut2.penup()
tut2.shape("square")
tut2.shapesize(5)
tut2.color("blue")

# --- ACTION ---
tut1.forward(100)
tut2.backward(100)

screen.mainloop()
