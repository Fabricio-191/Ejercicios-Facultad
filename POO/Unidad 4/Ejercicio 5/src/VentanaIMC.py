from tkinter import Button, Frame, StringVar, Toplevel, Label, Entry, W, E, DISABLED

class VentanaIMC(Toplevel):
	__frame: Frame
	def __init__(self, parent, paciente):
		super().__init__(parent)

		self.__frame = Frame(self)
		self.__frame.pack()

		label1 = Label(self.__frame, text='IMC')
		label1.grid(row=0, column=0, pady=5, padx=5, sticky=W)

		strVar1 = StringVar(self, "{:.2f}".format(paciente.calcularMCI()))
		entry1 = Entry(self.__frame, width=25, textvariable=strVar1, state=DISABLED)
		entry1.grid(row=0, column=1, columnspan=2, pady=5, padx=5, sticky=E)

		label2 = Label(self.__frame, text='Tipo')
		label2.grid(row=1, column=0, pady=5, padx=5, sticky=W)

		strVar2 = StringVar(self, paciente.tipo())
		entry2 = Entry(self.__frame, width=25, textvariable=strVar2, state=DISABLED)
		entry2.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky=E)

		boton = Button(self.__frame, text='Cerrar', command=self.destroy)
		boton.grid(row=2, column=1, pady=5, padx=5, sticky='sew')
