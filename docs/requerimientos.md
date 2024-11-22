Requerimientos del Sistema - Sistema de Gestión de Citas Médicas

Este documento detalla los requerimientos funcionales y no funcionales para el sistema de gestión de citas médicas.

Requerimientos Funcionales

1. Registro de Pacientes
El sistema debe permitir registrar nuevos pacientes con validaciones específicas para cada campo:

Cédula: Debe tener un formato válido y único para cada paciente (ejemplo: 123-456789-0001).
Nombre: Debe contener únicamente letras y aceptar espacios en blanco.
Correo electrónico: Debe verificarse que sea válido (formato estándar como <usuario@dominio.com>).
Teléfono: Debe cumplir un formato numérico con un mínimo y máximo de dígitos según el país (ejemplo: 10 dígitos).
Dirección: Texto libre con un límite de 255 caracteres.

2.Registro de Médicos
El sistema debe registrar nuevos médicos con las siguientes características:

ID: Asignado automáticamente por el sistema, debe ser único y secuencial.
Nombre: Solo letras y espacios en blanco.
Especialidad: Seleccionada de una lista predefinida de especialidades (ejemplo: Pediatría, Cardiología).

1. Actualización de Disponibilidad de Médicos
El sistema debe permitir al médico registrar su disponibilidad en un rango de fechas y horas:

Fecha y hora de inicio: Debe ser igual o posterior a la fecha actual.
Fecha y hora de fin: Debe ser posterior a la fecha y hora de inicio.
Validación: Se debe verificar que el rango de disponibilidad no se superponga con otra disponibilidad ya registrada.

4.Programación de Citas
El sistema debe permitir a los pacientes programar citas médicas con las siguientes reglas:

Cédula del paciente: Validada para asegurar que esté registrada previamente en el sistema.
ID del médico: Verificado para confirmar que está registrado en el sistema.
Fecha y hora de la cita:
Debe coincidir con la disponibilidad registrada del médico.
No debe solaparse con otra cita ya registrada.
Detalle de la cita: Texto opcional con un máximo de 255 caracteres.

1. Consulta de Citas
El sistema debe permitir a los pacientes consultar las citas programadas con el siguiente formato:

Mostrar lista de citas con:
Fecha y hora.
Médico asignado.
Detalle de la cita.

6.Cancelación de Citas
El sistema debe permitir a los pacientes cancelar citas programadas bajo las siguientes condiciones:

El paciente debe proporcionar el ID de la cita.
Se debe verificar que la cita aún no haya ocurrido.
Se debe registrar el motivo de la cancelación como texto opcional.

1. Generación de Reportes
El sistema debe generar dos tipos de reportes con la opción de exportar a formato Excel:

Reporte de Demanda:
Cantidad de citas por médico y especialidad.
Rangos de horarios más solicitados.
Reporte de Cancelaciones:
Citas canceladas por paciente.
Motivos de cancelación más frecuentes.
Requerimientos No Funcionales

1. Interfaz de Usuario

Debe ser interactiva, basada en menús, y fácil de usar.
Debe mostrar mensajes claros en caso de errores (ejemplo: "La cédula ingresada no es válida").
2. Rendimiento

Capacidad para manejar al menos 500 médicos y 5000 pacientes sin impactar significativamente la velocidad del sistema.
Los reportes deben generarse en menos de 2 segundos para un total de hasta 10,000 registros.
3. Seguridad

Validaciones estrictas para evitar datos duplicados o incorrectos.
Enmascarar datos sensibles como la cédula en los listados públicos.
Realizar copias de seguridad automáticas del sistema diariamente.
4. Escalabilidad

Estructura modular del código para facilitar la adición de nuevas funcionalidades, como recordatorios por correo o gestión de recetas.

5.Mantenimiento
Código estructurado siguiendo el estándar PEP 8.

Contacto
Para preguntas o soporte adicional, puedes abrir un issue en el repositorio del proyecto o ponerte en contacto con el Desarrollador
