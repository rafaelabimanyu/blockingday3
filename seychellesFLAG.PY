import turtle
from PIL import Image

def save_as_jpg ( canvas , filename ):
        canvas.postscript(file=f"{filename}.eps")
        img = Image.open(f"{filename}.eps")
        img.save(f"{filename}.jpg")
def drawRectangle (ttl , x, y, width, height):
    ttl . up ()
    ttl . goto (x , y)
    ttl . setheading (0)
    ttl . down ()
    for i in range (2) :
        ttl . forward (width)
        ttl . right (90)
        ttl . forward (height)
        ttl . right (90)
    ttl . up ()
def drawTriangle (ttl, x1, y1, x2, y2, x3, y3):
    ttl . penup ()
    ttl . goto (x1, y1)
    ttl . pendown ()
    ttl . goto (x2 , y2)
    ttl . goto (x3, y3)
    ttl . goto (y1, y1)
    ttl . penup ()    
def fillTriangle (ttl, x1, y1, x2, y2, x3, y3, color) :
    ttl.fillcolor (color)
    ttl.begin_fill()
    drawTriangle(ttl, x1, y1, x2, y2, x3, y3)
    ttl.end_fill()

turtle . setup (1500, 100, 0, 0)
myBlue = "#003882"
myYellow = "#FCD647"
myRed = "#D12421"
myGreen = "#007336"
myWhite = "#FFFFFF"

joe = turtle . Turtle()
joe.screen.colormode(255)
drawRectangle(joe, 0, 300, 600, 300)
joe.goto (0, 0)

fillTriangle(joe, 0, 0, 0, 300, 200, 300, myBlue)
fillTriangle(joe, 0, 0, 200, 300, 400, 300, myYellow)
fillTriangle(joe, 0, 0, 400, 300, 600, 300, myRed)
fillTriangle(joe, 0, 0, 600, 300, 600, 150, myWhite)
fillTriangle(joe, 0, 0, 600, 150, 600, 0, myGreen)
joe.hideturtle()
ts = turtle.getscreen()
tc = ts.getcanvas()

tc.postscript(file =" SeychellesFlag . eps ")
save_as_jpg (tc ," SeychellesFlag ")
turtle.done()