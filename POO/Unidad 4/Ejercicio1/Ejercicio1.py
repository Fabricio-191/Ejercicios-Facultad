from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Aplicacion(tk.Tk):
    __estatura=None
    __peso=None
    __mci=None
    __tipo_mci=None

    def __init__(self):
        super().__init__()
        self.title("Calculadora IMC")
        self.__peso = StringVar()
        self.__estatura = StringVar()
        self.__mci = DoubleVar()
        self.__tipo_mci = StringVar()

        self.pesoEntry = tk.Entry(self, textvariable=self.__peso,width=60)
        self.pesoEntry.grid(column=1, row=1 , columnspan=4, sticky=W)

        self.estaturaEntry = tk.Entry(self, textvariable=self.__estatura,width=60)
        self.estaturaEntry.grid(column=1, row=0,columnspan=4, sticky=W)

        self.estaturaEntry.focus()

        tk.Label(
            self, text="Estatura: ", 
        ).grid(column=0, row=0,sticky=W)

        tk.Label(
            self, text="cm",background="#cccccc"
        ).grid(column=5, row=0,sticky=E)

        tk.Label(
            self, text="Peso: ", 
        ).grid(column=0, row=1,sticky=W)

        tk.Label(
            self, text="kg",background="#cccccc"
        ).grid(column=5, row=1,sticky=E)

        tk.Button(
            self, text="Calcular", bg='#5cba5c',fg='#ffffff', height=1, width=20, command=self.calcular
        ).grid(column=1, row=3, columnspan=2, sticky=W)

        tk.Button(
            self, text="Limpiar", bg='#5cba5c',fg='#ffffff', height=1, width=20, command=self.limpiar
        ).grid(column=3, row=3, columnspan=2, sticky=E) 

        tk.Label(
            self, text=f"Tu Indice de Masa Corporal (IMC) es: ", fg='#6d8c68', bg='#e1f0d9'
        ).grid(column=1, row=5, columnspan= 3, sticky=W)

        tk.Label(
            self, textvariable=self.__mci, fg='#6d8c68', bg='#e1f0d9',font=('calibre',10,'bold')
        ).grid(column=3, row=5, sticky=E)

        tk.Label(
            self, text="kg/m2",fg='#6d8c68',bg='#e1f0d9',font=('calibre',10,'bold')
        ).grid(column=4, row=5, sticky=E)
            
        tk.Label(
            self, textvariable=self.__tipo_mci, fg='#6d8c68', bg='#e1f0d9',font=('calibre',10,'bold')
        ).grid(column=1, row=6, columnspan=4, sticky=N)  
        
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)     
            
    def limpiar(self):
        self.__estatura.set("")
        self.__peso.set("")

    def calcular(self):
        try:
            m2 = float(self.estaturaEntry.get())
            peso = float(self.pesoEntry.get())         
        except ValueError:
            messagebox.showerror(
                title='Error', message='Debe ingresar un valor numérico'
            )
            self.__estatura.set('')
            self.__peso.set('')
            self.estaturaEntry.focus()
        else:
            mci = peso / ((m2 / 100) * (m2 / 100))
            self.__mci.set('{0:.2f}'.format(mci) )         
            if mci < 18.5:
                self.__tipo_mci.set("Peso inferior al normal")
            elif  18.5 <= mci < 25:
                self.__tipo_mci.set("Peso normal")
            elif 25 <= mci < 30:
                self.__tipo_mci.set("Sobrepeso")
            else:
                self.__tipo_mci.set("Obesidad")
      
if __name__=='__main__':
    app = Aplicacion()
    app.mainloop()