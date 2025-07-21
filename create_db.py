# Importamos las librerías necesarias
from sqlalchemy import create_engine
import pandas as pd

# Importamos el DataFrame transformado
df_final = pd.read_csv('tabla_fac_estructurada.csv')


# Parámetros de conexión
usuario = 'postgres'
contraseña = '6Humanos36'
host = 'localhost'
puerto = '5432'
nombre_bd = 'db_met_cdmx'

# Prueba de conexión a la base de datos PostgreSQL
try:
    engine = engine = create_engine(f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{nombre_bd}')
    conn = engine.connect()
    print("¡Conexión exitosa!")
    conn.close()
except Exception as e:
    print("Error al conectar:", e)

# Crear engine de conexión a PostgreSQL
engine = engine = create_engine(f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{nombre_bd}')

# Guardar el DataFrame como una tabla SQL
df_final.to_sql('mediciones_clima', engine, if_exists='replace', index=False)

# Verificamod que la tabla exista y contamos sus registros
try:
    df_check = pd.read_sql("SELECT COUNT(*) AS total FROM mediciones_clima", engine)
    print("La tabla existe y tiene:", df_check['total'].iloc[0], "registros.")
except Exception as e:
    print("Error al consultar la tabla:", e)