
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

[5.   Data cleaning](#section5)

[6.   Exploratory Data Analysis - Data Visualization](#section6)

[7.   Feature Engineering](#section7)

[8.   Exploratory Data Analysis Once Encoded](#section8)

[9.   Predictive Model](#section9)

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

    python scripts/main.py -d FinalProject.csv

Con el siguiente

<a id="section3"></a>

# 4. Understanding the data 

<div style="border-top: 2px solid black;"></div>


[GO UP](#section0)


Con el siguiente comando, se van a mostrar algunas características del dataset.

    python scripts/main.py -d FinalProject.csv -u

<div style="border-top: 4px solid black;"></div>

<a id="section5"></a>

# 5. Data Cleaning

[GO UP](#section0)

A. Irrellevant variables/columns

B. Dealing with outliers

C. Mistaken data

D. Null values

E. Repeated categories

F. Dealing with duplicates and repeated usernames

!  Testing the data cleaning

<div style="border-top: 2px solid black;"></div>

### A. Irrellevant variables/columns

El creador del dataset avisa que las dos últimas columnas son un error y es recomendable eliminarlas antes de empezar cualquier proyecto. 

**Atención!** En caso de realizar el comando 2 veces, se perderá información relevante para el análisis. 

Con el siguiente comando podrás eliminarlas:

    python scripts/main.py -d FinalProject.csv -c -ir

<div style="border-top: 2px solid black;"></div>

### B. Dealing with Outliers

Mediante un script llamado outliers, dentro del directorio cleaning, se siguen los siguientes pasos:

- Se detectan outliers (he decidido ser muy flexible a la hora de determinar cuál era la distancia para que se considerara outlier para no perder mucha información válida).

- Se generará un gráfico de la dispersión para cada una de las variables con outliers, dentro de una carpeta "before", dentro de la carpeta "outliers" que se crearán en caso de no existir

- Se eliminan los outliers

- Se generará otro gráfico para cada una de las mismas variables, pero esta vez sin outliers.

        python scripts/main.py -d FinalProject.csv -c -out


<div style="border-top: 2px solid black;"></div>

### C. Mistaken data

Alguna variable toma valores sin sentido:

La variable **Dependent_count** representa el número de personas que dependen económicamente del usuario. Por tanto, no tiene sentido que haya usuarios con -1 personas dependientes. En conclusión, esa data está mal y vamos a eliminarla. Para no perder la información de todas esas columnas vamos a asignar un valor nulo, que posteriormente ya veremos cómo tratar.

    python scripts/main.py -d FinalProject.csv -c -md

<div style="border-top: 2px solid black;"></div>

### D. Null Values

Con el siguiente comando, observará el número de valores nulos para cada variable y se eliminarán de la siguiente forma:

- los valores nulos en variables numéricas, se reemplazarán por el promedio de la variable numérica
- los valores nulos en variables categóricas serán eliminados

        python scripts/main.py -d FinalProject.csv -c -vn

<div style="border-top: 2px solid black;"></div>

### E. Repeated Categories


Hay algunos valores de variables que representan lo mismo. 

Por ejemplo: F = f = female = Female 

    python scripts/main.py -d FinalProject.csv -c -rep

<div style="border-top: 2px solid black;"></div>

### F. Dealing with duplicates or repeated users

Con el comando a continuación se identifica y cuenta las filas duplicadas en el conjunto de datos y en caso de haber usuarios repetidos.

    python scripts/main.py -d FinalProject.csv -c -dup

### !  Testing the data cleaning

Para testear las funciones de limpieza del dataset

    pytest tests/test_cleaning_data.py

<div style="border-top: 4px solid black;"></div>

<a id="section6"></a>
# 6. Exploratory Data Analysis - Feature engineering - Data Visualization

[GO UP](#section0)

<div style="border-top: 2px solid black;"></div>

<br>Para entender la distribución de las siguientes variables puede usar el siguiente comando. 

    python scripts/main.py -d FinalProject.csv -e -pgd

Check the directory exploring_data/categoricalEDA

### A. Categorical EDA

<div style="border-top: 2px solid black;"></div>
<br>
Use el siguiente comando:

    python scripts/main.py -d FinalProject.csv -e -ceda

Con este obtendrá una imagen, un diagrama de barras para cada variable categorica.

*Interpretaciones:*

>*Interpretación 1:* La gran mayoría de usuarios no han abandonado los servicios bancarios. Nos interesaría saber qué porcentaje (lo buscaremos posteriormente).

>*Interpretación 2:* Hay una cantidad parecida de hombres y mujeres, un poco más de mujeres que hombres.

>*Interpretación 3:* La categoría de clientes más frecuente es la de graduados. También tienen muchos clientes que han terminado el High School, clientes de los que se desconoce el grado de educación y clientes no educados. Los grupos menos frecuentes son por tanto: College, Post-Graduate y Doctorate.

>*Interpretación 4:* La mayoría de los clientes están o casados o solteros. 

>*Interpretación 5:* Las categorías de income más frecuentes son las de incomes bajos. La categoría más frecuente es la de incomes altos.

>*Interpretación 6:* La gran mayoría tiene la tarjeta Blue, con una frecuencia mucho mayor que las demás opciones.

### B. Numerical EDA

<div style="border-top: 2px solid black;"></div>

Para obtener un análisis de las variables numéricas use el siguiente comando:

    python scripts/main.py -d FinalProject.csv -e -neda

*Interpretaciones:*

>*Interpretación 1:* La distribución de la edad sigue una distribución Normal, teniendo la media en los 46 años, aproximadamente.
    
>*Interpretación 2:* La cantidad de personas dependientes económicamente también sigue una distribución Normal. Lo más frecuente es que haya 2 o 3 personas dependientes.

>*Interpretación 3:* Los meses de contrato más frecuentes son 36 meses, aproximadamente.

>*Interpretación 4:* Normalmente los clientes tienen 3 o 4 productos del banco. Es menos frecuente tener 1 o 2. 

>*Interpretación 5:* Lo normal es estar inactivo 1,2 o 3 meses al año. Es inusual estar inactivo durante un periodo más largo de tiempo.

>*Interpretación 6:* El número de contactos hechos en el último año más usual son 2 o 3 contactos.
    
>*Interpretación 7:* El límite de crédito suele ser bajo. A medida que sube el límite de crédito baja la frecuencia de este.
    
>*Interpretación 8:* Mucha gente tiene Revolving Balance = 0. No obstante, aquellos que si tienen suelen tener unos 1500 aproximadamente (sigue una Distribución Normal).

>*Interpretación 9:* Average Open_To_Buy también suelen ser bajos, los altos son muy poco frecuentes.
    
>*Interpretación 10:* La Total Amount Change Q1 to Q4 suelen ser inferiores a 1. Una minoría poco significativa llega al 2 o más.
    
>*Interpretación 11:* Total transactions amount suelen ser bajas (menos de 6.000)
    
>*Interpretación 12:* Total transition count: mayoritariamente se hacen de 60 a 80 transacciones, aproximadamente.
        
>*Interpretación 13:* La variable Total_Ct_Chng_Q4_Q1 suele ser inferior a 1, igual que la variable Total Amount Change Q1 to Q4. Una minoría poco significativa llega al 2 o más.

>*Interpretación 14:* El average utilization ratio suele ser bajo (10% o menos). Luego se distribuye más o menos uniformemente para los demas porcentajes.

<div style="border-top: 4px solid black;"></div>

<a id="section7"></a>
# 7. Feature engineering

[GO UP](#section0)

- A. Creating new variables with the existing ones
- B. Encoding categorical variables

<div style="border-top: 2px solid black;"></div>

### A. Creating new variables with the existing ones
<div style="border-top: 2px solid black;"></div>

Para crear nuevas columnas a partir de las ya existentes, por favor, use el siguiente comando:

    python scripts/main.py -d FinalProject.csv -fe -nvar

En pantalla podrá observar que se han creado 2 variables:

* Total_Trans_Amt  / Total_Trans_Ct = Avg_Trans_Amt  

* Avg_Utilization_Ratio * 100 = Avg_Utilization_Ratio_Percentage

<div style="border-top: 2px solid black;"></div>

### B. Encoding categorical variables
<div style="border-top: 2px solid black;"></div>

A continuación vamos a codificar algunas de las variables categoricas para poder incluirlas en el gráfico de correlaciones, por ejemplo.

- Label Encoding
- One Hot Encoding

        python scripts/main.py -d FinalProject.csv -fe -enc

Vemos que se ha creado una columna (que toma valor 0 o 1) para cada una de las categorías. El tipo de data de estas nuevas columnas es muy simple_ uint8, ya que solamente debe tomar 0s o 1s. También vemos que las variables iniciales (que tomaban como valores cada una de las categorías) ya no están. 

<div style="border-top: 4px solid black;"></div>

<a id="section7"></a>
# 8. Exploratory Data Analysis Once Encoded

[GO UP](#section0)

- A. Deciding what to analyze
- B. Graphical representations to develop analysis

<div style="border-top: 2px solid black;"></div>
<br>
Recordemos que el problema u **objetivo inicial es identificar aquellos perfiles o aquellas características de las personas que abandonan los servicios bancarios** para poder identificarlos antes de que hagan el abandono. Por tanto, **cómo se relacionen las otras variables no será de nuestro interés para este análisis**, aunque podrían haber relaciones muy fuertes y determinantes.

    python scripts/main.py -d FinalProject.csv -ee -corr

Se genera una carpeta llamada correlations, en donde podemos observar como se relaciona la variable '!ATTRITION_FLAG!' con las demás. Con esto podremos concluir que factores hacen que sea más probable que un cliente abandone el banco.

*Interpretaciones:*

Las variables Total_Relationship_Count, Months_Inactive_12_mon, Contacts_Count_12_mon, CLIENTNUM, Total_Trans_Amt, Total_Trans_Ct Total_Revolving_Bal, Total_Amt_Chng_Q4_Q1, Total_Ct_Chng_Q4_Q1 y Avg_Utilization_Ratio muestran correlaciones con la variable de interés, Attrition_Flag, lo que indica la necesidad de crear gráficos para explorar estas relaciones. 

### B. Graphical representation
<div style="border-top: 2px solid black;"></div>

Para obtener una carpeta con las relaciones con Attrition_Flag use el siguiente comando:

    python scripts/main.py -d FinalProject.csv -ee -g

*Interpretación:*

>***Interpretación 1:*** Unas características que pueden ser útiles para identificar a los perfiles que pueden abandonar el banco son: 1- Realizan pocas transacciones (50 o menos), 2- La cantidad total de dinero movido en transacciones es bajo. 

>***Porcentajes relevantes:*** El 60,8% de los clientes que abandonan solamente hacen transacciones entre 500 y 2500 unidades monetarias. El 80,4% de los que abandnan han hecho menos de 4500 unidades monetarias. Solamente un 0,1% de los clientes que ha abandonado ha hecho más de 10500 unidades monetarias en transacciones. El 60,4% de clientes que abandonan han hecho entre 30 y 50 transacciones.El 93,1% de los que abandonan han hecho menos de 70 transacciones. En comparación, el 49% de los clientes existentes han hecho menos de 70 transacciones (un 44,1% menos, es decir, una gran diferencia).

>***Interpretación 2:*** Los consumidores que no abandonan el banco tienen en media 4 productos, mientras que la media de los clientes que abandonaron es de 3. 
He hechó gráficos con el % de abandonos y el % de no abandonos para cada cantidad de productos porque el gráfico con el recuento de clientes difícil de interpretar. Estos gráficos son mucho mas interpretables: hay un porcentaje mayor de abandonos en los clientes con 2, 1 y 3 productos en este orden en comparación con los porcentajes de los grupos 4, 5 y 6 productos.

>***Porcentajes relevantes 2:*** En el grupo de clientes con 2 productos hay una tasa de abandono del 27,9%. Para el grupo de 1 producto, el 25,7% de clientes abandonaron. En cambio, en los grupos de clientes con 4, 5, 6 productos contratados, el % de abanono no llega al 12%. El grupo de 3 productos es un punto medio.

>***Interpretación 3:*** El 51.7% de los clientes que han estado activos todos los meses del último año han abandonado los servicios. No obstante este no es un dato alarmante ya que no se trata de una muestra representativa (en la categoría 0 meses de inactividad hay muy pocos usuarios). 
En cambio, en los grupos de 1, 2 y 3 meses si hay una muestra representativa en donde vemos una tendencia: a más meses de inactividad, mayor es la tasa de abandono, siendo la menor la de 1 mes de inactividad con menos de un 4.5% de abandonos, y la mayor la de 3 meses con un 21.5%. El banco debería entonces preocuparse por aquellos clientes que pasan más meses inactivos.


>***Porcentajes relevantes:*** El 51,7% de los clientes que han estado activos todos los meses del último año han abandonado los servicios. A continuación, el 30% de los que han estado inactivos 4 meses han abandonado, el 21,45% de los que lo han estado 3 meses han abanonado. Cabe destacar también que menos del 4,5% de los clientes que solamente inactivos 1 meses han abandonado.


>***Interpretación 4:*** Claramente cuantos más contactos se han hecho con el banco (seguramente, más quejas), más abandonos hay.

>***Porcentajes relevantes:*** El 100% de los clientes que han contactado con el banco en el último año 6 veces han abandonado los servicios. De los clientes que han hecho 5 contactos han abandonado un 33,7% y la proporción disminuye a medida que bajan los contactos. De los clientes que no han hecho ningún contacto solamente han abandonado menos de un 1,8%.

>***Interpretación 5:*** He analizado por encima la relación con CLIENTNUM porque en la tabla de correlaciones había uan pequeña correlación, pero al hacer los gráficos rapidamente he visto que no hay.

>***Interpretación 6:*** Vemos que la distribución de abandonos tiende a tener saldos en la tarjeta de crédito bajos o nulos. Podemos decir que lo más frecuente es que las personas que cierran su contrato tienen un salgo entre -500 y 500. Todas las personas con un saldo inferior a -400 aproximadamente abandonan los servicios.

>***Porcentajes relevantes:*** Personas que abandonan con saldo entre -500 y 500 del total de personas que abandonan: 60.9%. Personas que abandonan con saldo entre -500 y 500 entre total personas entre -500 y 500: 38.4%

>***Interpretación 7:*** En la variable cambio de dinero en transacciones del trimestre 1 al 4, a mayoría de valores se mueven entre -0.25 y 1.25, no obstante, cuando hacemos el pairplot separando las categorías attrited y no, vemos que de 0.75 a 1 y de 0.75 a 0.5 la frecuencia de clientes Existentes disminuye en picado cuando la frecuencia de clientes attrited disminuye mucho menos (se mantiene más). Como tienen una forma normal aproximadamente, podemos decir que los valores de los clientes existentes están muy concentrados (varianza baja) cuando los clientes que han abandonado están más dispersos. Personas que abandonan con Total_Amt_Chng_Q4_Q1 entre 0 y 0.25 entre total personas en ese rango:  

> ***Porcentajes importantes:*** Personas que abandonan con Total_Amt_Chng_Q4_Q1 entre 0 y 0.25 entre total personas en ese rango:  100.0 %
Personas que abandonan con Total_Amt_Chng_Q4_Q1 entre 0.25 y 0.5 entre total personas en ese rango:  38.54907539118065 %
Personas que abandonan con Total_Amt_Chng_Q4_Q1 entre 0.5 y 0.75 entre total personas en ese rango:  14.331688478867196 %
Personas que abandonan con Total_Amt_Chng_Q4_Q1 entre 0.75 y 1 entre total personas en ese rango:  13.615529792396872 %
Personas que abandonan con Total_Amt_Chng_Q4_Q1 entre 1 y 1.25 entre total personas en ese rango:  19.88555078683834 %

>***Interpretación 8:*** Esta variable también sigue una distribución normal. La diferencia principal es que la media no es la misma: la media de los clientes que han abandonado es 0.55, y la de los que no han abandonado 0.74. Es decir, los clientes que abandonan tienden a tener un cambio del 1r al 4o trimestre en el número de transacciones tienden a ser más bajos.

>***Porcentajes importantes:*** Personas que abandonan con Total_Ct_Chng_Q4_Q1 entre 0 y 0.25 entre total personas en ese rango:  73.57142857142858 %
Personas que abandonan con Total_Ct_Chng_Q4_Q1 entre 0.25 y 0.5 entre total personas en ese rango:  46.85920577617328 %
Personas que abandonan con Total_Ct_Chng_Q4_Q1 entre 0.5 y 0.75 entre total personas en ese rango:  12.386195214905781 %
Personas que abandonan con Total_Ct_Chng_Q4_Q1 entre 0.75 y 1 entre total personas en ese rango:  7.656102918104802 %
Personas que abandonan con Total_Ct_Chng_Q4_Q1 entre 1 y 1.25 entre total personas en ese rango:  7.6923076923076925 %

>***Interpretación 9:*** Como podemos ver, hay dos modas para los clientes existentes (en 0% y en 60%), y una para los que abandonaron (0%). Observamos que el 65.7% de los clientes que abandonaron tenían una utilización media de entre el 0% y 10%, cuando para la misma utilización solamente hay un 34.8% de los clientes existentes.


<div style="border-top: 4px solid black;"></div>
<a id="section9"></a>
# 8. Predictive Model

[GO UP](#section0)

<div style="border-top: 2px solid black;"></div>

