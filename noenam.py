import turtle
import math

# Fungsi menggambar lingkaran dengan warna
def draw_circle(radius, color, border_color="black"):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()
    # Tambahkan border jika diperlukan
    if border_color:
        turtle.color(border_color)
        turtle.penup()
        turtle.goto(0, -radius)
        turtle.pendown()
        turtle.circle(radius)

# Fungsi menulis teks melingkar
def write_text_circle(text, radius, offset_angle=0, font_size=10):
    turtle.penup()
    for i, char in enumerate(text):
        angle = offset_angle + (i / len(text)) * 360
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        turtle.goto(x, y)
        turtle.setheading(angle + 90)
        turtle.write(char, align="center", font=("Arial", font_size, "bold"))

# Fungsi menggambar tangan
def draw_hand():
    # Telapak tangan
    turtle.penup()
    turtle.goto(-40, -50)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.goto(40, -50)  # Garis bawah
    turtle.goto(40, 50)  # Sisi kanan telapak
    turtle.goto(20, 50)  # Pangkal jari kanan
    turtle.goto(20, 100)  # Jari kanan
    turtle.goto(10, 100)  # Ujung kanan
    turtle.goto(10, 120)  # Ujung atas
    turtle.goto(-10, 120)  # Ujung kiri
    turtle.goto(-10, 100)  # Jari kiri
    turtle.goto(-20, 100)  # Pangkal kiri
    turtle.goto(-20, 50)  # Telapak kiri
    turtle.goto(-40, 50)  # Sisi kiri telapak
    turtle.goto(-40, -50)  # Kembali ke awal
    turtle.end_fill()

# Fungsi menggambar tombol kecil
def draw_button():
    turtle.penup()
    turtle.goto(0, 120)  # Posisi tombol di atas jari
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(15)  # Tombol kecil
    turtle.end_fill()

# Setup layar
turtle.setup(800, 800)
turtle.speed(10)
turtle.hideturtle()
turtle.bgcolor("white")

# 1. Lingkaran luar (putih dengan border hitam)
draw_circle(200, "white")

# 2. Lingkaran dalam (biru)
draw_circle(150, "blue")

# 3. Teks melingkar
write_text_circle("SEKOLAH MENENGAH KEJURUAN", 180, 90, font_size=10)  # Teks atas
write_text_circle("PRESTASI PRIMA", 180, -90, font_size=10)  # Teks bawah

# 4. Gambar tangan
draw_hand()

# 5. Tombol kecil di atas jari
draw_button()

# Selesai
turtle.done()
