import tkinter,random
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()
druh=0

def semafor ():
    druh=random.randint(1,5)
    canvas.delete('all')

    if druh==1:
        canvas.create_oval(200,190,250,240,fill='red')
        canvas.create_oval(200,250,250,310,fill='orange')
    if druh==2:
        canvas.create_oval(200,320,260,380,fill='green')
    if druh==3:
        canvas.create_oval(200,190,250,240,fill='red')
        canvas.create_oval(200,250,250,310,fill='orange')
        canvas.create_oval(200,320,250,380,fill='green')
    if druh==4:
        canvas.create_oval(200,250,250,310,fill='orange')
    if druh==5:
        canvas.create_oval(200,190,250,240,fill='red')
        
        
        
    
    canvas.after(500,semafor)


semafor()

