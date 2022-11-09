import tkinter,random
canvas=tkinter.Canvas()
canvas.pack()

def text():
    x=random.randint(1,300)
    y=random.randint(1,300)
    farby=random.choice(('green','yelow','blue','red','brown','orange'))
    text = int(entry1.get())
    canvas.create_text(x,y,text=text,color=farby)
def zmaz(event):
    canvas.delete(all)
entry1=tkinter.Entry()
entry1.pack()
button=tkinter.Button(text='pis', command=text)
button.pack()
canvas.bind('<>Button-1',zmaz)
