# reporte.py
import pandas as pd

class Reporte:
    """
    Clase para generar reportes y exportarlos a formato Excel.
    """

    def __init__(self, id_admin, tipo, contenido):
        """
        Inicializa un nuevo reporte.
        :param id_admin: ID del administrador que genera el reporte.
        :param tipo: Tipo de reporte (demanda de citas, cancelaciones, etc.).
        :param contenido: Contenido del reporte.
        """
        self.id_admin = id_admin
        self.tipo = tipo
        self.contenido = contenido

    def generar(self):
        """
        Genera el contenido del reporte.
        Esta es una función general que puede ser implementada por reportes específicos.
        """
        pass

    def exportar_informe(self, nombre_archivo):
        """
        Exporta el contenido del reporte a un archivo Excel.
        :param nombre_archivo: Nombre del archivo Excel a generar.
        """
        df = pd.DataFrame(self.contenido)
        df.to_excel(f"{nombre_archivo}.xlsx", index=False)
        print(f"Reporte exportado exitosamente como {nombre_archivo}.xlsx")


class ReporteDemanda(Reporte):
    """
    Reporte específico que analiza la demanda de médicos y citas.
    """

    def generar(self, sistema_citas):
        """
        Genera un reporte de demanda de citas para cada médico.
        :param sistema_citas: El sistema que contiene los médicos y citas.
        """
        demanda = []
        for medico in sistema_citas.medicos:
            citas_medico = len([cita for cita in sistema_citas.citas if cita.id_medico == medico.id_medico])
            demanda.append({
                "Médico": medico.nombre,
                "Especialidad": medico.especialidad,
                "Citas Programadas": citas_medico
            })
        self.contenido = demanda


class ReporteCancelaciones(Reporte):
    """
    Reporte específico que analiza las cancelaciones de citas.
    """

    def generar(self, sistema_citas):
        """
        Genera un reporte de cancelaciones de citas.
        :param sistema_citas: El sistema que contiene los pacientes y citas.
        """
        cancelaciones = []
        for paciente in sistema_citas.pacientes:
            canceladas = len([cita for cita in paciente.citas if cita.estado == "Cancelada"])
            cancelaciones.append({
                "Paciente": paciente.nombre,
                "Citas Canceladas": canceladas
            })
        self.contenido = cancelaciones
