from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Manejo del formulario
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    # Aquí puedes guardar los datos en una base de datos
    print(f"Nombre: {name}, Email: {email}")
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
