from flask import redirect, render_template, request, session, url_for
from .database import db, Receta, Ingrediente
from datetime import datetime
from __main__ import app

counts = {}

for receta in Receta.query.all():
	counts[str(receta.id)] = 0
	
for ingrediente in Ingrediente.query.all():
	counts[str(ingrediente.recetaid)] += 1

@app.route('/share_recipe', methods = ['GET', 'POST'])
def share_recipe():
	valorRetorno = None
	
	if request.method == 'POST':
		if not request.form['nombre'] or not request.form['tiempo'] or not request.form['elaboracion']:
			valorRetorno = render_template('message.html', message="Por favor ingrese los datos requeridos")
		else:
			nueva_receta = Receta(
				nombre = request.form['nombre'],
				tiempo=request.form['tiempo'],
				elaboracion = request.form['elaboracion'],
				cantidadmegusta = 0,
				fecha=datetime.now(),
				usuarioid = session['user_id']
			)

			db.session.add(nueva_receta)
			db.session.commit()

			counts[str(nueva_receta.id)] = 0

			valorRetorno = redirect(url_for('add_ingredient', recetaid = nueva_receta.id))
	else:
		valorRetorno = render_template('share_recipe.html')

	return valorRetorno

@app.route('/add_ingredient/<recetaid>/', methods = ['GET', 'POST'])
def add_ingredient(recetaid):
	valorRetorno = None

	if request.method == 'POST':
		if not request.form['nombre'] or not request.form['unidad'] or not request.form['cantidad']:
			valorRetorno = render_template('message.html', message="Falta completar datos")
		elif counts[recetaid] >= 10:
			valorRetorno = render_template('message.html', message='No se pueden agregar mas ingredientes a esta receta')
		else:
			nuevo_ingrediente = Ingrediente(
				nombre = request.form['nombre'],
				cantidad = request.form['cantidad'],
				unidad= request.form['unidad'],
				recetaid = recetaid
			)

			db.session.add(nuevo_ingrediente)
			db.session.commit()

			counts[recetaid] += 1

			if counts[recetaid] == 10:
				valorRetorno = render_template('message.html', message='Se llego al limite de ingredientes.\nLa receta se registro automaticamente')
			else:
				valorRetorno = render_template('add_ingredient.html', recetaid=recetaid, conteo = counts[recetaid])
	else:
		valorRetorno = render_template('add_ingredient.html', recetaid=recetaid, conteo=0)
		
	return valorRetorno

@app.route('/save_recipe')
def save_recipe():
	return render_template('message.html', message='La receta se registro correctamente')
	