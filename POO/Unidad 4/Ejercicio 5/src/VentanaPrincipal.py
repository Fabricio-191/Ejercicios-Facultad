from ManejadorPacientes import ManejadorPacientes
from VentanaNuevoPaciente import VentanaNuevoPaciente
from FormDatosPaciente import FormDatosPaciente2

from tkinter import Tk, Button, Listbox, Scrollbar, Frame
from tkinter import LEFT, RIGHT, BOTH, BOTTOM, Y, END

class VentanaPrincipal(Tk):
    __manejador: ManejadorPacientes
    __pacienteSeleccionado = None

    def __init__(self, manejador):
        super().__init__()
        self.__manejador = manejador
        self.title("Lista de Pacientes")

        self.__pacientesFrame = Frame(self)
        self.__pacientesFrame.pack(side=LEFT, padx=10, pady=10)
        self.__listbox = Listbox(self.__pacientesFrame, height=15)
        self.__listbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.__listbox.bind("<Double-Button-1>", self.seleccionarPaciente)
    
        scroll = Scrollbar(self.__pacientesFrame, command=self.__listbox.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.__listbox.config(yscrollcommand=scroll.set)

        self.__form = FormDatosPaciente2(self)
        self.__form.pack(padx=10, pady=10)

        self.__botonAgregarContacto = Button(self, text="Agregar Paciente", command=self.añadirPaciente)
        self.__botonAgregarContacto.pack(side=BOTTOM, pady=5)

        for paciente in self.__manejador:
            self.cargarPaciente(paciente)

        self.__pacienteSeleccionado = self.__manejador.first()
        self.__form.setPaciente(self.__pacienteSeleccionado)

    def añadirPaciente(self):
        def callback(paciente):
            self.__manejador.añadir(paciente)
            self.cargarPaciente(paciente)

        ventana = VentanaNuevoPaciente(self, callback)
        ventana.wait_window()

    def cargarPaciente(self, paciente):
        self.__listbox.insert(END, paciente.getNombre() + ' ' + paciente.getApellido())

    def seleccionarPaciente(self, _):
        pos = self.__listbox.curselection()[0]
        paciente = self.__manejador.obtenerPaciente(pos)

        self.__pacienteSeleccionado = paciente
        self.__form.setPaciente(paciente)