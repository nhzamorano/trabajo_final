# notificacion.py
class Notificacion:
    """
    Clase para gestionar el envío de notificaciones por correo electrónico o SMS.
    """

    def __init__(self, mensaje, medio):
        """
        Inicializa la notificación.
        :param mensaje: Mensaje de la notificación.
        :param medio: Medio de envío ('correo' o 'sms').
        """
        self.mensaje = mensaje
        self.medio = medio

    def enviar(self, destinatario):
        """
        Envía la notificación al destinatario.
        :param destinatario: Correo electrónico o número de teléfono.
        """
        if self.medio == 'correo':
            self.enviar_correo(destinatario)
        elif self.medio == 'sms':
            self.enviar_sms(destinatario)
        else:
            print(f"Medio de notificación '{self.medio}' no soportado.")

    def enviar_correo(self, email):
        """
        Simula el envío de una notificación por correo electrónico.
        :param email: Dirección de correo electrónico del destinatario.
        """
        print(f"Enviando correo a {email}: {self.mensaje}")

    def enviar_sms(self, telefono):
        """
        Simula el envío de una notificación por SMS.
        :param telefono: Número de teléfono del destinatario.
        """
        print(f"Enviando SMS a {telefono}: {self.mensaje}")
