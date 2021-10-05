# ask the user how many sides the spiral should have
# ask for their name
# draw a spiral that writes their name in the correct number of spiral sides
# and colors
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green",
          "orange", "purple", "white", "gray"]
sides = int(turtle.numinput("Number of sides",
            "How many sides do you want (1-8)?", 4, 1, 8))
your_name = turtle.textinput("Enter your name", "What is your name?")
for x in range(360):
    t.pencolor(colors[x % sides])
    t.penup()
    t.forward(x*3 / sides-1)
    t.pendown()
    t.write(your_name, font=("Arial", int((x+sides)/sides), "bold"))
    t.left(360 / sides + 1)
    t.width(x*sides/200)
