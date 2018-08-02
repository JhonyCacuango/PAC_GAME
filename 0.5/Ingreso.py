from tkinter import *
import os
import sys
from fileinput import close
from pygame import image
#crear y personalizar ventana
class Ingreso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('INGRESO DE NOMBRE')
        #self.ventana.geometry("300x150")#tamaño de la ventana ancho por alto
        self.ventana.config(bg='light goldenrod')  
        self.ventana.wm_attributes("-topmost", 1)
        
    def ingresonombre(self):
# parte de ingresar un nombre de jugador 
        self.nombre_label = Label(self.ventana,text="INGRESA TU NOMBRE:",bg='light goldenrod')#etiqueta
        self.nombre_label.grid(pady=5,row=0,column=0) #el espacio en blanco
        self.nombre_str = StringVar() 
        self.nombre_entry1 = Entry(self.ventana,textvariable=self.nombre_str)#caja de texto
        self.nombre_entry1.grid(padx=5,row=0,column=1)#Para posicionarlo la funcion grid(row,columns) que seria fila,columns.
        self.salir = Button(self.ventana,text="LISTO",width=50,bg='skyblue',command=self.ventana.destroy)
        self.salir.grid(padx=10,pady=10,row=2,column=0, columnspan=2)
        self.ventana.mainloop()

#parte de ingresar ldos nombres de jugadores
    def ingressodosjugadores(self):
        
        #self.ventana.geometry("350x150")
        self.nombre_label = Label(self.ventana,text="NOMBRE DEL PRIMER JUGADOR:",bg='light goldenrod')#etiqueta
        self.nombre_label.grid(pady=5,row=0,column=0) #el espacio en blanco
        self.nombre_str1 = StringVar() 
        self.nombre_entry = Entry(self.ventana,textvariable=self.nombre_str1)#caja de texto
        self.nombre_entry.grid(padx=5,row=0,column=1)
        self.last_label= Label(self.ventana,text="NOMBRE DEL SEGUNDO JUGADOR: ",bg='light goldenrod') #Label(ventana,text)
        self.last_label.grid(pady=5,row=1,column=0)
        self.last_str = StringVar()# StringVar()tendra el valor de lo escrito en la caja de texto
        self.last_entry = Entry(self.ventana,textvariable=self.last_str)
        self.last_entry.grid(padx=5,row=1,column=1)
        self.salir = Button(self.ventana,text="LISTO",width=50,bg='skyblue',command=self.ventana.destroy)
        self.salir.grid(padx=10,pady=10,row=2,column=0,columnspan=2)
        self.ventana.mainloop()
#parte de obtener los nombres
    def nombre(self):
        self.nombre=self.nombre_str.get()
        return str(self.nombre)
    def nombre1(self):
        self.nombre1=self.nombre_str1.get()
        return self.nombre1
    def nombre2(self):
        self.nombre2=self.last_str.get()
        return self.nombre2