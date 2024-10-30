import mysql.connector
from app import create_app
from mysql.connector import Error

def setup_database(db_config):
    """Function to run setup.sql file to initialize the database schema."""
    try:
        print("Attempting to connect to MySQL...")
        # First connect without specifying the database
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['username'],
            password=db_config['password'],
            port=db_config['port'],
            auth_plugin='mysql_native_password'
        )
        cursor = conn.cursor()  # Enable multiple statement execution
        
        # Load setup.sql
        print("Reading setup.sql file...")
        with open('setup.sql', 'r') as f:
            sql_script = f.read()
        print("SQL Script content:")
        print(sql_script)
            
        # Execute the entire script
        print("Executing SQL script...")
        results = cursor.execute(sql_script, multi=True)
        if results:
            for result in results:
                print(f"Executed statement: {result}")
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Database setup completed successfully.")
    except Error as e:
        print(f"Error setting up database: {e}")
    except FileNotFoundError:
        print("Error: setup.sql file not found. Make sure it exists in the correct location.")

def get_db_config():
    """Prompt user for database connection details."""
    print("Please enter your MySQL database connection details:")
    db_config = {
        'username': input("Username (deafult root): ") or 'root',
        'password': input("Password: "),
        'host': input("Host (default localhost): ") or 'localhost',
        'port': input("Port (default 3306): ") or '3306',
        'database': 'marine_biodiversity_db'
    }
    return db_config

def main():
    db_config = get_db_config()
    setup_database(db_config)
    
    # Create and run the Flask app
    app = create_app(db_config)
    app.run()

if __name__ == '__main__':
    main()
