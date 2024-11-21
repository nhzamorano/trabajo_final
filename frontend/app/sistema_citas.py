# sistema_citas.py
from paciente import Paciente
from medico import Medico
from cita import Cita
from datetime import datetime

class SistemaCitas:
    """
    Clase Singleton que gestiona el sistema de citas.
    """

    _instance = None

    @staticmethod
    def get_instance():
        """Método estático para obtener la instancia única del sistema."""
        if SistemaCitas._instance is None:
            SistemaCitas._instance = SistemaCitas()
        return SistemaCitas._instance

    def __init__(self):
        """Inicializa el sistema de citas."""
        if SistemaCitas._instance is not None:
            raise Exception("Esta clase es un Singleton")
        else:
            self.pacientes = []
            self.medicos = []
            self.citas = []

    def agregar_paciente(self, paciente):
        """Agrega un paciente al sistema."""
        self.pacientes.append(paciente)

    def agregar_medico(self, medico):
        """Agrega un médico al sistema."""
        self.medicos.append(medico)

    def programar_cita(self, paciente, medico, fecha, detalle):
        """Programa una nueva cita."""
        id_cita = len(self.citas) + 1

        # Mostrar la disponibilidad del médico
        medico.mostrar_disponibilidad()

        # Verificar si el médico está disponible en la fecha
        if not medico.verificar_disponibilidad(fecha):
            print(f"El médico {medico.nombre} no está disponible en la fecha {fecha}.")
            return

        nueva_cita = Cita(id_cita, fecha, paciente.cedula, medico.id_medico, detalle)
        self.citas.append(nueva_cita)
        paciente.agendar_cita(nueva_cita)
        print(f"Cita programada para el paciente {paciente.nombre} con el médico {medico.nombre} en la fecha {fecha}.")
