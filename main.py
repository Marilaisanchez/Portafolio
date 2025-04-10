# Import
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(30), nullable = False)
    text = db.Column(db.Text, nullable = False)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')

# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    email = request.form.get('email')
    text = request.form.get('text')

    if email and text: 
        with open('form.txt', 'a') as f:
            f.write(f"FORMULARIO\n{email}\n{text}\n")

        formulario = Form(email = email, text = text)
        db.session.add(formulario)
        db.session.commit()

    return render_template('index.html', 
                           button_python=button_python,
                           button_html=button_html,
                           button_discord=button_discord,
                           button_db=button_db,
                           email=email,
                           text=text)



if __name__ == "__main__":
    app.run(debug=True)
