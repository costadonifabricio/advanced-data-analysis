import mysql.connector
from mysql.connector import Error

def create_database():
    """Create a connection to MySQL server and create a database."""
    try:
        # Establecer la conexión al servidor MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="" 
        )

        if connection.is_connected():
            print("Conexión exitosa a MySQL")
            
            cursor = connection.cursor()
            
            # Crear la base de datos si no existe
            cursor.execute("CREATE DATABASE IF NOT EXISTS CompanyData")
            print("Base de datos 'CompanyData' creada o ya existe")
    
    except Error as e:
        print(f"Error al conectar o crear la base de datos: {e}")
    
    finally:
        if connection.is_connected():
            # Cerrar la conexión
            connection.close()
            print("Conexión cerrada")

# Llamar a la función directamente
create_database()
