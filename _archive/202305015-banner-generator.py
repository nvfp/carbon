import random
import tkinter as tk

from carbon.color import interpolate_color


root = tk.Tk()
root.attributes('-fullscreen', True)

mon_width = root.winfo_screenwidth()
mon_height = root.winfo_screenheight()

page = tk.Canvas(width=mon_width, height=mon_height, bg='#000', highlightthickness=0, borderwidth=0)
page.place(x=0, y=0)


POSITIVE = '#00bfff'
NEGATIVE = '#ff6961'

random.seed(0)

C = [
    (0, 0),
    (1, 0),
    (2, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 3),
    (2, 3),
]
A = [
    (1, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (2, 1),
    (0, 3),
    (2, 3),
]
R = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 1),
]
B = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 1),
    (1, 3),
    (2, 3),
    (2, 2),
    (0, -1),
]
O = [
    (0, 2),
    (2, 2),
    (1, 1),
    (1, 3),
    (1, 2),
]
N = [
    (1, 1),
    (0, 1),
    (0, 2),
    (0, 3),
    (2, 2),
    (2, 3),
]

SHIFT_X = 3
SHIFT_Y = 5
CARBON = []
for i in [C, A, R, B, O, N]:

    for x, y in i:
        CARBON.append((x+SHIFT_X, y+SHIFT_Y))
    SHIFT_X += max([p[0] for p in i]) - min([p[0] for p in i]) + 2

TL_X = -10
TL_Y = -15
GAP_X = 50
GAP_Y = 55

RAD = 19

OFFSET = 5

prev = []
NX = 30
NY = 16
for x in range(NX):
    now = []
    for y in range(NY):

        X = TL_X + GAP_X*x + random.randint(-OFFSET, OFFSET)
        Y = TL_Y + GAP_Y*y + random.randint(-OFFSET, OFFSET)

        R = (RAD + random.randint(0, 7))/2
        
        COLOR = random.choice([POSITIVE, NEGATIVE])
        k = random.uniform(0.03, 0.45)
        color = interpolate_color('#000000', COLOR, k)

        now.append((X, Y, k))

        W = 0
        if (x, y) in CARBON:
            color = '#ffc107'
            W = 0
            R += 9
        
        page.create_oval(
            X-R, Y-R,
            X+R, Y+R,
            fill=color, outline='#888', width=W
        )

        if x > 0:
            for yy in range(NY):
                if random.random() < 0.2:
                    x1, y1, v = prev[yy]
                    page.create_line(
                        x1, y1, X, Y,
                        fill=interpolate_color('#000000', '#ffffff', random.uniform(0.04, 0.2)),
                        width=1, tags='weights'
                    )
    prev = now

page.tag_lower('weights')


root.bind('<Escape>', lambda e: root.destroy())
root.mainloop()