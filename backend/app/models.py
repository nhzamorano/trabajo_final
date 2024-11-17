from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Config
from sqlalchemy.sql import func

# Configuración de SQLAlchemy
engine = create_engine(Config.DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Declarativo base de SQLAlchemy
Base = declarative_base()

# Definir el modelo Medico
class Medico(Base):
    __tablename__ = 'medicos'
    identificacion = Column(Integer, primary_key=True)
    nombre_completo = Column(String(50), nullable=False)
    telefono = Column(String(50),nullable=False)
    especialidad = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Medico(nombre='{self.nombre_completo}', especialidad='{self.especialidad}')>"

class Paciente(Base):
    __tablename__ = 'pacientes'
    identificacion = Column(Integer, primary_key=True)
    nombre_completo = Column(String(50), nullable=False)
    celular = Column(String(50),nullable=False)
    correo = Column(String(50), nullable=False)

class Cita(Base):
    __tablename__ = 'citas'
    id = Column(Integer, primary_key=True)
    fecha_hora = Column(String(100), nullable=False)
    paciente = Column(Integer,nullable=False)
    medico = Column(Integer, nullable=False)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(100),nullable=False)
    cargo = Column(String(255),nullable=True)
    usuario = Column(String(100), nullable=False,unique=True)
    contrasena = Column(String(255),nullable=False)
    email = Column(String(255),nullable=True,unique=True)
    fecha_registro = Column(DateTime, default=func.now())

# Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(engine)
