import tkinter
canvas=tkinter.Canvas()
canvas.pack()
def ziak(x,y):
    canvas.create_rectangle(x-10,y-10,x+10,y+10)




entry = tkinter.Entry()
entry.pack()
canvas.bind('<Button-1>',ziak)
