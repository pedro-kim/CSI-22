import turtle

s = turtle.getscreen()

tess = turtle.Turtle()


def draw_poly(t, n, sz):
    int_angle = (n - 2) * 180 / n
    for i in range(n):
        t.forward(sz)
        t.left(180 - int_angle)


draw_poly(tess, 8, 50)
