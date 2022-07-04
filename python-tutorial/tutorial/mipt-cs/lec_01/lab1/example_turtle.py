import math
import turtle

turtle = turtle.Turtle()
turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('green')


# 1
def david():
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(30)
            turtle.left(360 / 3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.right(60)


# 2
def turtle_move(x):
    turtle.penup()
    turtle.backward(x)
    turtle.pendown()


# 4
def turtle_circle():
    for i1 in range(360):
        turtle.forward(1)
        turtle.left(1)


# 5
def turtle_more_quad():
    step = 0
    for q in range(5):
        for i in range(4):
            turtle.forward(50 + step * 2)
            turtle.left(360 / 4)
        step += 10
        turtle_move_step(10)


# 5.1
def turtle_move_step(x):
    turtle.penup()
    turtle.back(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.pendown()


# 6
def turtle_spider():
    n = 12
    while n >= 0:
        turtle.right(360 + 360 / 13)
        turtle.forward(75)
        turtle.stamp()
        turtle.back(75)
        n = n - 1


# 7
def turtle_spiral():
    n = 0.1
    for i in range(1000):
        turtle.left(7)
        turtle.forward(n)
        n += 0.01


# 8
def turtle_quad_plus():
    for i in range(100):
        turtle.forward(i + 1)
        turtle.left(90)


# 9
def turtle_nine():
    step = 30
    x = 1
    n = 3
    turtle.up()
    turtle.goto(step, 0)
    turtle.down()

    def polygon(x):
        while x <= n:
            turtle.left((180 - 360 / n) / 2)
            turtle.left(360 / n)
            turtle.forward(2 * step * math.sin(math.pi / n))
            x += 1
            turtle.right((180 - 360 / n) / 2)

    while n <= 11:
        polygon(x)
        n += 1
        step += 20
        turtle.up()
        turtle.goto(step, 0)
        turtle.down()


# 10
x, n = 10, 10
def turtle_flower(x):
    while True:
        # turtle_circle()
        turtle.circle(50)
        turtle.left(360 / n)
        # turtle.circle(-50)
        # turtle.left(360 / n)
        if (x < 0):
            break
        x -= 1

# 11
turtle.left(90)
def turtle_buterfly(n):
    turtle.circle(n)
    turtle.circle(-n)
    n+=10

for i in range(1, 100, 5):
    turtle_buterfly(10+i)

# 12
turtle.left(90)
x = 1
while x <= 6:
    turtle.circle(-50, 180, 100)
    turtle.circle(-10, 180, 100)
    x += 1

# 14
def stars(n):
    turtle.left(180 - (180 / n))
    turtle.forward(200)
x = 1
while x <= n:
    stars(n)
    x += 1


# turtle_flower(x)
# turtle_nine()
# turtle_spiral()
# turtle_more_quad()
# david()
# turtle_move(100)
# turtle_circle()

# turtle.hideturtle()
