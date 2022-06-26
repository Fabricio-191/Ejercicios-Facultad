# -*- coding: utf-8 -*-
from Fraccion import Fraccion
from tkinter import Tk, ttk, StringVar, E, W
from functools import partial

class Calculadora:
    __ventana: Tk
    __operador: StringVar
    __panel: StringVar
    __valorPrevio: int | Fraccion = 0
    __valorActual: int | Fraccion = 0

    def __init__(self): 
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')

        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # type: ignore
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        ttk.Button(mainframe, text='DEL', command=self.borrarPanel).grid(column=3, row=2, sticky=E)
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, 1)).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO, 2)).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO, 3)).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO, 4)).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO, 5)).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO, 6)).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, 7)).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO, 8)).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO, 9)).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, 0)).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=8, sticky=W)
     
        self.__panel = StringVar()
        self.__operador = StringVar()

        operatorEntry = ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E)) # type: ignore
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E)) # type: ignore
        self.__panel.set('0')
        panelEntry.focus()
        
        self.__ventana.mainloop()

    def borrarPanel(self):
        self.__valorActual = 0
        self.__panel.set('0')

    def ponerNUMERO(self, numero):
        self.__valorActual *= 10
        self.__valorActual += numero
        self.__panel.set(str(self.__valorActual))

    def resolverOperacion(self, operacion):
        resultado = 0
        if operacion == '+':
            resultado = self.__valorActual + self.__valorPrevio
        elif operacion == '-':
            resultado = self.__valorPrevio - self.__valorActual
        elif operacion == '*':
            resultado = self.__valorPrevio * self.__valorActual
        elif operacion == '/':
            if self.__valorActual == 0:
                self.__panel.set('Math Error')
                return

            if isinstance(self.__valorPrevio, Fraccion):
                resultado = self.__valorPrevio / self.__valorActual
            else:
                resultado = Fraccion(self.__valorPrevio, self.__valorActual)
        elif operacion == '%':
            if self.__valorActual == 0:
                self.__panel.set('Math Error')
                return

            resultado = self.__valorPrevio / self.__valorActual
        else:
            resultado = self.__valorActual
        
        print(self.__valorPrevio, operacion, self.__valorActual, '=', resultado)

        self.__valorActual = resultado # type: ignore
        self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        if op == '=':
            self.resolverOperacion(self.__operador.get())
        else:
            self.__operador.set(op)
            self.__valorPrevio = self.__valorActual
            self.__valorActual = 0
    
if __name__ == '__main__':
    calculadora = Calculadora()
