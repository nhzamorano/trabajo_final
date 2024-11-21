# medico.py
from datetime import datetime

class Medico:
    """
    Clase que representa a un médico en el sistema.
    Contiene información básica del médico y métodos para gestionar su disponibilidad.
    """
    
    def __init__(self, id_medico, nombre, especialidad):
        """
        Inicializa un nuevo médico.
        :param id_medico: ID del médico.
        :param nombre: Nombre del médico.
        :param especialidad: Especialidad del médico.
        """
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad
        self.horarios_disponibles = []

    def actualizar_disponibilidad(self, fecha_hora_inicio, fecha_hora_fin):
        """
        Actualiza los horarios disponibles del médico.
        :param fecha_hora_inicio: Fecha y hora de inicio de la disponibilidad.
        :param fecha_hora_fin: Fecha y hora de fin de la disponibilidad.
        """
        self.horarios_disponibles.append((fecha_hora_inicio, fecha_hora_fin))

    def verificar_disponibilidad(self, fecha):
        """
        Verifica si el médico está disponible en la fecha y hora dadas.
        :param fecha: Fecha y hora para verificar la disponibilidad.
        :return: True si está disponible, False en caso contrario.
        """
        for inicio, fin in self.horarios_disponibles:
            if inicio <= fecha <= fin:
                return True
        return False

    def mostrar_disponibilidad(self):
        """Muestra los horarios disponibles del médico."""
        if not self.horarios_disponibles:
            print(f"{self.nombre} no tiene horarios de disponibilidad registrados.")
        else:
            print(f"Horarios disponibles de {self.nombre}:")
            for inicio, fin in self.horarios_disponibles:
                print(f"Desde {inicio} hasta {fin}")
