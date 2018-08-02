from tkinter import *
import os
import sys
#crear y personalizar ventana
class Ingreso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('INGRESO DE NOMBRE')
        self.ventana.geometry("250x150")#tamaño de la ventana ancho por alto
        self.ventana.config(bg='gray')
        self.ventana.resizable(width=False, height=False)
    def ingresonombre(self):
# parte de ingresar un nombre de jugador 
        self.nombre_label = Label(ventana,text="INGRESA TU NOMBRE:",bg='gray')#etiqueta
        self.nombre_label.grid(row=2,column=1) #el espacio en blanco
        self.nombre_str = StringVar() 
        self.nombre_entry = Entry(ventana,textvariable=nombre_str)#caja de texto
        self.nombre_entry.grid(row=2,column=2)#Para posicionarlo la funcion grid(row,columns) que seria fila,columns.
        self.ventana.mainloop()

#parte de ingresar ldos nombres de jugadores
    def ingressodosjugadores(self):
        self.nombre_label = Label(ventana,text="NOMBRE DEL PRIMER JUGADOR:",bg='gray')#etiqueta
        self.nombre_label.grid(row=2,column=1) #el espacio en blanco
        if self.nombre_str!="":
            self.nombre_str1 = StringVar() 
            self.nombre_entry = Entry(ventana,textvariable=nombre_str1)#caja de texto
        else:
            self.nombre_str1=self.nombre_str
        self.nombre_entry.grid(row=2,column=2)
        self.last_label= Label(ventana,text="NOMBRE DEL SEGUNDO JUGADOR: ",bg='gray') #Label(ventana,text)
        self.last_label.grid(row=4,column=1)
        self.last_str = StringVar()# StringVar()tendra el valor de lo escrito en la caja de texto
        self.last_entry = Entry(ventana,textvariable=last_str)
        self.last_entry.grid(row=4,column=2)
        self.ventana.mainloop()
#parte de obtener los nombres
    def nombre(self):
        self.nombre1=self.nombre_str
        return self.nombre1
    def nombres(self):
        self.nombre1=self.nombre_str
        self.nombre2=self.nombre_str1
        return self.nombre1

#salir listo 
    def boton(self):
        self.salir = Button(ventana,text="FINALIZAR",bg='skyblue',command=quit)
        self.salir.grid(row=7,column=2)
        self.ventana.mainloop()

