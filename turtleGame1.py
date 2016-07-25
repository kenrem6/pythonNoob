#!/usr/bin/env python3
# -*- coding utf-8 -*-
"""
    Title: A simple Turtle demo
    Created: 25-07-16
    Authors: Jonas Solsvik

    Description:
         A turtle object is in many ways like any game object. It has many attributes which
          can be changed. Speed, color, shape, size, and much much more. It can also copy itself.
           Therefore the turtle-library can be used to create experimental and educational
            games. Bear in mind that the simplicity of the turtle library hurts its performance
             considerabily. Therefore is is seen as a stepping stone to other more powerful low-level
              libraries such as openGl, Vulkan and DirectX12
    -------------------------------------- Jonas -------------------- """

from turtle import Turtle, Screen

# --- Create objects---
screen = Screen()
tut1 = Turtle()
tut2 = Turtle()

# --- INIT turtles ---
tut1.speed(1)
tut1.penup()
tut1.shape("circle")
tut1.shapesize(5)
tut1.color("red")

tut2.speed(1)
tut2.penup()
tut2.shape("square")
tut2.shapesize(5)
tut2.color("blue")

# --- ACTION ---
tut1.forward(100)
tut2.backward(100)

screen.mainloop()
