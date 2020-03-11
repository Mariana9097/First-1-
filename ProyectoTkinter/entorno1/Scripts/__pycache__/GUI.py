from tkinter import messagebox
from tkinter import ttk
from tkinter import *

import sqlite3

ventana= Tk()
ventana.title("Centro Medico")
ventana.config(width= 600, height= 500)
#ventana.geometry("700x600+100+100")


color_bg= "light blue"
photo = PhotoImage(file = "fondo-azul-ondas-electrocardiograma.gif")

frame= LabelFrame(ventana,text="Pacientes",font=("Verdana",24), cursor="hand2" )
frame.config(width= 600, height=500, relief= "groove" , bd=25)
frame.grid(row=0, column=0, columnspan=5,padx=10, pady=10)
frame.pack(fill='both', expand=1)
frame.pack(side=RIGHT)

Label(ventana, image= photo).pack()


Label(frame, text="Nombre:", bg=color_bg).grid(row=1, column=1)
Entry(frame).grid(row=1, column=2)

Label(frame, text="DNI:", bg=color_bg).grid(row=2, column=1)
Entry(frame).grid(row=2, column=2)

Label(frame, text="Obra Social:",bg=color_bg).grid(row=3, column=1)
combo =ttk.Combobox(frame)
combo.grid(row=3, column=2)

Label(frame, text="Numero de Obra",bg=color_bg).grid(row=4, column=1)
Entry(frame).grid(row=4, column=2)

Label(frame, text="Telefono:", bg=color_bg).grid(row=5, column=1)
Entry(frame).grid(row=5, column=2)

Label(frame, text="Domicilio:", bg=color_bg).grid(row=6, column=1)
Entry(frame).grid(row=6, column=2)



def Guardar():
     messagebox.askyesno(message="¿Desea guardar?", title="Se guardó %")
     #query='INSERT INTO'

#def Eliminar(self):

#def Editar():

boton_guardar= ttk.Button(frame, text="Guardar", command=Guardar).grid(row=8, column=4)






ventana.mainloop()
