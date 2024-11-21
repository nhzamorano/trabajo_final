from flask import Flask, render_template,redirect,jsonify,request,url_for
import requests
import json

API_BASE_URL = "http://localhost:8000"

def cargar_citas_de_hoy():
    try:
        response = requests.get(f"{API_BASE_URL}/citas_hoy")
        if response.status_code == 200:
            contenido = response.content.decode('utf-8', errors='replace')
            datos = json.loads(contenido)  # Parsea el JSON
            return datos
        else: 
            return jsonify({"error": "Error al obtener datos desde la api"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def cargar_citas_semana():
    try:
        response = requests.get(f"{API_BASE_URL}/citas_semana")
        if response.status_code == 200:
            contenido = response.content.decode('utf-8', errors='replace')
            datos = json.loads(contenido)  # Parsea el JSON
            return datos
        else: 
            return jsonify({"error": "Error al obtener datos desde la api"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def cargar_citas():
    try:
        response = requests.get(f"{API_BASE_URL}/citas")
        if response.status_code == 200:
            contenido = response.content.decode('utf-8', errors='replace')
            datos = json.loads(contenido)  # Parsea el JSON
            return datos
        else: 
            return jsonify({"error": "Error al obtener datos desde la api"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def cargar_cita_por_id(id):
    try:
        response = requests.get(f"{API_BASE_URL}/cita/{id}")
        if response.status_code == 200:
            contenido = response.content.decode('utf-8', errors='replace')
            datos = json.loads(contenido)  # Parsea el JSON
            return datos
        else: 
            return jsonify({"error": "Error al obtener datos desde la api"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Crear la app
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('citas.html')

@app.route('/citas')
def dashboard():
    return render_template('citas.html')

@app.route('/citas_hoy')
def citas_hoy():
    datos = cargar_citas_de_hoy()
    if not datos or "error" in datos:
        status_code = datos.get("status_code", 500) if isinstance(datos, dict) else 500
        return jsonify({"error": datos.get("error", "Error desconocido")}), status_code

    citas = datos.get("citas")
    if not citas:
        return jsonify({"message": "No hay citas disponibles."}), 200
    
    return render_template('proximas_citas.html', citas=citas)

@app.route('/citas_semana')
def citas_semana():
    datos = cargar_citas_semana()
    if not datos or "error" in datos:
        status_code = datos.get("status_code", 500) if isinstance(datos, dict) else 500
        return jsonify({"error": datos.get("error", "Error desconocido")}), status_code

    citas = datos.get("citas")
    if not citas:
        return jsonify({"message": "No hay citas disponibles."}), 200
    
    return render_template('citas_semana.html', citas=citas)

@app.route('/reporte_citas')
def reporte_citas():
    datos = cargar_citas()
    if not datos or "error" in datos:
        status_code = datos.get("status_code", 500) if isinstance(datos, dict) else 500
        return jsonify({"error": datos.get("error", "Error desconocido")}), status_code

    citas = datos.get("citas")
    if not citas:
        return jsonify({"message": "No hay citas disponibles."}), 200
    
    return render_template('reporte_citas.html', citas=citas)

@app.route('/agregar_citas', methods=['POST', 'GET'])
def agregar_citas():
    if request.method == 'POST':
        fecha = request.form.get('fecha_hora') 
        id_paciente = int(request.form.get('id_paciente'))
        id_medico = int(request.form.get('id_medico'))
        data = {
            'fecha_hora': fecha,
            'paciente': id_paciente,  
            'medico': id_medico       
        }
        response = requests.post(f"{API_BASE_URL}/cita", json=data)
        if response.status_code in [200, 201]:
            return redirect(url_for('index'))
        else:
            print(f"Error {response.status_code}: {response.text}")
            return jsonify({"error": "No se pudo agregar la cita."}), 500
    
    return render_template('adicionar_citas.html')

@app.route('/modificar_cita/<int:id>', methods=['GET', 'POST'])
def modificar_cita(id):
    
    datos = cargar_cita_por_id(int(id))
    if not datos or "error" in datos:
        status_code = datos.get("status_code", 500) if isinstance(datos, dict) else 500
        return jsonify({"error": datos.get("error", "Error desconocido")}), status_code

    citas = datos
    cita_i = citas['cita']
    print(cita_i)
    if not citas:
        return jsonify({"message": "No hay citas disponibles."}), 200
    
    return render_template('modificar_cita.html', cita = cita_i)




if __name__ == '__main__':
    app.run(port=5000, debug=True)