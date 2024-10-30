from app import db

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
    observation_date = db.Column(db.Date)
    location = db.Column(db.String(200))
    notes = db.Column(db.Text)
    
    researcher = db.relationship('Researcher', back_populates='observations')
    species = db.relationship('Species', back_populates='observations')
