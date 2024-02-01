
<a id="section0"></a>

<div style="border-top: 4px solid black;"></div>
<br>

# FINAL PROJECT

> *Name and surnames:* Carla Marti de Miguel

> *Course:* ADVANCED PYTHON

> *Date:* 02/01/2024

<div style="border-top: 2px solid black;"></div>

<br>

> *Nota 1:* La explicación o comentarios de cada código se encuentran debajo del mismo

> *Nota 2:* Los separadores más gruesos muestran el cambio de apartado mientras que las líneas separadoras más finas muestran el cambio de subapartado o la separación del título del apartado

<div style="border-top: 4px solid black;"></div>


## 0. Table of contents

[1. Executive summary](#section1)

[2.   Installing versions of libraries](#section2)

[3.   Reading dataset](#section3)

[4.   Understanding the data](#section4)

](#section4)

[5.   Data cleaning 

Exploring data](#section5)

[6.   Feature engineering](#section6)

[7.   Exploratory Data Analysis - Data Visualization](#section7)

[8.   Predictive Model](#section8)

[9.   Communicating the findings](#section9)

[GO UP](#section0)

<div style="border-top: 4px solid black;"></div>

<a id="section1"></a>
# 1. Executive Summary

<div style="border-top: 2px solid black;"></div>

<br>
Origen del dataset url: <i>https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers?resource=download</i>

En este proyecto el CEO de un banco observa los grandes números de abandonos de los servicios bancarios de parte de sus clientes. Quiere identificar cuales son los perfiles más propensos a abandonar el banco y buscar alguna forma de evitar estos abandonos. Para hacerlo, se nos ha proporcionado un dataset con más de 20 variables y más de 10.000 clientes (tanto existentes como antiguos/attrited).

Las variables son las siguientes:

- **CLIENTNUM**: Número de identificación del cliente
- **Attrition_Flag**: Indica si el cliente ha abandonado o no el banco
- **Customer_Age**: Edad del cliente
- **Gender**: Género del cliente
- **Dependent_count**: Cantidad de personas que dependen económicamente del cliente (hijos, cónyuge o familiares)
- **Education_Level**: Nivel educativo del cliente
- **Marital_Status**: Estado civil del cliente
- **Income_Category**: Categoría de ingresos del cliente (por intervalos)
- **Card_Category**: Categoría de la tarjeta de crédito del cliente
- **Months_on_book**: Número de meses en los que el cliente ha tenido una relación con el banco
- **Total_Relationship_Count**: Cantidad total de productos financieros que el cliente tiene con el banco
- **Months_Inactive_12_mon**: Cantidad de meses de inactividad en los últimos 12 meses
- **Contacts_Count_12_mon**: Cantidad de veces que el cliente fue contactado en los últimos 12 meses
- **Credit_Limit**: Límite de crédito del cliente
- **Total_Revolving_Bal**: Saldo total de crédito rotativo del cliente
- **Avg_Open_To_Buy**: Promedio del saldo restante en una cuenta o línea de crédito después de deducir el saldo utilizado o gastado
- **Total_Amt_Chng_Q4_Q1**: Cambio porcentual de transacciones del 4º trimestre en comparación al 1r trimestre
- **Total_Trans_Amt**: Amount total de transacciones realizadas
- **Total_Trans_Ct**: Número de transacciones
- **Total_Ct_Chng_Q4_Q1**: Cambio porcentual en la cantidad de transacciones del 4º trimestre en comparación al 1r trimestre
- **Avg_Utilization_Ratio**: Ratio de utilización promedio
- **Otras**: Hay más variables que se nos han proporcionado que son un error, las eliminaremos


[GO UP](#section0)

<div style="border-top: 4px solid black;"></div>

<a id="section2"></a>
# 2. Installing versions of libraries
<div style="border-top: 2px solid black;"></div>
<br>
En primer lugar, use el siguiente comando para instalar las mismas versiones de las diferentes librerías que he usado a lo largo del proyecto.<br><br>

    pip install -r requirements.txt


<div style="border-top: 4px solid black;"></div>
<a id="section3"></a>
<br>

# 3. Reading the data 

<div style="border-top: 2px solid black;"></div>


[GO UP](#section0)

Con el siguiente comando puede leer el dataset:

    python scripts/read_data.py -r

Con el siguiente

<a id="section3"></a>

# 4. Understanding the data 

<div style="border-top: 2px solid black;"></div>


[GO UP](#section0)


Con el siguiente comando, se van a mostrar algunas características del dataset.

    python scripts/read_Data.py -u

<div style="border-top: 4px solid black;"></div>

<a id="section4"></a>
# 4. Data Cleaning

[GO UP](#section0)

A. Irrellevant variables/columns

B. Dealing with outliers

C. Mistaken data

D. Null values

E. Repeated categories

F. Wrong data type

G. Dealing with duplicates

H. Repeated usernames

<div style="border-top: 2px solid black;"></div>

### A. Irrellevant variables/columns

El creador del dataset avisa que las dos últimas columnas son un error y es recomendable eliminarlas antes de empezar cualquier proyecto. Con el siguiente comando podrás eliminarlas

    python scripts/cleaning_data.py -ir

<div style="border-top: 2px solid black;"></div>

### B. Dealing with Outliers

Mediante un script llamado outliers, dentro del directorio cleaning, se siguen los siguientes pasos:

- Se detectan outliers (he decidido ser muy flexible a la hora de determinar cuál era la distancia para que se considerara outlier para no perder mucha información válida).

- Se generará un gráfico de la dispersión para cada una de las variables con outliers, dentro de una carpeta "before", dentro de la carpeta "outliers" que se crearán en caso de no existir

- Se eliminan los outliers

- Se generará otro gráfico para cada una de las mismas variables, pero esta vez sin outliers.

    python scripts/cleaning_data.py -out


