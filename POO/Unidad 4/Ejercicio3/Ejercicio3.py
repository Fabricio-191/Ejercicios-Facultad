from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import requests


class Aplicacion(tk.Tk):
    __precioArs=None
    __precioDls=None

    def __init__(self):
        super().__init__()
        self.title("Conversor de moneda")
        self.resizable = (0,0)
        self.__precioArs = StringVar()
        self.__precioDls = StringVar()
        self.__precioDls.trace('w', self.calcular)
        self.precioEntry = ttk.Entry(self, width=15, textvariable=self.__precioDls)
        self.precioEntry.grid(column=2, row=1, sticky=(W, E))
        tk.Label(self, textvariable=self.__precioArs).grid(column=2, row=2, sticky=(W, E))
        tk.Button(self, text='Salir', padx=10, pady=5, command=self.destroy).grid(column=3, row=3, sticky=W)
        tk.Label(self, text="dolares").grid(column=3, row=1, sticky=W)
        tk.Label(self, text="es equivalente a").grid(column=1, row=2, sticky=E)
        tk.Label(self, text="pesos").grid(column=3, row=2, sticky=W)
        
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.precioEntry.focus()

    def calcular(self, *args):
        if self.precioEntry.get()!='':
            try:
                valor=float(self.precioEntry.get())

                response = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
                data = response.json()
                precioDolar = None

                for obj in data:
                    if obj['casa']['nombre'] == 'Oficial':
                        precioDolar = float(obj['casa']['venta'].replace(',', '.'))
                self.__precioArs.set(valor*precioDolar)
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                message='Debe ingresar un valor numérico')
                self.__precioDls.set('')
                self.precioEntry.focus()
        else:
            self.__precioArs.set('')

if __name__=='__main__':
    app = Aplicacion()
    app.mainloop()