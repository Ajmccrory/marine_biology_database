import mysql.connector
from app import create_app
from app.routes import main as main_bp
from mysql.connector import Error

def setup_database(db_config):
    """Function to run setup.sql file to initialize the database schema."""
    try:
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['username'],
            password=db_config['password'],
            port=db_config['port']
        )
        cursor = conn.cursor()
        cursor.execute("USE marine_biodiversity_db")

        # Load setup.sql
        with open('setup.sql', 'r') as f:
            sql_script = f.read()
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Database setup completed.")
    except Error as e:
        print(f"Error setting up database: {e}")

def get_db_config():
    """Prompt user for database connection details."""
    print("Please enter your MySQL database connection details:")
    db_config = {
        'username': input("Username: "),
        'password': input("Password: "),
        'host': input("Host: "),
        'port': input("Port (default 3306): ") or '3306',
        'database': 'marine_biodiversity_db'
    }
    return db_config

def main():

    db_config = get_db_config()
    setup_database(db_config)
    # Create the Flask app
    app = create_app()

    # Set the SQLALCHEMY_DATABASE_URI directly on the app config
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymsql://{db_config['username']}:{db_config['password']}@"
        f"{db_config['host']}:3306/{db_config['database']}"
    )

    app.register_blueprint(main_bp)
    # Run the app
    app.run()

    app = create_app()






    # Run Flask app
    app.run(debug=True)

if __name__ == '__main__':
    main()
