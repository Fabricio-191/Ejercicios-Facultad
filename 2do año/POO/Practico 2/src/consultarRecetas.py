from __main__ import app
from flask import render_template, request, redirect, url_for
from .database import db, Receta, Ingrediente

@app.route('/ranking')
def ranking():
	recetas = Receta.query.all()
	recetas.sort(key=lambda x: x.cantidadmegusta, reverse=True)

	return render_template('ranking.html', recetas = recetas[0:5])

@app.route('/consult_recipe_time/', methods = ['GET', 'POST'])
def consult_recipe_time():
	valorRetorno = None

	if request.method == 'POST':
		if request.form['tiempo']:
			tiempo = int(request.form['tiempo'])
			recetas_filtradas = Receta.query.filter(Receta.tiempo <= tiempo).all()
			
			if len(recetas_filtradas) == 0:
				valorRetorno = render_template('message.html', message="No se encontraron recetas")
			else:
				valorRetorno = render_template('show_recipes.html', lista = recetas_filtradas)
		else:
			valorRetorno = render_template('message.html', message="Por favor ingrese los datos requeridos")
	else:
		valorRetorno = render_template('consult_recipe_time.html')

	return valorRetorno

@app.route('/consult_recipe_ingredient', methods = ['GET', 'POST'])
def consult_recipe_ingredient():
	valorRetorno = None

	if request.method == 'POST':
		if request.form['nombre']:
			nombreIngrediente = '%' + request.form['nombre'] + '%'
			ingredientes = Ingrediente.query.filter(Ingrediente.nombre.like(nombreIngrediente)).all()
			
			if len(ingredientes) == 0:
				valorRetorno = render_template('message.html', message="No se encontro ninguna coincidencia")
			else:
				recetas_filtradas = []

				for ingrediente in ingredientes:
					if ingrediente.receta not in recetas_filtradas:
						recetas_filtradas.append(ingrediente.receta)

				valorRetorno = render_template('show_recipes.html', lista = recetas_filtradas)
		else:
			valorRetorno = render_template('message.html', message="Por favor ingrese los datos requeridos")
	else:
		valorRetorno = render_template('consult_recipe_ingredient.html')
	
	return valorRetorno
			

@app.route("/like/<receta_id>")
def like(receta_id):
	receta = Receta.query.get(receta_id)

	receta.cantidadmegusta += 1
	db.session.commit()

	return redirect(url_for('view_recipe', receta_id = receta_id))

@app.route('/view_recipe/<receta_id>')
def view_recipe(receta_id):
	select_recipe = Receta.query.get(receta_id)
	return render_template('view_recipe.html', receta = select_recipe)
