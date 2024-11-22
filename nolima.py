import turtle

def draw_flower_pattern():
    # Setup layar dan turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(2)
    
    # Warna untuk pola
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]

    # Gambar pola
    for i in range(360):
        pen.color(colors[i % len(colors)])  # Ganti warna secara berulang
        pen.forward(i * 2)                 # Panjang garis
        pen.right(59)                      # Sudut
        pen.forward(i * 2)
        pen.penup()
        pen.goto(0, 0)                     # Kembali ke titik tengah
        pen.pendown()

    # Selesai
    pen.hideturtle()
    screen.mainloop()

# Panggil fungsi
draw_flower_pattern()
