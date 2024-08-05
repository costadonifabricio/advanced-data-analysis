import pandas as pd
import mysql.connector

def insert_data_from_csv(csv_file):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="CompanyData"
    )
    
    cursor = connection.cursor()
    
    # Leer el archivo CSV
    df = pd.read_csv(csv_file)
    
    # Insertar los datos en la tabla
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['employee_id'], row['department'], row['performance_score'], row['years_with_company'], row['salary']))
    
    connection.commit()
    cursor.close()
    connection.close()

# Llamar a la función con el archivo CSV
insert_data_from_csv('script.csv')
