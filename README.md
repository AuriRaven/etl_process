# Proceso <font color='Teal'>ETL</font> para Ingeniería de Datos 
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# <font color='teal'>OBJETIVO</font>

Crear un proceso ELT para ingeniería de datos (para dos bases de datos distintas) el cual, funcione en el siguiente orden:

### <font color='teal'>1. Extracción</font>
Se reciben archivos ```csv``` y ```json```, y con ello, extraemos información estructural sobre cómo debe ser nuestra base de datos.  Para el caso de los archivos csv, procedemos a encontrar variables que podamos conectar con variables contenidas en los archivos json. En el caso de los archivos json, recorremos las primeras llaves principales para con ello, encontrar la información que nos interesa filtrar. Los datos que utilizaremos para ejecutar un proceso ETL, pueden ser descargados dando click [aquí](https://drive.google.com/drive/folders/1UZHYYyrtbxuuJZatS_aQukX0bhAjP1iB). 

### <font color='teal'>2. Transformación</font>
Una vez que ya hemos extraído y entendido la estructura de los archivos, procedemos a transformar los datos en cada archivo a un formato más acotado y compatible para unirse con los demás archivos y con ello formar una tabla estructurada que unifique la información que nos interesa filtrar. 
### <font color='teal'>3. Carga</font>
El último paso, consiste en poder crear una base de datos que nos permita leer los datos que acabamos de transformar en tablas estructuradas. Aquí, podemos crear conexiones a partir de claves primarias y foráneas entre tablas, las cuales formaran una base de datos relacional. Por otro lado, también podemos hacer consultas estructuradas sobre la información ya transformada.  

# <font color='teal'>ESTRUCTURA DEL REPOSITORIO</font>

```
etl_process/
│
├── etl_ia_model.py
├── etl_met_cdmx.py
├── create_db.py
├── metric_script.py
│ 
└── 
```

**NOTA** Este ordenamiento de archivos, nos permitirá en un futuro construir librerías personalizadas para estandarizar los procesos ETL y automatizarlos.
------------------------------------------------------------------------------------------------------------------------------------------------------------
