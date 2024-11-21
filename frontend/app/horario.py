# horario.py
from datetime import time

class Horario:
    """
    Clase que representa un horario de disponibilidad de un médico.
    """

    def __init__(self, id_medico, dia, hora_inicio, hora_fin):
        """
        Inicializa un nuevo horario para un médico.
        :param id_medico: ID del médico al que pertenece el horario.
        :param dia: Día de la semana.
        :param hora_inicio: Hora de inicio de disponibilidad en formato 'HH:MM'.
        :param hora_fin: Hora de fin de disponibilidad en formato 'HH:MM'.
        """
        self.id_medico = id_medico
        self.dia = dia
        self.hora_inicio = time.fromisoformat(hora_inicio)
        self.hora_fin = time.fromisoformat(hora_fin)

    def disponible(self, fecha):
        """
        Verifica si el médico está disponible en una fecha específica.
        :param fecha: Fecha y hora a verificar.
        :return: True si el médico está disponible, False si no.
        """
        dia_semana = fecha.strftime("%A")
        hora_actual = fecha.time()

        if self.dia == dia_semana and self.hora_inicio <= hora_actual <= self.hora_fin:
            return True
        return False
