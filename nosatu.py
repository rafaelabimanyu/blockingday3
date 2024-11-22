import turtle

def draw_rectangle(ttl, width, height):
    for _ in range(2):
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height)
        ttl.left(90)

def draw_triangle(ttl, side):
    for _ in range(3):
        ttl.forward(side)
        ttl.left(120)

def draw_trapezium(ttl, top_base, bottom_base, height):
    side = ((bottom_base - top_base) / 2)
    ttl.forward(bottom_base)
    ttl.left(120)
    ttl.forward(height)
    ttl.left(60)
    ttl.forward(top_base)
    ttl.left(60)
    ttl.forward(height)
    ttl.left(120)

def draw_parallelogram(ttl, base, side, angle):
    ttl.forward(base)
    ttl.left(180 - angle)
    ttl.forward(side)
    ttl.left(angle)
    ttl.forward(base)
    ttl.left(180 - angle)
    ttl.forward(side)
    ttl.left(angle)

def draw_rhombus(ttl, diagonal1, diagonal2):
    half_diag1 = diagonal1 / 2
    half_diag2 = diagonal2 / 2
    ttl.left(45)
    ttl.forward(half_diag1)
    ttl.left(90)
    ttl.forward(half_diag2)
    ttl.left(90)
    ttl.forward(half_diag1)
    ttl.left(90)
    ttl.forward(half_diag2)
    ttl.left(90)

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("white")
ttl = turtle.Turtle()
ttl.speed(5)

# Draw shapes
ttl.penup()
ttl.goto(-200, 100)
ttl.pendown()
ttl.write("Rectangle", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(-200, 50)
ttl.pendown()
draw_rectangle(ttl, 100, 50)

ttl.penup()
ttl.goto(0, 100)
ttl.pendown()
ttl.write("Triangle", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(0, 50)
ttl.pendown()
draw_triangle(ttl, 100)

ttl.penup()
ttl.goto(200, 100)
ttl.pendown()
ttl.write("Trapezium", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(200, 50)
ttl.pendown()
draw_trapezium(ttl, 60, 120, 50)

ttl.penup()
ttl.goto(-200, -100)
ttl.pendown()
ttl.write("Parallelogram", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(-200, -150)
ttl.pendown()
draw_parallelogram(ttl, 100, 50, 60)

ttl.penup()
ttl.goto(0, -100)
ttl.pendown()
ttl.write("Rhombus", align="center", font=("Arial", 12, "bold"))
ttl.penup()
ttl.goto(0, -150)
ttl.pendown()
draw_rhombus(ttl, 100, 60)

ttl.hideturtle()
turtle.done()
