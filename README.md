<h1 align='center'>
 <b>PROYECTO FINTECH </b>
</h1>

# <h1 align="center">**`Predicción de Fraude en Transacciones Financieras`**</h1>

<p align='center'>
<img src ="images/concepto-proteccion-contra-fraude-financiero-bloqueo-tarjeta-credito-llave-maestra-fondo-claro_1182900-14964.avif" width="11000px" height="450px">
<p>

# Índice

1. [Introduccion](#introducción)
2. [Contexto y Rol a Desarrollar](#contexto-y-rol-a-desarrollar)
3. [Fuente de Datos](#fuente-de-datos)
4. [Diccionario](#Diccionario)
5. [ETL y EDA](#etl-y-eda)
6. [Conclusiones](#Conclusiones)
7. [Colaboradores](#Equipo)
8. [Tecnologías Utilizadas](#tecnologías-utilizadas)


## **Introducción:**


En el contexto de la creciente digitalización de los servicios financieros, la detección de fraudes en transacciones electrónicas se ha convertido en un desafío crítico para las empresas ``fintech`` y los proveedores de servicios de pago. El fraude financiero, que puede implicar la manipulación indebida de transacciones con tarjetas de crédito, cuentas bancarias o sistemas de pagos electrónicos, no solo afecta la integridad financiera de las empresas, sino también la confianza de los usuarios en las plataformas.

El objetivo de este proyecto es desarrollar un modelo predictivo capaz de identificar transacciones fraudulentas en tiempo real utilizando técnicas avanzadas de aprendizaje automático y análisis de comportamiento. A través del análisis de un conjunto de datos históricos de transacciones, este proyecto buscará detectar patrones y anomalías que caracterizan las actividades fraudulentas, proporcionando a la empresa una herramienta eficiente para mitigar riesgos financieros.

El modelo será entrenado para aprender a diferenciar entre transacciones legítimas y fraudulentas, basándose en características clave como el comportamiento del usuario, la geolocalización, los montos transaccionales, el tipo de comercio y otras variables relevantes. Se implementarán diversas etapas de procesamiento de datos y análisis exploratorio (ETL y EDA) para limpiar, transformar y comprender los datos antes de aplicar algoritmos de machine learning que proporcionen predicciones precisas y accionables.

Este proyecto no solo busca implementar una solución tecnológica innovadora, sino también aportar valor estratégico a la empresa al mejorar la capacidad de respuesta ante fraudes, reducir pérdidas económicas, y fortalecer la confianza de los clientes en sus transacciones financieras.


# **Contexto y Rol a desarrollar**

El proyecto se enmarca en el contexto del sistema financiero de los `Estados Unidos`, abarcando los ``51 estados``. La cantidad de transacciones digitales ha crecido exponencialmente en los últimos años, impulsada por la digitalización del comercio y el auge de plataformas de pagos electrónicos. Este incremento ha generado un aumento proporcional en los intentos de fraude, convirtiéndose en una prioridad para las empresas ``fintech`` desarrollar sistemas robustos de detección y prevención de fraudes financieros.

El análisis cubrirá un período específico que comprende desde ``enero de 2019 hasta junio de 2020``, un intervalo en el cual la adopción de pagos electrónicos aceleró debido, en parte, a la creciente penetración de las tecnologías móviles y la pandemia global, que impulsó el uso del comercio electrónico. Este contexto genera un escenario único para estudiar patrones de fraude relacionados con los cambios en los hábitos de consumo y la presión sobre los sistemas de pago digitales.

### **Rol a Desarrollar:**
Como Científico de Datos en este proyecto, la principal responsabilidad será desarrollar un sistema predictivo que detecte actividades fraudulentas. Esto incluye las siguientes tareas clave:

- **Exploración de datos (EDA):** Analizar y comprender las características de las transacciones financieras en los diferentes estados, identificando patrones y posibles anomalías.
- **Ingeniería de características:** Crear nuevas variables relevantes a partir de los datos disponibles que puedan mejorar la capacidad del modelo para diferenciar entre transacciones legítimas y fraudulentas.
- **Modelado predictivo:** Desarrollar y entrenar un modelo de machine learning que pueda clasificar de manera precisa las transacciones como legítimas o fraudulentas. 
- **Evaluación y optimización:** Validar el desempeño del modelo utilizando métricas clave y optimizarlo para maximizar su precisión y reducir falsos positivos.


## **Fuente de Datos**
El conjuntos de datos de transacciones financieras
fraudulentas se obtuvo a traves de repositorios de datos abiertos como el conjunto de datos de Fraude
de Tarjetas de Crédito en Kaggle.


Link: https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset 

## **Diccionario**

El conjunto de datos utilizado en este proyecto contiene información detallada sobre transacciones financieras realizadas en diferentes comercios y estados dentro de los Estados Unidos. Cada fila del dataset representa una transacción, con una variedad de variables que describen tanto la transacción como al titular de la tarjeta, el comerciante, y la geolocalización asociada. A continuación, se presenta una descripción de cada una de las variables clave:

1. **trans_date_trans_time:** Marca de tiempo de la transacción (fecha y hora en que ocurrió la transacción).  
2. **cc_num:** Número de la tarjeta de crédito (hash o anonimizado).  
3. **merchant:** Comerciante o tienda donde ocurrió la transacción.  
4. **category:** Tipo de transacción (ej. supermercado, entretenimiento).  
5. **amt:** Monto de la transacción.  
6. **first:** Nombre del titular de la tarjeta.  
7. **last:** Apellido del titular de la tarjeta.  
8. **gender:** Género del titular de la tarjeta.  
9. **street:** Detalles de la dirección del titular de la tarjeta.  
10. **city:** Ciudad donde reside el titular de la tarjeta.  
11. **state:** Estado donde reside el titular de la tarjeta.  
12. **zip:** Código postal del titular de la tarjeta.  
13. **lat:** Latitud de la dirección del titular de la tarjeta.  
14. **long:** Longitud de la dirección del titular de la tarjeta.  
15. **city_pop:** Población de la ciudad del titular de la tarjeta.  
16. **job:** Ocupación o profesión del titular de la tarjeta.  
17. **dob:** Fecha de nacimiento del titular de la tarjeta.  
18. **trans_num:** Identificador único de la transacción.  
19. **unix_time:** Marca de tiempo de la transacción en Unix (segundos desde la época Unix, útil para cálculos de tiempo).  
20. **merch_lat:** Latitud de la ubicación del comerciante.  
21. **merch_long:** Longitud de la ubicación del comerciante.  
22. **is_fraud:** Indicador de si la transacción fue fraudulenta (1 para fraudulenta, 0 para no fraudulenta).  
23. **merch_zipcode:** Código postal del comerciante.

## **ETL Y EDA**




## **Conclusiones**


## **Equipo**


<table>
  <thead>
    <tr>
      <th>Nombre</th>
      <th>Correo electrónico</th>
      <th>Rol</th>
      <th>LinkedIn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Natalia Lopera</td>
      <td>loperanataliaal@gmail.com</td>
      <td>Data Science | Data Analyst</td>
      <td><a href="https://www.linkedin.com/in/cesar-augusto-garc%C3%ADa-galeano-2190bb200//" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn logo" width="20" height="20"></a></td>
    </tr>
    <tr>
      <td>Jose Castro Rodriguez</td>
      <td>jcastroprogrammer@hotmail.com</td>
      <td>Data Science | Data Analyst</td>
      <td><a href="https://www.linkedin.com/in/ana-florencia-sandoval-876615286/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn logo" width="20" height="20"></a></td>
    </tr>
    <tr>
      <td>Blas Fernando Pacios</td>
      <td>blasferp@gmail.com</td>
      <td>Data Science | Data Analyst</td>
      <td><a href="https://www.linkedin.com/in/blas-fernando-pacios-14a46a280//" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn logo" width="20" height="20"></a></td>
    </tr>
  </tbody>
</table>


## **Tecnologías utilizadas**

![Static Badge](https://img.shields.io/badge/PowerBI-gray?style=flat&logo=powerbi)
![Static Badge](https://img.shields.io/badge/Python-gray?style=flat&logo=python)
![Static Badge](https://img.shields.io/badge/-Pandas-gray?style=flat&logo=pandas)
![Static Badge](https://img.shields.io/badge/-Matplotlib-gray?style=flat&logo=matplotlib)
![Static Badge](https://img.shields.io/badge/-Seaborn-gray?style=flat&logo=seaborn)
![Static Badge](https://img.shields.io/badge/-Jupyter_Notebook-gray?style=flat&logo=jupyter)
![Static Badge](https://img.shields.io/badge/Visual_Studio_Code-gray?style=flat&logo=visual%20studio%20code&logoColor=white)

---
