from tkinter import messagebox, StringVar, IntVar, Label, Entry, Radiobutton, Button, W, E, Tk

class Aplicacion(Tk):
	__precioSinIva: StringVar
	__precioConIva: StringVar
	__valorIVA: StringVar

	def __init__(self):
		super().__init__()
		self.title("Calculo de IVA")
		self.__precioSinIva = StringVar()
		self.__precioConIva = StringVar()
		self.__valorIVA = StringVar()
		self.radioValue= IntVar()

		Label(self, text="Precio sin IVA: ").grid(column=0, row=0,sticky=W)

		self.precioEntry = Entry(self, textvariable=self.__precioSinIva,width=30)
		self.precioEntry.grid(column=1, row=0 , columnspan=4, sticky=W)
		
		boton1 = Radiobutton(self, text='IVA 21 %', value=0, command=self.cambiarIVA,variable=self.radioValue)
		boton1.grid(row=2, column=0, columnspan=1, sticky='w')
		boton1.select()

		Radiobutton(self, text='IVA 10.5 %', value=1,command=self.cambiarIVA, variable=self.radioValue).grid(
			row=3, column=0, columnspan=1, sticky='w'
		)

		Label(self, text="IVA: ").grid(column=0, row=4,sticky=W)

		Label(self, textvariable= self.__valorIVA).grid(column=1, row=4,sticky=W)
		
		Label(self, text="Precio con IVA: ").grid(column=0, row=5,sticky=W)

		Label(self, textvariable= self.__precioConIva).grid(column=1, row=5,sticky=W) 
		
		Button(self, text="Calcular", bg='#5cba5c', height=1, width=20, command=self.calcular).grid(
			column=0, row=6, columnspan=2, sticky=W
		)

		Button(self, text="Salir", bg='#f8cecc', height=1, width=20, command=self.destroy).grid(
			column=2, row=6, columnspan=2, sticky=E
		) 
		
		self.radioValue.set(-1)

		for child in self.winfo_children():
			child.grid_configure(padx=5, pady=5)

	def cambiarIVA(self):
		if self.radioValue.get() == 0:
			self.__valorIVA.set('21')
		else:
			self.__valorIVA.set('10.5')

	def calcular(self, *args):
		if self.precioEntry.get() == '':
			self.__precioConIva.set('')
		else:
			try:
				valor = float(self.precioEntry.get())
				valor += valor * float(self.__valorIVA.get()) / 100
				self.__precioConIva.set(str(valor))
			except ValueError:
				messagebox.showerror(
					'Error de tipo',
					'Debe ingresar un valor numérico'
				)
	  
if __name__=='__main__':
	app = Aplicacion()
	app.mainloop()