import mysql.connector
from mysql.connector import Error
import subprocess

def configure_database():
    try:
        connexion = mysql.connector.connect(
            host='localhost',
            user='user',
            password='password'
        )

        if connexion.is_connected():
            cursor = connexion.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS test")
            cursor.execute("USE test")
            
            requete_table = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                password VARCHAR(100)
            )
            """
            cursor.execute(requete_table)
            
            cursor.execute("INSERT INTO users (name, password) VALUES ('admin', 'secret')")
            connexion.commit()

            commande = [
                'mysql',
                '-u', 'user',
                '-p' + 'password',
                '-D', 'test',
                '-e', 'SELECT * FROM users;'
            ]
            
            resultat = subprocess.run(commande, capture_output=True, text=True, check=True)
            print(resultat.stdout)

    except Error as e:
        print(f"Error : {e}")
    except subprocess.CalledProcessError as e:
        print(f"Subprocess Error : {e.stderr}")
    
    finally:
        if 'connexion' in locals() and connexion.is_connected():
            cursor.close()
            connexion.close()

if __name__ == "__main__":
    configure_database()