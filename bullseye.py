from turtle import *

screen = Screen()
screen.bgcolor("white") 

# Set up the turtle
penup()
goto(0, -50) 
pendown()

# Define the colors for the bullseye
colors = ["black", "white", "black", "white", "black", "white", "black", "white", "red", "white", "black"]

# Draw concentric circles
radius = 120
for color_name in colors:
    penup()
    goto(0, -radius) 
    pendown()
    color(color_name)  # Set the color
    circle(radius) 
    radius -= 10  # Decrease the radius for the next circle

# Draw horizontal and vertical lines intersecting in the middle
penup()
goto(-220, 0)  
pendown()
color("black")
forward(480)
penup()
goto(0, 150)  
pendown()
right(90)
forward(300)  

hideturtle()
done() 
