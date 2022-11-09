import tkinter
from random import *
canvas=tkinter.Canvas(width=600,height=600)
canvas.pack()
canvas.create_rectangle(0,300,600,600,fill='blue')
def lodicka(x,y):
    x=0
    y=0

    canvas.create_oval(x+5,y+5,x+10,y+10)
    canvas.create_rectangle(x+15,y+15,x+20,y+20)
    
def balon(x,y):
    x=0
    y=0
    canvas.create_rectangle(x+5,y+5,x+20,y+20)


def button1_lodicka():
    300<x<600 or 300<y<600
        
def button3_balon():
    0<x<300 or  0<y<300 
    
canvas.bind('<Button-1>',lodicka)
canvas.bind('<Button-3>',balon)
