from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Species

main = Blueprint('main', __name__)

@main.route('/')
def index():
    species_list = Species.query.all()
    return render_template('index.html', species=species_list)

@main.route('/add_species', methods=['GET', 'POST'])
def add_species():
    if request.method == 'POST':
        species = Species(
            common_name=request.form['common_name'],
            scientific_name=request.form['scientific_name'],
            habitat=request.form['habitat'],
            migratory_pattern=request.form['migratory_pattern'],
            seasonal_behavior=request.form['seasonal_behavior']
        )
        db.session.add(species)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_species.html')
