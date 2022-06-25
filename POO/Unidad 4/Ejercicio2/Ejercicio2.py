from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Aplicacion(tk.Tk):
    __precioSinIva=None
    __precioConIva=None
    __valorIVA = None

    def __init__(self):
        super().__init__()
        self.title("Calculo de IVA")
        self.__precioSinIva = StringVar()
        self.__precioConIva = StringVar()
        self.__valorIVA = StringVar()
        self.radioValue= IntVar()

        tk.Label(
            self, text="Precio sin IVA: ", 
        ).grid(column=0, row=0,sticky=W)

        self.precioEntry = tk.Entry(self, textvariable=self.__precioSinIva,width=30)
        self.precioEntry.grid(column=1, row=0 , columnspan=4, sticky=W)
        
        tk.Radiobutton(self, text='IVA 21 %', value=0, command=self.cambiarIVA,variable=self.radioValue).grid(row=2, column=0, columnspan=1, sticky='w')

        tk.Radiobutton(self, text='IVA 10.5 %', value=1,command=self.cambiarIVA, variable=self.radioValue).grid(row =3, column=0, columnspan=1, sticky='w')

        tk.Label(
            self, text="IVA: ", 
        ).grid(column=0, row=4,sticky=W)

        tk.Label(
            self, textvariable= self.__valorIVA, 
        ).grid(column=1, row=4,sticky=W)
        
        tk.Label(
            self, text="Precio con IVA: ", 
        ).grid(column=0, row=5,sticky=W)

        tk.Label(
            self, textvariable= self.__precioConIva, 
        ).grid(column=1, row=5,sticky=W) 
        
        tk.Button(
            self, text="Calcular", bg='#5cba5c', height=1, width=20, command=self.calcular
        ).grid(column=0, row=6, columnspan=2, sticky=W)

        tk.Button(
            self, text="Salir", bg='#f8cecc', height=1, width=20, command=self.destroy
            ).grid(column=2, row=6, columnspan=2, sticky=E) 
        
        self.radioValue.set(-1)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def cambiarIVA(self):
        if self.radioValue.get() == 0:
            self.__valorIVA.set(21)
        else:
            if self.radioValue.get() == 1:
                self.__valorIVA.set(10.5)

    def calcular(self, *args):
        if self.precioEntry.get()!='':
            try:
                valor=float(self.precioEntry.get())
                self.__precioConIva.set(valor + valor*float(self.__valorIVA.get())/100)
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                message='Debe ingresar un valor numérico')
        else:
            self.__precioConIva.set('')
      
if __name__=='__main__':
    app = Aplicacion()
    app.mainloop()