from random import randint
from tkinter import *


def generate():
    
    limit, value = 255, lambda: randint(0, limit)
    rgb, color = [value(), value(), value()], []
    for i in range(len(rgb)):
        for _ in range(limit):
            if rgb[i] != limit:
                color.append("#" + "".join(["0{0:x}".format(j) if j < 16 else "{0:x}".format(j) for j in [int(k) for k in rgb]]))
                rgb[i] += 1
                
    canvas.configure(width=len(color))

    color.reverse()
    for l in range(len(color)):
        canvas.create_line(l, 0, l, 360, fill=(color[l]))

    button.configure(command=lambda: [canvas.delete('all'), generate()])


window = Tk()
window.title("Hue generator")
window.resizable(False, False)

button = Button(window, text="Generate", relief=RIDGE, command=generate)
button.pack(side=BOTTOM, anchor=S, fill=X, padx=2, pady=2)

canvas = Canvas(window, width=360, height=360, highlightthickness=0)
canvas.pack()

window.mainloop()
