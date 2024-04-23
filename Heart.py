import turtle

pen = turtle.Turtle()
turtle.title("Heart Shape")
pen.speed(1)

screen = turtle.Screen()
screen.bgcolor("black")


# def curve():
#     for i in range(99):
#         pen.right(2)
#         pen.forward(3)


def heart():
    pen.color("dark red")
    pen.begin_fill()
    pen.fillcolor("red")
    pen.left(140)
    pen.forward(180)
    # curve()
    pen.circle(-90, 200)
    pen.left(120)
    # curve()
    pen.circle(-90, 200)
    pen.forward(177)
    pen.end_fill()
    pen.hideturtle()


def txt():
    pen.up()
    pen.setpos(-60, 140)
    pen.down()
    pen.color("dark red")
    pen.write("Kocham cię!!!", font=("Verdana", 12, "bold"))


heart()

txt()

screen.exitonclick()
