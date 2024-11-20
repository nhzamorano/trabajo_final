from flask import Flask, render_template, request, redirect, url_for, flash
import requests

API_BASE_URL = "http://localhost:8000"  # Base URL del backend FastAPI

def create_frontend_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "sistemas"

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/medicos")
    def medicos():
        response = requests.get(f"{API_BASE_URL}/medicos")
        medicos = response.json().get("medicos", [])
        return render_template("medicos.html", medicos=medicos)

    @app.route("/agregar_medico", methods=["GET", "POST"])
    def agregar_medico():
        if request.method == "POST":
            data = {
                "identificacion": int(request.form["identificacion"]),
                "nombre_completo": request.form["nombre_completo"],
                "telefono": request.form["telefono"],
                "especialidad": request.form["especialidad"]
            }
            response = requests.post(f"{API_BASE_URL}/medico", json=data)
            if response.status_code == 200:
                flash("Médico agregado exitosamente", "success")
            else:
                flash("Error al agregar el médico", "danger")
            return redirect(url_for("medicos"))
        return render_template("agregar_medico.html")

    return app
