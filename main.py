from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, Mundo!"

@app.route('/progra')
def progra():
    return "¡PROGRAMACION DISTRIBUIDA!"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Cambia el host y el puerto.
