import turtle
import math
import colorsys
import random

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor('black')
screen.title('Untuk Kesayanganku ❤️')


screen.tracer(15)  

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

def x(t):
    return 16 * math.sin(t) ** 3

def y(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(1, 4000):
    tx = x(i) * 18
    ty = y(i) * 18
    
    hue = 0.85 + (i / 15000)
    if hue > 1.0:
        hue -= 1.0
    c = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    
    t.pencolor(c)
    t.goto(tx, ty)
    t.goto(0, 0)

screen.update()

t.pensize(1)
for _ in range(50):
    t.penup()
    hx = random.randint(-420, 420)
    hy = random.randint(-320, 320)
    
    if hx**2 + hy**2 > 70000:
        t.goto(hx, hy)
        t.pendown()
        
        c = colorsys.hsv_to_rgb(0.85 + random.random()/8, 0.8, 1.0)
        t.color(c)
        
        t.begin_fill()
        t.setheading(0)
        t.left(140)
        t.forward(10)
        t.circle(-5, 200)
        t.setheading(60)
        t.circle(-5, 200)
        t.forward(10)
        t.end_fill()

screen.update()

t.penup()
t.goto(0, -15) 
t.color("#ff99cc")
t.write("I Love You", align="center", font=("Arial", 45, "bold"))

t.goto(0, -50)
t.color("white")
t.write("— always & forever —", align="center", font=("Arial", 16, "italic"))

screen.update()
turtle.done()
