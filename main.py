import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Conexión exitosa a MySQL")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def create_database_and_table(self):
        if self.connection and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                
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
                print(f"Error al crear la base de datos o la tabla: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a la base de datos.")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada.")

# Uso de la clase DatabaseManager
db_manager = DatabaseManager(host="localhost", user="root", password="")
db_manager.connect()
db_manager.create_database_and_table()
db_manager.close_connection()