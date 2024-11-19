from fastapi import FastAPI, HTTPException, Depends
from app.crud import *
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from app import create_app

app = FastAPI()
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

class MedicoBase(BaseModel):
    identificacion: int
    nombre_completo: str
    telefono: str 
    especialidad: str

class PacienteBase(BaseModel):
    identificacion: int
    nombre_completo: str
    celular: str 
    correo: str

class CitaBase(BaseModel):
    fecha_hora: str
    paciente: int
    medico: int

class UsuarioBase(BaseModel):
    nombre: str
    telefono: str 
    cargo: str
    usuario: str
    contrasena: str
    email:str
    fecha_registro: datetime = datetime.now()

@app.get("/favicon.ico")
async def favicon():
    return {"detail": "Favicon no configurado"}

#***********MEDICOS*******************
@app.post("/medico")
def agregar_medico_view(medico: MedicoBase):
    nuevo_medico = agregar_medico(medico.identificacion,medico.nombre_completo, medico.telefono, medico.especialidad)
    if nuevo_medico is None:
        raise HTTPException(status_code=400, detail="Error al crear el medico")
    return {"mensaje": "Medico agregado", "medico": nuevo_medico.nombre_completo}

@app.put("/medico/{medico_id}")
def actualizar_medico_view(medico_id: int, medico: MedicoBase):
    medico_actualizado = actualizar_medico(
        medico_id,
        medico.nombre_completo,
        medico.telefono,
        medico.especialidad
    )
    if medico_actualizado is None:
        raise HTTPException(status_code=404, detail="Medico no encontrado o no se pudo actualizar")
    return {"mensaje": "Medico actualizado", "medico": medico_actualizado.nombre_completo}

@app.get("/medicos")
def obtener_medicos_view():
    medicos = obtener_medicos()
    medicos_lista = [{
        "identificacion": medico.identificacion,
        "nombre_completo": medico.nombre_completo,
        "telefono": medico.telefono,
        "especialidad": medico.especialidad
    }
    for medico in medicos
    ]
    if medicos_lista:
        return {"medicos": medicos_lista}
    else:
        return {"mensaje": "No hay medicos disponibles en esta bd"} 

@app.get("/medico/{identificacion}")
def obtener_medico_view(identificacion: int):
    medico = obtener_medico_por_id(identificacion)
    if not medico:
        #raise HTTPException(status_code=404, detail="Medico no encontrado")
        return {"mensaje": "Medico no encontrado"}
    medico_lista = [{
        "identidicacion": medico.identificacion,
        "nombre_completo": medico.nombre_completo,
        "telefono": medico.telefono,
        "especialidad": medico.especialidad
    }]
    return {"medico": medico_lista}

@app.delete("/medico/{medico_id}")
def eliminar_medico_view(medico_id: int):
    medico_eliminado = eliminar_medico(medico_id=medico_id)
    if not medico_eliminado:
        raise HTTPException(status_code=404, detail="Medico no encontrado")
    return {"mensaje": "Medico eliminado", "medico": medico_eliminado.nombre_completo}

#********PACIENTES*************
@app.post("/paciente")
def agregar_paciente_view(paciente: PacienteBase):
    nuevo_paciente = agregar_paciente(paciente.identificacion,paciente.nombre_completo, paciente.celular, paciente.correo)
    if nuevo_paciente is None:
        raise HTTPException(status_code=400, detail="Error al crear el paciente")
    return {"mensaje": "Paciente agregado", "paciente": nuevo_paciente.nombre_completo}

@app.put("/paciente/{paciente_id}")
def actualizar_paciente_view(paciente_id: int, paciente: PacienteBase):
    paciente_actualizado = actualizar_paciente(
        paciente_id,
        paciente.nombre_completo,
        paciente.celular,
        paciente.correo
    )
    if paciente_actualizado is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado o no se pudo actualizar")
    return {"mensaje": "Paciente actualizado", "paciente": paciente_actualizado.nombre_completo}


@app.get("/pacientes")
def obtener_pacientes_view():
    pacientes = obtener_pacientes()
    pacientes_lista = [{
        "identificacion": paciente.identificacion,
        "nombre_completo": paciente.nombre_completo,
        "celular": paciente.celular,
        "correo": paciente.correo
    }
    for paciente in pacientes
    ]
    if pacientes_lista:
        return {"pacientes": pacientes_lista}
    else:
        return {"mensaje": "No hay pacientes disponibles en esta bd"} 

@app.get("/paciente/{identificacion}")
def obtener_paciente_view(identificacion: int):
    paciente = obtener_paciente_por_id(identificacion)
    if not paciente:
        #raise HTTPException(status_code=404, detail="Medico no encontrado")
        return {"mensaje": "Paciente no encontrado"}
    paciente_lista = [{
        "identidicacion": paciente.identificacion,
        "nombre_completo": paciente.nombre_completo,
        "celular": paciente.celular,
        "correo": paciente.correo
    }]
    return {"paciente": paciente_lista}

@app.delete("/paciente/{paciente_id}")
def eliminar_paciente_view(paciente_id: int):
    paciente_eliminado = eliminar_paciente(paciente_id=paciente_id)
    if not paciente_eliminado:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"mensaje": "Paciente eliminado", "paciente": paciente_eliminado.nombre_completo}

#******** CITAS ************
@app.post("/cita")
def agregar_cita_view(cita: CitaBase):
    nueva_cita = agregar_cita(cita.fecha_hora,cita.paciente, cita.medico)
    if nueva_cita is None:
        raise HTTPException(status_code=400, detail="Error al crear la cita")
    return {"mensaje": "Cita agregado", "cita": nueva_cita.paciente}

@app.put("/cita/{cita_id}")
def actualizar_cita_view(cita_id: int, cita: CitaBase):
    cita_actualizada = actualizar_cita(
        cita_id,
        cita.fecha_hora,
        cita.paciente,
        cita.medico
    )
    if cita_actualizada is None:
        raise HTTPException(status_code=404, detail="Cita no encontrado o no se pudo actualizar")
    return {"mensaje": "Cita actualizado", "cita": cita_actualizada.paciente}

@app.get("/citas")
def obtener_citas_view():
    citas = obtener_citas()
    citas_lista = [{
        "fecha_hora": cita.fecha_hora,
        "paciente": paciente_nombre,
        "medico": medico_nombre
    }
    for cita,paciente_nombre,medico_nombre in citas
    ]
    if citas_lista:
        return {"citas": citas_lista}
    else:
        return {"mensaje": "No hay citas disponibles para ese pasciente en la bd"} 

@app.get("/cita/{identificacion}")
def obtener_cita_view(identificacion: int):
    cita = obtener_cita_por_id(identificacion)
    if not cita:
        #raise HTTPException(status_code=404, detail="Medico no encontrado")
        return {"mensaje": "Cita no encontrada"}
    return {"cita": cita}

@app.delete("/cita/{cita_id}")
def eliminar_cita_view(cita_id: int):
    cita_eliminada = eliminar_cita(cita_id)
    if not cita_eliminada:
        raise HTTPException(status_code=404, detail="Cita no encontrado")
    return {"mensaje": "Cita eliminada"}

#********Usuarios***********
@app.post("/usuario")
def agregar_usuario_view(usuario: UsuarioBase):
    nuevo_usuario = agregar_usuario(usuario.nombre,usuario.telefono,usuario.cargo,usuario.usuario,usuario.contrasena,usuario.email,usuario.fecha_registro)
    if nuevo_usuario is None:
        raise HTTPException(status_code=400, detail="Error al crear el usuario")
    return {"mensaje": "Usuario agregado", "usuario": nuevo_usuario.nombre}

@app.put("/usuario/{usuario_id}")
def actualizar_usuario_view(usuario_id: int, usuario: UsuarioBase):
    usuario_actualizado = actualizar_usuario(
        usuario_id,
        usuario.nombre,
        usuario.telefono,
        usuario.cargo,
        usuario.usuario,
        usuario.contrasena,
        usuario.email,
        usuario.fecha_registro,
    )
    
    # Verificar si el usuario se pudo actualizar
    if usuario_actualizado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado o no se pudo actualizar")
    
    return {"mensaje": "Usuario actualizado", "usuario": usuario_actualizado.nombre}

@app.get("/usuarios")
def obtener_usuarios_view():
    usuarios = obtener_usuarios()
    usuarios_lista = [{
        "id": usuario.id,
        "nombre": usuario.nombre,
        "telefono": usuario.telefono,
        "cargo": usuario.cargo,
        "usuario": usuario.usuario,
        "contrasena": usuario.contrasena,
        "email": usuario.email,
        "fecha_registro": usuario.fecha_registro
    }
    for usuario in usuarios
    ]
    if usuarios_lista:
        return {"usuarios": usuarios_lista}
    else:
        return {"mensaje": "No hay usuarios disponibles en esta bd"}

@app.get("/usuario/{id}")
def obtener_usuario_view(id: int):
    usuario = obtener_usuario_por_id(id)
    if not usuario:
        #raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"mensaje": "Usuario no encontrado"}
    
    usuario_lista = [{
        "id": usuario.id,
        "nombre": usuario.nombre,
        "telefono": usuario.telefono,
        "cargo": usuario.cargo,
        "usuario": usuario.usuario,
        "contrasena": usuario.contrasena,
        "email": usuario.email,
        "fecha_registro": usuario.fecha_registro
    }]
    return {"medico": usuario_lista}

@app.delete("/usuario/{usuario_id}")
def eliminar_usuario_view(usuario_id: int):
    usuario_eliminado = eliminar_usuario(usuario_id=usuario_id)
    if not usuario_eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado", "usuario": usuario_eliminado.nombre}

