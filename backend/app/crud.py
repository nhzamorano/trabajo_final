from datetime import datetime
from sqlalchemy.exc import IntegrityError
from .models import Medico,Paciente,Usuario, session

#*************MEDICOS**************************
def agregar_medico(identificacion : int,nombre_completo: str, telefono:str, especialidad: str):
    nuevo_medico = Medico(identificacion=identificacion,nombre_completo=nombre_completo, telefono=telefono, especialidad=especialidad)
    session.add(nuevo_medico)
    try:
        session.commit()
        return nuevo_medico
    except IntegrityError:
        session.rollback()
        print("Error de integridad: el medico ya existe")
        return None

def actualizar_medico(
    medico_id: int, 
    nombre_completo: str, 
    telefono: str, 
    especialidad: str
):
    medico_existente = session.query(Medico).filter_by(identificacion=medico_id).first()
    if not medico_existente:
        print(f"Medico con ID {medico_id} no encontrado")
        return None

    medico_existente.nombre_completo = nombre_completo
    medico_existente.telefono = telefono
    medico_existente.especialidad = especialidad

    try:
        session.commit()
        return medico_existente
    except IntegrityError:
        session.rollback()
        print("Error de integridad: conflicto al actualizar el medico")
        return None

def obtener_medicos():
    return session.query(Medico).all()

def obtener_medico_por_id(identificacion: int):
    return session.query(Medico).filter(Medico.identificacion == identificacion).first()

def eliminar_medico(medico_id: int):
    medico_existente = session.query(Medico).filter_by(identificacion=medico_id).first()
    if not medico_existente:
        print(f"Medico con ID {medico_id} no encontrado")
        return None
    session.delete(medico_existente)
    
    try:
        session.commit()
        print(f"Medico con ID {medico_id} eliminado exitosamente")
        return medico_existente
    except Exception as e:
        session.rollback()
        print(f"Error al eliminar el medico: {str(e)}")
        return None

#***************PACIENTES*************************************
def agregar_paciente(identificacion : int,nombre_completo: str, celular:str, correo: str):
    nuevo_paciente = Paciente(identificacion=identificacion,nombre_completo=nombre_completo, celular=celular, correo=correo)
    session.add(nuevo_paciente)
    try:
        session.commit()
        return nuevo_paciente
    except IntegrityError:
        session.rollback()
        print("Error de integridad: el paciente ya existe")
        return None

def actualizar_paciente(
    paciente_id: int, 
    nombre_completo: str, 
    celular: str, 
    correo: str
):
    paciente_existente = session.query(Paciente).filter_by(identificacion=paciente_id).first()
    if not paciente_existente:
        print(f"Paciente con ID {paciente_id} no encontrado")
        return None

    paciente_existente.nombre_completo = nombre_completo
    paciente_existente.celular = celular
    paciente_existente.correo = correo

    try:
        session.commit()
        return paciente_existente
    except IntegrityError:
        session.rollback()
        print("Error de integridad: conflicto al actualizar el paciente")
        return None

def eliminar_paciente(paciente_id: int):
    paciente_existente = session.query(Paciente).filter_by(identificacion=paciente_id).first()
    if not paciente_existente:
        print(f"Paciente con ID {paciente_id} no encontrado")
        return None
    session.delete(paciente_existente)
    
    try:
        session.commit()
        print(f"Paciente con ID {paciente_id} eliminado exitosamente")
        return paciente_existente
    except Exception as e:
        session.rollback()
        print(f"Error al eliminar el paciente: {str(e)}")
        return None

def obtener_pacientes():
    return session.query(Paciente).all()

def obtener_paciente_por_id(identificacion: int):
    return session.query(Paciente).filter(Paciente.identificacion == identificacion).first()

#----------------------------------------------------------------
def agregar_usuario(nombre: str, telefono: str,cargo:str,usuario:str,contrasena:str,email:str,fecha_registro: datetime):
    nuevo_usuario = Usuario(nombre=nombre, telefono=telefono,cargo=cargo,usuario=usuario,contrasena=contrasena,email=email,fecha_registro=fecha_registro)
    session.add(nuevo_usuario)
    try:
        session.commit()
        return nuevo_usuario
    except IntegrityError:
        session.rollback()
        print("Error de integridad: el usuario ya existe")
        return None

def obtener_usuarios():
    return session.query(Usuario).all()

def obtener_usuario_por_id(id: int):
    return session.query(Usuario).filter(Usuario.id == id).first()

#
def actualizar_usuario(
    usuario_id: int, 
    nombre: str, 
    telefono: str, 
    cargo: str, 
    usuario: str, 
    contrasena: str, 
    email: str, 
    fecha_registro: datetime
    #db_session: session
):
    # Buscar el usuario por ID
    usuario_existente = session.query(Usuario).filter_by(id=usuario_id).first()
    
    # Verificar si el usuario existe
    if not usuario_existente:
        print(f"Usuario con ID {usuario_id} no encontrado")
        return None

    # Actualizar los datos del usuario
    usuario_existente.nombre = nombre
    usuario_existente.telefono = telefono
    usuario_existente.cargo = cargo
    usuario_existente.usuario = usuario
    usuario_existente.contrasena = contrasena
    usuario_existente.email = email
    usuario_existente.fecha_registro = fecha_registro

    # Guardar los cambios en la base de datos
    try:
        session.commit()
        return usuario_existente
    except IntegrityError:
        session.rollback()
        print("Error de integridad: conflicto al actualizar el usuario")
        return None

def eliminar_usuario(usuario_id: int):
    usuario_existente = session.query(Usuario).filter_by(id=usuario_id).first()
    
    # Verificar si el usuario existe
    if not usuario_existente:
        print(f"Usuario con ID {usuario_id} no encontrado")
        return None

    # Eliminar el usuario
    session.delete(usuario_existente)
    
    try:
        session.commit()
        print(f"Usuario con ID {usuario_id} eliminado exitosamente")
        return usuario_existente
    except Exception as e:
        session.rollback()
        print(f"Error al eliminar el usuario: {str(e)}")
        return None

