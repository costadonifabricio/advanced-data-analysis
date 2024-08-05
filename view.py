import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

def fetch_data():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="CompanyData"
    )
    
    # Definir la consulta SQL para extraer todos los datos de la tabla EmployeePerformance
    query = "SELECT * FROM EmployeePerformance"
    
    # Ejecutar la consulta y almacenar los resultados en un DataFrame de pandas
    df = pd.read_sql(query, connection)
    
    # Cerrar la conexión a la base de datos
    connection.close()
    
    # Devolver el DataFrame con los datos
    return df

# Función para analizar los datos
def analyze_data(df):
  
    analysis = {}
    
    # Obtener una lista única de todos los departamentos en los datos
    departments = df['department'].unique()

    # Iterar sobre cada departamento
    for dept in departments:
        
        dept_data = df[df['department'] == dept]
        
        # Calcular las estadísticas para el departamento actual y almacenarlas en el diccionario
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
            'correlation_years_performance': round(float(dept_data[['years_with_company', 'performance_score']].corr().iloc[0,1]), 4),
            'correlation_salary_performance': round(float(dept_data[['salary', 'performance_score']].corr().iloc[0,1]), 4)
        }

    # Devolver el diccionario con los resultados del análisis
    return analysis

# Función para crear histogramas
def plot_histograms(df):
    
    departments = df['department'].unique()
    
    for dept in departments:
        dept_data = df[df['department'] == dept]
        
        # Crear un histograma del performance_score para el departamento actual
        plt.hist(dept_data['performance_score'], bins=20, alpha=0.7, label=dept)
    
    # Configurar el título y etiquetas del histograma
    plt.title('Histograma del performance_score por departamento')
    plt.xlabel('Performance Score')
    plt.ylabel('Frecuencia')
    plt.legend(loc='upper right')
    
    # Mostrar el histograma
    plt.show()

# Función para crear gráficos de dispersión
def plot_scatter_plots(df):
   
    plt.figure()
    plt.scatter(df['years_with_company'], df['performance_score'], alpha=0.5)
    plt.title('Years with Company vs Performance Score')
    plt.xlabel('Years with Company')
    plt.ylabel('Performance Score')
    plt.show()

    # Crear un gráfico de dispersión de salary vs performance_score
    plt.figure()
    plt.scatter(df['salary'], df['performance_score'], alpha=0.5)
    plt.title('Salary vs Performance Score')
    plt.xlabel('Salary')
    plt.ylabel('Performance Score')
    plt.show()

df = fetch_data()

# Analizar los datos
analysis = analyze_data(df)

# Imprimir los resultados del análisis
print(analysis)

# Crear y mostrar histogramas
plot_histograms(df)

# Crear y mostrar gráficos de dispersión
plot_scatter_plots(df)
