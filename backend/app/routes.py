from flask import Blueprint, render_template, request, redirect, url_for
from .crud import (
    agregar_paciente, obtener_pacientes, 
    agregar_cita, obtener_citas, 
    agregar_medico, obtener_medicos
)

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/pacientes', methods=['GET', 'POST'])
def pacientes():
    if request.method == 'POST':
        identificacion = request.form['identificacion']
        nombre_completo = request.form['nombre']
        celular = request.form['celular']
        correo = request.form['correo']
        agregar_paciente(identificacion, nombre_completo, celular, correo)
        return redirect(url_for('routes.pacientes'))

    pacientes = obtener_pacientes()
    return render_template('pacientes.html', pacientes=pacientes)

@bp.route('/citas', methods=['GET', 'POST'])
def citas():
    if request.method == 'POST':
        fecha_hora = request.form['fecha_hora']
        paciente_id = request.form['paciente_id']
        medico_id = request.form['medico_id']
        agregar_cita(fecha_hora, paciente_id, medico_id)
        return redirect(url_for('routes.citas'))

    citas = obtener_citas()
    pacientes = obtener_pacientes()
    medicos = obtener_medicos()
    return render_template('citas.html', citas=citas, pacientes=pacientes, medicos=medicos)

@bp.route('/medicos', methods=['GET', 'POST'])
def medicos():
    if request.method == 'POST':
        identificacion = request.form['identificacion']
        nombre_completo = request.form['nombre_completo']
        telefono = request.form['telefono']
        especialidad = request.form['especialidad']
        agregar_medico(identificacion, nombre_completo, telefono, especialidad)
        return redirect(url_for('routes.medicos'))

    medicos = obtener_medicos()
    return render_template('medicos.html', medicos=medicos)
