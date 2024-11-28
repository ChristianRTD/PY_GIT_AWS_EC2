from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, Mundo!"

@app.route('/progra')
def progra():
    return "¡PROGRAMACION DISTRIBUIDA!"

if __name__ == '__main__':
    app.run()
