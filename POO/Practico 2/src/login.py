from __main__ import app
from flask import render_template, request, session, url_for, redirect
from .database import db, Usuario
import hashlib

def encode(password):
	return hashlib.md5(bytes(password, encoding='utf-8')).hexdigest()

@app.route('/', methods=['GET','POST'])
def home():
	valorRetorno = None

	if request.method == 'POST':
		if not request.form['email'] or not request.form['password']:
			valorRetorno = render_template('message.html', message="Por favor ingrese los datos requeridos")
		else:
			usuario_actual = Usuario.query.filter_by(correo=request.form['email']).first()
			if usuario_actual is None:
				valorRetorno = render_template('message.html', message="El correo no está registrado")
			else:
				clave = encode(request.form['password'])
				if usuario_actual.clave != clave:
					valorRetorno = render_template('message.html', message="La contraseña no es válida")
				else:
					session['user_id'] = usuario_actual.id
					session['user_name'] = usuario_actual.nombre
					valorRetorno = render_template('home.html')
	else:
		valorRetorno = render_template('home.html', usuario = None)

	return valorRetorno

@app.route('/logout')
def logout():
	del session['user_id']
	del session['user_name']
	return redirect(url_for('home'))

@app.route('/registration', methods=['GET', 'POST'])
def registration():
	valorRetorno = None
	
	if request.method == 'POST':
		if not request.form['nombre'] or not request.form['email'] or not request.form['contraseña']:
			valorRetorno = render_template('message.html', message="Los datos ingresados no son correctos...")
		else:
			nuevo_usuario = Usuario(
				nombre=request.form['nombre'],
				correo=request.form['email'],
				clave=encode(request.form['contraseña'])
			)

			db.session.add(nuevo_usuario)
			db.session.commit()

			valorRetorno = render_template('message.html', message="El usuario se registró exitosamente")
	else:
		valorRetorno = render_template('registration.html')

	return valorRetorno
		
