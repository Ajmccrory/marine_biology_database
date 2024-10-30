# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(db_config=None):
    app = Flask(__name__)
    
    # Configure SQLAlchemy
    if db_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            f"mysql+pymysql://{db_config['username']}:{db_config['password']}@"
            f"{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
