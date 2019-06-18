import graphics as gr

win = gr.GraphWin("Russ game", 1000, 1000)
alpha = 0.05


def fractal_rec(a, b, c, d, deep=200):
    if deep < 1:
        input()
        win.close()
        return
    for m, n in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*m), gr.Point(*n)).draw(win)
    a1 = (a[0] * (1 - alpha) + b[0] * alpha, a[1] * (1 - alpha) + b[1] * alpha)
    b1 = (b[0] * (1 - alpha) + c[0] * alpha, b[1] * (1 - alpha) + c[1] * alpha)
    c1 = (c[0] * (1 - alpha) + d[0] * alpha, c[1] * (1 - alpha) + d[1] * alpha)
    d1 = (d[0] * (1 - alpha) + a[0] * alpha, d[1] * (1 - alpha) + a[1] * alpha)
    fractal_rec(a1, b1, c1, d1, deep-1)


fractal_rec((50, 50), (950, 50), (950, 950), (50, 950))

