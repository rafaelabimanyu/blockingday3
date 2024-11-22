import turtle

def draw_rectangle(ttl, width, height, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(2):
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height)
        ttl.left(90)
    ttl.end_fill()

def draw_triangle(ttl, side, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(3):
        ttl.forward(side)
        ttl.left(120)
    ttl.end_fill()

def draw_trapezium(ttl, top_base, bottom_base, height, color):
    side = ((bottom_base - top_base) / 2)
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.forward(bottom_base)
    ttl.left(120)
    ttl.forward(height)
    ttl.left(60)
    ttl.forward(top_base)
    ttl.left(60)
    ttl.forward(height)
    ttl.left(120)
    ttl.end_fill()

def draw_parallelogram(ttl, base, side, angle, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.forward(base)
    ttl.left(180 - angle)
    ttl.forward(side)
    ttl.left(angle)
    ttl.forward(base)
    ttl.left(180 - angle)
    ttl.forward(side)
    ttl.left(angle)
    ttl.end_fill()

def draw_pentagon(ttl, side, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(5):
        ttl.forward(side)
        ttl.left(72)
    ttl.end_fill()

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("white")
ttl = turtle.Turtle()
ttl.speed(5)

# Draw shapes with colors
ttl.penup()
ttl.goto(-200, 100)
ttl.pendown()
ttl.write("Rectangle", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(-200, 50)
ttl.pendown()
draw_rectangle(ttl, 100, 50, "red")

ttl.penup()
ttl.goto(0, 100)
ttl.pendown()
ttl.write("Triangle", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(0, 50)
ttl.pendown()
draw_triangle(ttl, 100, "yellow")

ttl.penup()
ttl.goto(200, 100)
ttl.pendown()
ttl.write("Trapezium", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(200, 50)
ttl.pendown()
draw_trapezium(ttl, 60, 120, 50, "green")

ttl.penup()
ttl.goto(-200, -100)
ttl.pendown()
ttl.write("Parallelogram", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(-200, -150)
ttl.pendown()
draw_parallelogram(ttl, 100, 50, 60, "blue")

ttl.penup()
ttl.goto(0, -100)
ttl.pendown()
ttl.write("Pentagon", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(0, -150)
ttl.pendown()
draw_pentagon(ttl, 80, "purple")

ttl.hideturtle()
turtle.done()
