import turtle

# ფუნქცია სახლის დახაზვისთვის
def draw_house():
    # სახლი
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.end_fill()

    # კედელი
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(141.42)
    turtle.setheading(0)
    turtle.forward(100)
    turtle.setheading(-45)
    turtle.forward(141.42)

    # გაშიფვრა
    turtle.penup()
    turtle.goto(-50, -100)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)

    # სტრიშარი
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.goto(0, 0)
    turtle.goto(100, -100)

# ფუნქცია ვარსკვლავების დახაზვისთვის
def draw_star():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)

# სამყაროს დახაზვა
turtle.speed(0)
turtle.bgcolor("skyblue")

# სახლების დახაზვა
draw_house()

# ეზოს დახაზვა
turtle.penup()
turtle.goto(-300, -200)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
turtle.end_fill()

# მზის დახაზვა
turtle.penup()
turtle.goto(250, 200)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# ვარსკვლავების დახაზვა
turtle.penup()
turtle.goto(250, 200)
turtle.pendown()
turtle.color("white")
for _ in range(5):
    turtle.begin_fill()
    draw_star()
    turtle.end_fill()
    turtle.right(144)

# ფანჯრების დახაზვა
turtle.penup()
turtle.goto(-400, -200)
turtle.pendown()
turtle.color("brown")
turtle.forward(800)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(400)
turtle.hideturtle()

# turtle-ს ფანჯარის დასამთავრებლად ელოდება
turtle.done()