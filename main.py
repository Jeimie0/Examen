from flask import Flask, render_template, request

app = Flask(__name__)

# Usuarios registrados
usuarios_registrados = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        total_sin_descuento = cantidad_tarros * 9000

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'total_con_descuento': total_con_descuento
        }

    return render_template('form_ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contrasena = request.form['contrasena']

        # Verificar el nombre de usuario y la contraseña
        if nombre_usuario in usuarios_registrados and usuarios_registrados[nombre_usuario] == contrasena:
            if nombre_usuario == 'juan':
                resultado = {'mensaje': f'Bienvenido Administrador {nombre_usuario}'}
            elif nombre_usuario == 'pepe':
                resultado = {'mensaje': f'Bienvenido Usuario {nombre_usuario}'}
        else:
            resultado = {'mensaje': 'Nombre de usuario o contraseña incorrectos.'}

    return render_template('form_ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)