from tkinter import *


def TextBox():
    root = Tk()
    frame = Frame(root)
    frame2 = Frame(root)
    
    ys = Scrollbar(frame)
    xs = Scrollbar(frame2)
    
    dsp = Text(frame, yscrollcommand = ys.set, xscrollcommand = xs.set)
    
    xs.config(orient = 'hor', command = dsp.xview)
    ys.config(orient = 'vert', command = dsp.yview)

    ys.pack(side = LEFT, expand = NO, fill = Y)
    dsp.pack(side = LEFT, expand = YES, fill = BOTH)
    frame.pack(side = TOP, expand = YES, fill = BOTH)
    frame2.pack(side = TOP, fill =X)

    Frame(frame2, width = 16).pack(side = LEFT)
    xs.pack(side = LEFT, expand = YES, fill = X)

    root.mainloop()

TextBox()

