# cita.py
from datetime import datetime

class Cita:
    """
    Clase que representa una cita médica.
    """

    def __init__(self, id_cita, fecha, id_paciente, id_medico, detalle, estado='Pendiente'):
        """
        Inicializa una nueva cita.
        :param id_cita: ID único de la cita.
        :param fecha: Fecha y hora de la cita.
        :param id_paciente: ID del paciente.
        :param id_medico: ID del médico.
        :param detalle: Detalle de la cita.
        :param estado: Estado de la cita (por defecto 'Pendiente').
        """
        self.id = id_cita
        self.fecha = fecha
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.detalle = detalle
        self.estado = estado

    def confirmar_cita(self):
        """Confirma la cita."""
        self.estado = 'Confirmada'
        print(f"Cita con ID {self.id} confirmada.")

    def cancelar_cita(self):
        """Cancela la cita."""
        self.estado = 'Cancelada'
        print(f"Cita con ID {self.id} cancelada.")
