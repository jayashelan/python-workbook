import turtle

def draw_multicolor_square(t, sz):
    """Make turtle t draww a multi-color square of sz."""
    # for i in ["red","purple","hotpink","blue"]:
    #     t.color(i)
    #     t.forward(sz)
    #     t.left(90)
    draw_rectangle(t, sz, sz)


def draw_rectangle(t, w, h):
    """Get turtl t to draw a rectangle of width and height h"""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)


def make_window(colr,title):
    """
    Setup up the window with the given background color and title
    Returns new window
    """

    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(title)
    return w

def make_turtle(colr,sz):
    """
    setup up a turtle with the given color and pensize.
    Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen","Tess and Alex dancing ")
tess = make_turtle("hotpink",5)
draw_rectangle(tess,20,20)
wn.mainloop()
