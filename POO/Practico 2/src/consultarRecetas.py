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
    if request.method == 'POST':
        if request.form['tiempo']:
            tiempo = int(request.form['tiempo'])
            recetas_filtradas = Receta.query.filter(Receta.tiempo <= tiempo).all()
			
            if len(recetas_filtradas) == 0:
                return render_template('message.html', message="No se encontraron recetas")
            else:
                return render_template('show_recipes.html', lista = recetas_filtradas)
        else:
            return render_template('message.html', message="Por favor ingrese los datos requeridos")
	
    return render_template('consult_recipe_time.html')

@app.route('/consult_recipe_ingredient', methods = ['GET', 'POST'])
def consult_recipe_ingredient():
    if request.method == 'POST':
        if request.form['nombre']:
            ing_actual = Ingrediente.query.filter_by(nombre = request.form['nombre']).first()
            if ing_actual is None:
                return render_template('message.html', message="El ingrediente no se encontro")
            else:
                recetas = Receta.query.all()
                recetas_filtradas = []

                for receta in recetas:
                    for ingrediente in receta.ingrediente:
                        if ing_actual.nombre in ingrediente.nombre:
                            recetas_filtradas.append(receta)

                return render_template('show_recipes.html', lista = recetas_filtradas)
        else:
            return render_template('message.html', message="Por favor ingrese los datos requeridos")
			
    return render_template('consult_recipe_ingredient.html')

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
