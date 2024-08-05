import mysql.connector
from mysql.connector import Error

def create_database_and_table():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="" 
        )

        if connection.is_connected():
            print("Conexión exitosa a MySQL")
            cursor = connection.cursor()
            
            # Crear la base de datos
            cursor.execute("CREATE DATABASE IF NOT EXISTS CompanyData")
            cursor.execute("USE CompanyData")
            
            # Crear la tabla si no existe
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS EmployeePerformance (
                id INT AUTO_INCREMENT PRIMARY KEY,
                employee_id INT,
                department VARCHAR(255),
                performance_score DECIMAL(5,2),
                years_with_company INT,
                salary DECIMAL(10,2)
            )
            """)
            print("Tabla 'EmployeePerformance' creada o ya existe")
            
    except Error as e:
        print(f"Error al conectar o crear la base de datos o tabla: {e}")
    
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")

# Llama a la función directamente
create_database_and_table()
