"""
Realice un programa  que simule el comportamiento de un hospital, donde los pacientes acuden a sacar turnos para los consultorios externos en mesa de entradas  donde se toma la siguiente información: nombre, documento y especialidad (Ginecología, Clínica médica, Oftalmología, Pediatría)  con un tiempo promedio de atención de 2 minutos. Dependiendo de la especialidad se le indica el numero de  consultorio en que será atendido. El tiempo promedio de atención del médico es de 20’. 
Considerando que la frecuencia de llegada de los pacientes al hospital es de 1 por minutos  aproximadamente; que en cada especialidad se atiende un máximo de 10 pacientes y los turnos solamente se dan de 7 a 8 de la mañana.

Se pide
    a) calcular el tiempo promedio de espera en la cola de turnos.
    b) tiempo promedio de espera de los pacientes en cada especialidad.
    c) cantidad de personas que no pudieron obtener turnos.

Nota: considere el tiempo de simulación de 4 horas
"""
import time

class Turno:
    __nombre: str
    __documento: str
    __especialidad: str
    
    def __init__(self, nombre, documento, especialidad):
        self.__nombre = nombre
        self.__documento = documento
        self.__especialidad = especialidad

class Especialidad: # Cola
    __turnos: list
    __nombre: str

    def __init__(self, nombre):
        self.__turnos = []
        self.__nombre = nombre

    def agregarTurno(self, turno):
        self.__turnos.append(turno)

    def obtenerTurno(self):
        if len(self.__turnos) == 0:
            raise Exception('No quedan elementos en la cola')

        return self.__turnos.pop(0)

    def longitud(self):
        return len(self.__turnos)

    def getNombre(self):
        return self.__nombre
        

class Hospital:
    __especialidades: list[Especialidad]

    def __init__(self):
        self.__especialidades = [
            Especialidad('Ginecología'),
            Especialidad('Clínica médica'),
            Especialidad('Oftalmología'),
            Especialidad('Pediatría')
        ]