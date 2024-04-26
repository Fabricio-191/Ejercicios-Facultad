from .ManejadorPacientes import ManejadorPacientes
from .VentanaNuevoPaciente import VentanaNuevoPaciente
from .FormDatosPaciente import FormDatosPaciente
from .VentanaIMC import VentanaIMC
from .Paciente import Paciente

from tkinter import Tk, Button, Listbox, Scrollbar, Frame, messagebox
from tkinter import LEFT, RIGHT, BOTH, BOTTOM, Y, END

class VentanaPrincipal(Tk):
	__manejadorPacientes: ManejadorPacientes
	__pacienteSeleccionado: tuple[int, Paciente] | None

	def __init__(self, manejador):
		super().__init__()
		self.__manejadorPacientes = manejador
		self.title("Lista de Pacientes")

		self.__pacientesFrame = Frame(self)
		self.__pacientesFrame.pack(side=LEFT, padx=10, pady=10)

		self.__listbox = Listbox(self.__pacientesFrame, height=15)
		self.__listbox.pack(side=LEFT, fill=BOTH, expand=1)
		self.__listbox.bind("<Double-Button-1>", self.seleccionarPaciente)
		self.__listbox.bind("<<ListboxSelect>>", self.seleccionarPaciente)
	
		scroll = Scrollbar(self.__pacientesFrame, command=self.__listbox.yview)
		scroll.pack(side=RIGHT, fill=Y)
		self.__listbox.config(yscrollcommand=scroll.set)

		self.__form = FormDatosPaciente(self)
		self.__form.pack(padx=10, pady=10)
		
		botonGuardar = Button(self.__form, text="Guardar", command=self.guardar)
		botonGuardar.pack(side=RIGHT, ipadx=5, padx=5, pady=5)
		
		botonBorrar = Button(self.__form, text="Borrar", command=self.borrar)
		botonBorrar.pack(side=RIGHT, ipadx=5, padx=5, pady=5)
		
		botonVerIMC = Button(self.__form, text="Ver IMC", command=self.verIMC)
		botonVerIMC.pack(side=RIGHT, ipadx=5, padx=5, pady=5)

		botonAgregarPaciente = Button(self, text="Agregar Paciente", command=self.añadirPaciente)
		botonAgregarPaciente.pack(side=BOTTOM, pady=5)

		for paciente in self.__manejadorPacientes:
			self.cargarPacienteALista(paciente)

		self.mostrarPaciente(0)

	def cargarPacienteALista(self, paciente):
		self.__listbox.insert(END, paciente.getNombre() + ' ' + paciente.getApellido())

	def mostrarPaciente(self, pos):
		primerPaciente = self.__manejadorPacientes.obtener(pos)

		if primerPaciente is None:
			self.__pacienteSeleccionado = None
			self.__form.clear()
		else:
			self.__pacienteSeleccionado = (pos, primerPaciente)
			self.__form.setPaciente(primerPaciente)
			self.__listbox.select_set(pos)

	def añadirPaciente(self):
		def callback(paciente):
			self.__manejadorPacientes.añadir(paciente)
			self.cargarPacienteALista(paciente)

		ventana = VentanaNuevoPaciente(self, callback)
		ventana.wait_window()

	def guardar(self):
		if self.__pacienteSeleccionado is None:
			messagebox.showerror("Error", "No hay paciente seleccionado")
		else:
			datos = self.__form.obtenerDatos()
			pos = self.__pacienteSeleccionado[0]
			paciente = Paciente(datos)
			self.__manejadorPacientes.actualizar(pos, paciente)

	def borrar(self):
		if self.__pacienteSeleccionado is None:
			messagebox.showerror("Error", "No hay paciente seleccionado")
		else:
			pos = self.__pacienteSeleccionado[0]

			self.__manejadorPacientes.borrar(pos)
			self.__listbox.delete(pos)
			self.__form.clear()

			self.mostrarPaciente(0)

	def verIMC(self):
		if self.__pacienteSeleccionado is None:
			messagebox.showerror("Error", "No hay paciente seleccionado")
		else:
			ventana = VentanaIMC(self, self.__pacienteSeleccionado[1])
			ventana.wait_window()

	def seleccionarPaciente(self, _):
		currentSelection = self.__listbox.curselection()

		if len(currentSelection) != 0:
			self.mostrarPaciente(currentSelection[0])
