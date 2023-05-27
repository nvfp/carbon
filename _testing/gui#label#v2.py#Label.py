import tkinter as tk

from carbon.gui.label.v2 import Label


root = tk.Tk()
root.attributes('-fullscreen', True)

mon_width = root.winfo_screenwidth()
mon_height = root.winfo_screenheight()

page = tk.Canvas(width=mon_width, height=mon_height, bg='#000', highlightthickness=0, borderwidth=0)
page.place(x=0, y=0)




x = 100
y = 100
r = 3
lbl = Label(x, y, 'MAIN')
page.create_oval(x-r, y-r, x+r, y+r, fill='#f00')


lbl = Label(text='next to MAIN').align(lbl)
lbl = Label(text='below').align(lbl, 'n', 's', 0, 0)
lbl = Label(text='below again').align(lbl, 'n', 's', 0, 15)
lbl = Label(text='TR corner to DL corner').align(lbl, 'n', 's', 0, 15)



root.bind('<Escape>', lambda e: root.destroy())
root.mainloop()