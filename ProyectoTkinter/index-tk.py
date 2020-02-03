from tkinter import ttk
from tkinter import *

import sqlite3

class Paciente:
     dataname="database-tk.db"
     def __init__(self , window):
         self.wind=window
         self.wind.title("Products Application")

         

         # frame=Frame(width=500,height=400)
         frame=LabelFrame(self.wind,text="Registre un nuevo paciente")
         frame.grid(row=0,column=0,columnspan=3,pady=20)#metodo grid para pocicionar elementos
         window.config(bg="light pink")
         #frame.pack()
         frame.config(bg="NavajoWhite4")
         window.config(bd=45)
         window.config(relief="groove")
         frame.config(cursor="hand2")
         
         

         Label(frame,text="Nombre: ").grid(row=1,column=0) #dentro del frame
         self.Nombre=Entry(frame) #crea un input
         self.Nombre.grid(row=1,column=1)
         self.Nombre.focus()

         Label(frame,text="DNI: ").grid(row=2,column=0)
         self.DNI=Entry(frame)
         self.DNI.grid(row=2,column=1)

         ttk.Button(frame,text="Guardar", command= self.agregar_paciente).grid(row=3,columnspan=2,sticky=W+E)
         
         self.message=Label(text='',fg='red')
         self.message.grid(row=3, column= 0, columnspan= 2, sticky= W + E)

         self.tree=ttk.Treeview(height=10,columns=2)
         self.tree.grid(row=4,column=0, columnspan=2)
         self.tree.heading("#0",text="Nombre",anchor=CENTER)
         self.tree.heading("#1",text="DNI",anchor=CENTER)
        
         ttk.Button(text='Eliminar', command= self.eliminar_paciente).grid(row= 5, column= 0, sticky= W + E)
         ttk.Button(text='Editar', command= self.editar_paciente).grid(row= 5, column= 1, sticky= W + E)

         self.listar_pacientes()
        
     def run_query(self,query,parametros=()):
        with sqlite3.connect(self.dataname) as conn:
             cursor=conn.cursor()
             result=cursor.execute(query,parametros)
             conn.commit()
        return result    

     def listar_pacientes(self):
         records= self.tree.get_children()
         for element in records:
             self.tree.delete(element)
         query='SELECT *FROM Paciente ORDER BY Nombre DESC'
         db_rows=self.run_query(query)
         for row in db_rows:
             self.tree.insert("",0,text=row[1],values=row[2])
     def validation(self):
         return len(self.Nombre.get()) !=0 and len(self.DNI.get()) !=0 
     
     def agregar_paciente(self):
         if self.validation():
             query='INSERT INTO Paciente VALUES(NULL,?,?)'
             parametros=(self.Nombre.get(), self.DNI.get())
             self.run_query(query, parametros)
             self.message['text']= 'Paciente {} guardado'.format(self.Nombre.get())
             self.Nombre.delete(0, END)
             self.DNI.delete(0, END)
         else:
             self.message['text']="Nombre y dni requeridos"
         self.listar_pacientes()
     
     def eliminar_paciente(self):
          self.message['text']= '' #Limpio la variable
          try:
             self.tree.item(self.tree.selection())['text'][0]
          except IndexError as e:
             self.message['text']= 'Seleccionar'
             return 
          self.message['text']= ''
          Nombre= self.tree.item(self.tree.selection())['text']
          query= 'DELETE FROM Paciente WHERE Nombre=?'
          self.run_query(query, (Nombre, ))
          self.message['text']= 'Registro {} borrado'.format(Nombre)
          self.listar_pacientes()  
          # Para actualizar la lista

     def editar_paciente(self):
         self.message['text']= ''
         try:
             self.tree.item(self.tree.selection())['text'][0]
         except IndexError as e:
             self.message['text']= 'Seleccionar'
             return
         Nombre= self.tree.item(self.tree.selection())['text']
        # DNI= self.tree.item(self.tree.selection())['values'][0]
         self.edit_wind=Toplevel()
         self.edit_wind.title= 'Editar'
 
         #OldNombre
         Label(self.edit_wind, text= 'Nombre Actual').grid(row=0, column=1)
         Entry(self.edit_wind, textvariable= StringVar(self.edit_wind, value= Nombre), state= 'readonly').grid(row=0, column=2)

         #NewNombre
         Label(self.edit_wind, text= 'Nuevo nombre').grid(row= 1, column=1) 
         nuevo_nombre= Entry(self.edit_wind)
         nuevo_nombre.grid(row= 1 ,column= 2)

         Button(self.edit_wind, text= 'Guardar', command= lambda: self.edit_records(nuevo_nombre.get(), Nombre)).grid(row=4, column=2, sticky= W)
        

     def edit_records(self, nuevo_nombre,Nombre):
         query= 'UPDATE Paciente SET Nombre= ? WHERE Nombre=? '
         parametros= (nuevo_nombre, Nombre)
         self.run_query(query, parametros)
         self.edit_wind.destroy()
         self.message['text']= 'Record {} guardados'.format(Nombre)
         self.listar_pacientes()






if __name__=="__main__":
        window=Tk()
        application=Paciente(window)
        window.iconbitmap("descarga.ico")
        window.mainloop()
        


        

   

