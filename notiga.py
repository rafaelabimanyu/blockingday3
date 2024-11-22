import turtle

def draw_indonesia_flag(ttl, width, height):
    # Gambar bagian merah (bagian atas)
    ttl.penup()
    ttl.goto(-width / 2, height / 2)  # Posisi awal bagian merah
    ttl.pendown()
    ttl.fillcolor("red")
    ttl.begin_fill()
    ttl.setheading(0)  # Menghadap ke kanan
    for _ in range(2):
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height / 2)
        ttl.left(90)
    ttl.end_fill()

    # Gambar bagian putih (bagian bawah)
    ttl.penup()
    ttl.goto(-width / 2, 0)  # Posisi awal bagian putih
    ttl.pendown()
    ttl.fillcolor("white")
    ttl.begin_fill()
    ttl.setheading(0)  # Menghadap ke kanan
    for _ in range(2):
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height / 2)
        ttl.left(90)
    ttl.end_fill()

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("white")  # Latar belakang putih
ttl = turtle.Turtle()
ttl.speed(5)

# Gambar Bendera Indonesia (proporisi 2:1, misalnya lebar 400px dan tinggi 200px)
width = 400
height = 200

draw_indonesia_flag(ttl, width, height)

ttl.hideturtle()  # Sembunyikan kursor setelah menggambar
turtle.done()  # Menjaga jendela tetap terbuka
