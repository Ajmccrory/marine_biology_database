import mysql.connector
from app import create_app
from app.routes import main as main_bp
from mysql.connector import Error

def setup_database(db_config):
    """Function to run setup.sql file to initialize the database schema."""
    try:
        # First connect without specifying the database
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['username'],
            password=db_config['password'],
            port=db_config['port']
        )
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS marine_biodiversity_db")
        cursor.execute("USE marine_biodiversity_db")

        # Load setup.sql
        with open('setup.sql', 'r') as f:
            sql_script = f.read()
        # Execute each statement
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Database setup completed successfully.")
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
    
    # Create and run the Flask app
    app = create_app(db_config)
    app.run(debug=True)

if __name__ == '__main__':
    main()
