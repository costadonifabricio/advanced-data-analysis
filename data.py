import pandas as pd
import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa a MySQL")
                return True
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return False

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada.")

    def insert_data_from_csv(self, csv_file):
        if not self.connection.is_connected():
            print("No hay conexión a la base de datos.")
            return

        cursor = self.connection.cursor()

        # Leer el archivo CSV
        df = pd.read_csv(csv_file)

        # Insertar los datos en la tabla
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary)
                VALUES (%s, %s, %s, %s, %s)
            """, (row['employee_id'], row['department'], row['performance_score'], row['years_with_company'], row['salary']))

        self.connection.commit()
        cursor.close()

# Uso de la clase DatabaseManager
db_manager = DatabaseManager(host="localhost", user="root", password="", database="CompanyData")
if db_manager.connect():
    db_manager.insert_data_from_csv('script.csv')
    db_manager.close_connection()