import turtle

def draw_bar(tess,a):
    """draw the graph"""
    tess.begin_fill()
    tess.left(90)
    tess.forward(a)
    tess.right(90)
    tess.forward(40)
    tess.right(90)
    tess.forward(a)
    tess.left(90)
    tess.end_fill()
    tess.forward(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")


tess = turtle.Turtle()
tess.color("blue","red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess,a)

wn.mainloop()

