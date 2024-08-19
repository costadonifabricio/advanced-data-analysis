import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = self.connect()

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                print("Conexión exitosa a MySQL")
                return connection
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada.")

    def fetch_data(self):
        if not self.connection or not self.connection.is_connected():
            print("No hay conexión a la base de datos.")
            return pd.DataFrame()  # Devolver un DataFrame vacío en caso de error

        query = "SELECT * FROM EmployeePerformance"
        df = pd.read_sql(query, self.connection)
        return df

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def analyze_data(self):
        analysis = {}
        departments = self.df['department'].unique()

        for dept in departments:
            dept_data = self.df[self.df['department'] == dept]
            analysis[dept] = {
                'performance_score': {
                    'mean': round(float(dept_data['performance_score'].mean()), 4),
                    'median': round(float(dept_data['performance_score'].median()), 4),
                    'std': round(float(dept_data['performance_score'].std()), 4)
                },
                'salary': {
                    'mean': round(float(dept_data['salary'].mean()), 4),
                    'median': round(float(dept_data['salary'].median()), 4),
                    'std': round(float(dept_data['salary'].std()), 4)
                },
                'total_employees': dept_data.shape[0],
                'correlation_years_performance': round(float(dept_data[['years_with_company', 'performance_score']].corr().iloc[0, 1]), 4),
                'correlation_salary_performance': round(float(dept_data[['salary', 'performance_score']].corr().iloc[0, 1]), 4)
            }
        return analysis

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_histograms(self):
        departments = self.df['department'].unique()
        for dept in departments:
            dept_data = self.df[self.df['department'] == dept]
            plt.hist(dept_data['performance_score'], bins=20, alpha=0.7, label=dept)
        plt.title('Histograma del performance_score por departamento')
        plt.xlabel('Performance Score')
        plt.ylabel('Frecuencia')
        plt.legend(loc='upper right')
        plt.show()

    def plot_scatter_plots(self):
        plt.figure()
        plt.scatter(self.df['years_with_company'], self.df['performance_score'], alpha=0.5)
        plt.title('Years with Company vs Performance Score')
        plt.xlabel('Years with Company')
        plt.ylabel('Performance Score')
        plt.show()

        plt.figure()
        plt.scatter(self.df['salary'], self.df['performance_score'], alpha=0.5)
        plt.title('Salary vs Performance Score')
        plt.xlabel('Salary')
        plt.ylabel('Performance Score')
        plt.show()

# Uso de las clases
db_manager = DatabaseManager(host="localhost", user="root", password="", database="CompanyData")
data = db_manager.fetch_data()
db_manager.close_connection()

data_analyzer = DataAnalyzer(data)
analysis = data_analyzer.analyze_data()
print(analysis)

data_visualizer = DataVisualizer(data)
data_visualizer.plot_histograms()
data_visualizer.plot_scatter_plots()