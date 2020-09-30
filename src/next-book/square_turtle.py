import turtle

def draw_square(t,sz):
    """Make turtle t to square of size sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)



wm = turtle.Screen()
wm.bgcolor("lightgreen")
wm.title("Alex meets a function")

alex = turtle.Turtle()
draw_square(alex,50)
wm.mainloop()