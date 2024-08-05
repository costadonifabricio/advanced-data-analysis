## Práctica De Librerías - Python

## Descripción

Este proyecto tiene como objetivo realizar un análisis avanzado de datos en una base de datos MySQL llamada `CompanyData`, específicamente en la tabla `EmployeePerformance`. Se utiliza Python junto con pandas para la extracción y análisis de datos, y matplotlib para la visualización de los mismos.

## Estructura del Proyecto

- **main.py**: Script principal que contiene el código para la creación de la base de datos y tabla.
- **data.py**: Script para la inserción de datos desde un archivo CSV a la base de datos.
- **view.py**: Script para la extracción, análisis y visualización de los datos.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/costadonifabricio/advanced-data-analysis.git
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias

4. Configura la base de datos MySQL:

    - Ejecuta el script `main.py` para crear la base de datos y la tabla:

        ```bash
        python main.py
        ```

    - Población de la tabla con datos ficticios usando [Mockaroo]

    - Inserta los datos en la tabla ejecutando el script `data.py`:

        ```bash
        python data.py
        ```

## Uso

1. Ejecuta el script de visualización y análisis:

    ```bash
    python view.py
    ```

2. El script realizará las siguientes acciones:
    - Extraerá los datos de la base de datos MySQL.
    - Analizará los datos calculando estadísticas como media, mediana, desviación estándar, y correlaciones.
    - Imprimirá los resultados del análisis.
    - Creará histogramas y gráficos de dispersión para la visualización de los datos.


