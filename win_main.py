from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np
from matplotlib import style
from funciones import principal
import re
win = Tk()
win.geometry('800x400')
win.title('Grupo 07: KD-Tree caso: Iris')

def calcular():
    sepalo_longitud = float(txt2.get())
    sepalo_ancho = float(txt3.get())
    petalo_longitud = float(txt4.get())
    petalo_ancho = float(txt5.get())
    prueba = int(txt6.get())
    principal(sepalo_longitud,sepalo_ancho,petalo_longitud,petalo_ancho,prueba)
#controles
lbl1 = Label(win, text='Ingrese las características')
lbl1.pack()
lbl1.place(x=5,y=0)

lbl2 = Label(win, text='Longitud del sépalo :')
lbl2.pack()
lbl2.place(x=5,y=20)
txt2 = Entry(win,bg='pink')
txt2.insert(0,'1.0')
txt2.pack()
txt2.place(x=120, y=20, width=40)

lbl3 = Label(win, text='Ancho del sépalo :')
lbl3.pack()
lbl3.place(x=180,y=20)
txt3 = Entry(win,bg='pink')
txt3.insert(0,'2.0')
txt3.pack()
txt3.place(x=282, y=20, width=40)

lbl4 = Label(win, text='Longitud del pétalo :')
lbl4.pack()
lbl4.place(x=5,y=50)
txt4 = Entry(win,bg='bisque')
txt4.insert(0,'3.0')
txt4.pack()
txt4.place(x=120, y=50, width=40)

lbl5 = Label(win, text='Ancho del pétalo :')
lbl5.pack()
lbl5.place(x=180,y=50)
txt5 = Entry(win,bg='bisque')
txt5.insert(0,'0.0')
txt5.pack()
txt5.place(x=282, y=50, width=40)

lbl6 = Label(win, text='Prueba ? :')
lbl6.pack()
lbl6.place(x=380,y=50)
txt6 = Entry(win,bg='azure')
txt6.insert(0,'0')
txt6.pack()
txt6.place(x=482, y=50, width=40)


btn1= Button(win,text='Calcular consulta', bg='lightgrey', command= calcular)
btn1.pack()
btn1.place(x=550,y=20, width= 150, height=50)

canvas = Canvas(win,width=1600,height=1000, highlightbackground='black')
canvas.pack(pady=80,padx=20)

win.mainloop()