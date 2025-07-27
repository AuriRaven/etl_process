from sqlalchemy import create_engine
import pandas as pd

# Parámetros de conexión
usuario = 'postgres'
contraseña = 'escribe_contraseña'
host = 'localhost'
puerto = '5432'
nombre_bd = 'db_met_cdmx'

# Crear el engine
engine = create_engine(f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{nombre_bd}')

# Consulta SQL para obtener las 5 temperaturas más altas por año
consulta = """
SELECT *
FROM (
    SELECT 
        DATE(TO_TIMESTAMP(fecha, 'YYYY-MM-DD HH24:MI:SS')) AS dia,
        EXTRACT(YEAR FROM TO_TIMESTAMP(fecha, 'YYYY-MM-DD HH24:MI:SS')) AS anio,
        MAX(valor) AS temperatura_max,
        ROW_NUMBER() OVER (
            PARTITION BY EXTRACT(YEAR FROM TO_TIMESTAMP(fecha, 'YYYY-MM-DD HH24:MI:SS')) 
            ORDER BY MAX(valor) DESC
        ) AS fila
    FROM mediciones_clima
    WHERE nom_param = 'Temperatura ambiente'
    GROUP BY DATE(TO_TIMESTAMP(fecha, 'YYYY-MM-DD HH24:MI:SS')), EXTRACT(YEAR FROM TO_TIMESTAMP(fecha, 'YYYY-MM-DD HH24:MI:SS'))
) AS subconsulta
WHERE fila <= 5
ORDER BY anio, temperatura_max DESC;
"""


df_kpis = pd.read_sql_query(consulta, engine)

# Verifica los primeros resultados
print(df_kpis.head(20))

# Consulta para obtener las estaciones más frías por mes
consulta_nueva = """
WITH temperaturas AS (
    SELECT 
        DATE_TRUNC('month', fecha::timestamp) AS mes,
        id_station,
        AVG(valor) AS temp_promedio
    FROM 
        mediciones_clima
    WHERE 
        nom_param = 'Temperatura ambiente'
    GROUP BY 
        mes, id_station
),
ranking AS (
    SELECT 
        mes,
        id_station,
        temp_promedio,
        RANK() OVER (PARTITION BY mes ORDER BY temp_promedio ASC) AS posicion
    FROM 
        temperaturas
)
SELECT 
    mes,
    id_station,
    temp_promedio
FROM 
    ranking
WHERE 
    posicion = 1
ORDER BY 
    mes;
"""

# Ejecutar consulta y guardar en DataFrame
df_resultado = pd.read_sql_query(consulta_nueva, engine)

# Mostrar o guardar resultados
print(df_resultado.head(10))

