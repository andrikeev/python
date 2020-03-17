from tkinter import *


def map_to_sausages(*args):
    width, height = args[0]
    color = args[1]
    sausages = args[2:]

    master = Tk()
    canvas = Canvas(master, width=width, height=height, background=color)
    canvas.pack()

    for sausage in sausages:
        x, y, color, height = sausage
        width = height * 3
        canvas.create_oval(x - width // 2, y - height // 2, x + width // 2, y + height // 2, fill=color)

    mainloop()


if __name__ == '__main__':
    map_to_sausages((3800, 2600), '#000000', (20, 100, '#ffffff', 10), (40, 40, '#00ffff', 30), (60, 120, '#ff0000', 20))
