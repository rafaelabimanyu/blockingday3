import turtle

def fibonacci_tree(ttl, length, angle, depth):
    if depth == 0:
        return
    
    ttl.forward(length)
    ttl.left(angle)
    
    fibonacci_tree(ttl, length * 0.8, angle, depth - 1)
    
    ttl.right(2 * angle)
    
    fibonacci_tree(ttl, length * 0.8, angle, depth - 1)
    
    ttl.left(angle)
    ttl.backward(length)

# Setup layar dan turtle
screen = turtle.Screen()
screen.bgcolor("white")  # Latar belakang putih
ttl = turtle.Turtle()
ttl.speed(10)  # Kecepatan menggambar turtle
ttl.left(90)  # Arahkan turtle ke atas

# Atur posisi awal turtle
ttl.penup()
ttl.backward(100)
ttl.pendown()

# Tentukan panjang awal cabang, sudut, dan kedalaman rekursi
initial_length = 100  # Panjang awal cabang
angle = 30  # Sudut percabangan
depth = 10  # Kedalaman rekursi

# Gambar Fibonacci Tree
fibonacci_tree(ttl, initial_length, angle, depth)

ttl.hideturtle()
turtle.done()
