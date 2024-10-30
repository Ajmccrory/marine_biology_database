from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

db = SQLAlchemy(app)


class Researcher(db.Model):
    __tablename__ = 'researchers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    affiliation = db.Column(db.String(200))
    observations = db.relationship('Observation', back_populates='researcher')

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(200), nullable=False)
    habitat = db.Column(db.String(200))
    migratory_pattern = db.Column(db.String(200))
    seasonal_behavior = db.Column(db.String(200))
    observations = db.relationship('Observation', back_populates='species')

class Observation(db.Model):
    __tablename__ = 'observations'
    id = db.Column(db.Integer, primary_key=True)
    researcher_id = db.Column(db.Integer, db.ForeignKey('researchers.id'))
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    observation_date = db.Column(db.Date, default=date.today)
    location = db.Column(db.String(200))
    notes = db.Column(db.Text)
    
    researcher = db.relationship('Researcher', back_populates='observations')
    species = db.relationship('Species', back_populates='observations')

db.create_all()

@app.route('/')
def index():
    species = Species.query.all()
    return render_template('index.html', species=species)

@app.route('/add_species', methods=['GET', 'POST'])
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
        return redirect(url_for('index'))
    return render_template('add_species.html')

@app.route('/researcher_data/<int:id>')
def researcher_data(id):
    researcher = Researcher.query.get(id)
    return render_template('researcher_data.html', researcher=researcher)

@app.route('/species_data/<int:id>')
def species_data(id):
    species = Species.query.get(id)
    return render_template('species_data.html', species=species)

if __name__ == '__main__':
    app.run(debug=True)
