# paciente.py
class Paciente:
    """
    Clase que representa a un paciente en el sistema.
    Contiene información básica del paciente y métodos para gestionar citas.
    """
    
    def __init__(self, cedula, nombre, correo_electronico, telefono, direccion):
        """
        Inicializa un nuevo paciente.
        :param cedula: Cédula del paciente.
        :param nombre: Nombre del paciente.
        :param correo_electronico: Correo electrónico del paciente.
        :param telefono: Número de teléfono del paciente.
        :param direccion: Dirección del paciente.
        """
        self.cedula = cedula
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.direccion = direccion
        self.citas = []

    def agendar_cita(self, cita):
        """
        Agrega una cita a la lista de citas del paciente.
        :param cita: Instancia de la clase Cita.
        """
        self.citas.append(cita)
        print(f"Cita agendada para el paciente {self.nombre} con el médico {cita.id_medico} en la fecha {cita.fecha}.")

    def cancelar_cita(self, id_cita):
        """
        Cancela una cita del paciente.
        :param id_cita: ID de la cita a cancelar.
        """
        cita_a_cancelar = next((cita for cita in self.citas if cita.id == id_cita), None)
        if cita_a_cancelar:
            cita_a_cancelar.cancelar_cita()
            self.citas.remove(cita_a_cancelar)
            print(f"Cita con ID {id_cita} cancelada.")
        else:
            print("Cita no encontrada.")

    def consultar_citas(self):
        """Muestra las citas actuales del paciente."""
        if not self.citas:
            print("No hay citas programadas.")
        else:
            for cita in self.citas:
                print(f"Cita con ID {cita.id}, fecha {cita.fecha}, estado: {cita.estado}")
