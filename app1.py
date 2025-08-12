from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agregar_persona", methods=["POST"])
def agregar_persona():
    nombre = request.form['nombre']
    edad = request.form['edad']
    correo = request.form['correo']

    data = {
        'nombre': nombre,
        'edad': edad,
        'correo': correo
    }
    return render_template("confirmacion.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
