from tkinter import Tk, Label, Button, Entry

def miFuncion():
    print("Este mensaje es del boton")


ventana = Tk()
ventana.title("Algoritmo KD Tree Caso : IRIS")
ventana.geometry("800x400")
#ventana.mainloop()

lbl_Pregunta = Label(ventana,text="    Ingrese las medidas en cm.")
lbl_Pregunta.place(x= 0, y=10, width=300, height=30)
#lbl_Pregunta.pack()

lbl_sepalo_longitud = Label(ventana,text="Ingrese la longitud del Sepalo :")
lbl_sepalo_longitud.place(x=10, y= 30, width=250,height=30)
txt_Longitud_sepalo = Entry(ventana,bg='pink')
txt_Longitud_sepalo.place(x=10,y=50, width=100, height=30)
lbl_sepalo_ancho = Label(ventana,text="Ingrese el ancho del Sépalo :")
lbl_sepalo_ancho.pack(padx=10,pady=60,ipadx=100,ipady=30)
lbl_petalo_longitud = Label(ventana,text="Ingrese la longitud del petalo :")
lbl_petalo_longitud.pack()
lbl_petalo_ancho = Label(ventana,text="Ingrese el ancho del petalo :")
#lbl.config(bg = "gray")
lbl_petalo_ancho.pack()

btn = Button(ventana, text="Calcular", command = miFuncion)
btn.config(fg="red", bg = "blue")
#btn["fg"]="red"
#btn["bg"]="yellow"
btn.pack()


ventana.mainloop()