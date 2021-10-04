import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = eval(input("enter a number of sides between 2 and 7:"))
colors = ["red", "yellow", "blue", "orange",
          "green", "purple", "magenta", "brown"]
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x*3/sides + x)
    t.left(360/sides + 1)
    t.left(90)
    t.width(x*sides/200)
