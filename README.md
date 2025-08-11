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
├── ia_model.ipynb
├── met_cdmx.ipynb
├── create_db.py
├── metric_script.py
├── tabla_ia_estructurada.zip
└── 
```
------------------------------------------------------------------------------------------------------------------------------------------------------------

# <font color='violet'>I. Datos Meteorológicos de CDMX</font>

Corresponde a un conjunto de datasets que contienen información meteorológica de la CDMX (2013-2023). Es este caso, nos enfocaremos en los datos capturados por la estación de captura FES Acatlán.
## 1. Descargar Datos

Descargamos la carpeta llamada ***datos***. En esta carpeta leemos las subcarpetas  ***catálogos*** e ***históricos*** las cuales, contienen archivos csv y json respectivamente
## 2. Crear Proceso ETL

Recorremos cada archivo json en la carpeta *históricos*, para entender su estructura y anidamiento de llaves (como los diccionarios en Python).  Para los archivos csv, necesitamos comprender las variables, sus valores únicos y el tipo de dato que representan. 
## 3. Filtrar Datos (FES Acatlán)

Una vez que tenemos una idea de como está anidada la información en los archivos json, procedemos a filtrar la información que corresponde a las capturas de la estación Fes Acatlán (etiquetada como **"FAC"**, segun los csv de catálogos). Procedemos a conectar los csv con la información filtrada de los archivos json. Exportamos estos datos transformados a una tabla estructurada. 
## 4. Creación de Base de Datos (PosgreSQL)

Utilizando la librería ```sqlalchemy``` las cual, nos permitirá comunicarnos directamente con PosgreSQL(PgAdmin), en donde creamos una base de datos, la cuál contendrá la tabla estructurada que generamos en el paso anterior. 
## 5. Consultas SQL

Finalmente, una vez creada nuestra base de datos con la tabla, podemos proceder a hacer consultas estructuradas para extraer métricas o KPI's importantes respecto a nuestros datos.
### 5.1. Consulta de Días más Calurosos por Año

Se generaron los siguientes resultados al generar la consulta y restringirla a los primeros 20 registros generados, es decir, los 5 días más calurosos de los primeros 4 años registrados en la estación de captura FES Acatlán. 

```
           dia    anio  temperatura_max  fila
0   2013-04-18  2013.0             33.4     1
1   2013-05-22  2013.0             32.4     2
2   2013-04-16  2013.0             32.2     3
3   2013-04-15  2013.0             32.0     4
4   2013-04-14  2013.0             31.4     5
5   2014-03-23  2014.0             33.3     1
6   2014-04-13  2014.0             32.9     2
7   2014-03-28  2014.0             32.5     3
8   2014-04-14  2014.0             31.8     4
9   2014-05-11  2014.0             31.4     5
10  2015-04-25  2015.0             32.0     1
11  2015-05-10  2015.0             31.6     2
12  2015-04-21  2015.0             31.5     3
13  2015-04-20  2015.0             31.4     4
14  2015-04-08  2015.0             31.2     5
15  2016-05-25  2016.0             33.6     1
16  2016-05-02  2016.0             33.5     2
17  2016-05-20  2016.0             33.4     3
18  2016-05-08  2016.0             33.0     4
19  2016-05-21  2016.0             32.4     5
```

Podemos notar que, los meses de marzo, abril y mayo tienden a tener temperaturas más altas que los demás meses. 
### 5.2. Consulta de Estaciones más Frías por Mes

En la siguiente consulta, se pide mostrar la estación más frías por mes. En este caso, tendremos la misma estación en cada registro, pues nuestros datos están restringidos a la estación FES Acatlán. Para que pueda haber más variedad, necesitamos permitir que haya información de al menos otra estación. 

```
         mes    id_station  temp_promedio
0 2013-04-01  484150570109      19.897739
1 2013-05-01  484150570109      19.220029
2 2013-06-01  484150570109      18.321111
3 2013-07-01  484150570109      17.497577
4 2013-08-01  484150570109      17.239919
5 2013-09-01  484150570109      16.672419
6 2013-10-01  484150570109      17.042417
7 2013-11-01  484150570109      15.109458
8 2013-12-01  484150570109      14.473261
9 2014-01-01  484150570109      12.738710
```
# <font color='violet'>II. Datos de Modelo IA</font>

## 1. Descargar Datos

De la carpeta llamada ***resultados***, descargamos y leemos el único archivo json. 
## 2. Crear Proceso ETL

De igual manera como lo hicimos con los datos meteorológicos, revisamos la forma en la que las llaves del archivo json están anidadas. Con ello, podremos entender como filtrar la información de las marcas que nos interesan. Una vez que los datos están filtrados, podemos proceder a transformarlos en una tabla estructurada. 

