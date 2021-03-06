from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='800')
canvas.pack()

def drawkoch(x1, y1, x2, y2, num):
    if num == 1:
        canvas.create_line(x1, y1, x1+(x2-x1)/3, y1+(y2-y1)/3)
        canvas.create_line(x1+(x2-x1)/3, y1+(y2-y1)/3, x1+(x2-x1)/3+0.5*(x2-x1)/3+3**0.5*0.5*(y2-y1)/3, y1+(y2-y1)/3-3**0.5*0.5*(x2-x1)/3+0.5*(y2-y1)/3)
        canvas.create_line(x1+(x2-x1)/3+0.5*(x2-x1)/3+3**0.5*0.5*(y2-y1)/3, y1+(y2-y1)/3-3**0.5*0.5*(x2-x1)/3+0.5*(y2-y1)/3, x1+2*(x2-x1)/3, y1+2*(y2-y1)/3)
        canvas.create_line(x1+2*(x2-x1)/3, y1+2*(y2-y1)/3, x2, y2)
    else:
        drawkoch(x1, y1, x1+(x2-x1)/3, y1+(y2-y1)/3, num-1)
        drawkoch(x1+(x2-x1)/3, y1+(y2-y1)/3, x1+(x2-x1)/3+0.5*(x2-x1)/3+3**0.5*0.5*(y2-y1)/3, y1+(y2-y1)/3-3**0.5*0.5*(x2-x1)/3+0.5*(y2-y1)/3, num-1)
        drawkoch(x1+(x2-x1)/3+0.5*(x2-x1)/3+3**0.5*0.5*(y2-y1)/3, y1+(y2-y1)/3-3**0.5*0.5*(x2-x1)/3+0.5*(y2-y1)/3, x1+2*(x2-x1)/3, y1+2*(y2-y1)/3, num-1)
        drawkoch(x1+2*(x2-x1)/3, y1+2*(y2-y1)/3, x2, y2, num-1)

def drawkoch_snowflakes(x1, y1, x2, y2, num):
    drawkoch(x1, y1, x2, y2, num)
    drawkoch(x2, y2, x1+(x2-x1)/2, y1+(x2-x1)*3**0.5/2, num)
    drawkoch(x1+(x2-x1)/2, y1+(x2-x1)*3**0.5/2, x1, y1, num)

drawkoch_snowflakes(10, 200, 590, 200, 4)

root.mainloop()
