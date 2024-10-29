import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
# import pandas_profiling

from streamlit_option_menu import option_menu
# from streamlit_pandas_profiling import st_profile_report
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from graficos_funcion import graficas_barras, graficas_barras_apiladas, graficas_barras_agrupadas
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

##########################################################################################################################


#################################################################################################################################

# Obtener la fecha actual en español
meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

dias_semana = [
    "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
]

now = datetime.now()
current_date = f"{dias_semana[now.weekday()]}, {now.day} de {meses[now.month - 1]} de {now.year}"


# Mostrar la fecha en la barra lateral
st.sidebar.title(f'📅 Fecha:')
st.sidebar.markdown(
    f'<h2 style="color: #333;">{current_date}</h2>',
    unsafe_allow_html=True
)

# Cambiar el fondo de color del sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #000;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Separar con línea horizontal
st.sidebar.markdown("<hr>", unsafe_allow_html=True)


# Configuración del menú principal en la barra lateral
with st.sidebar:
    selected = option_menu(
        menu_title='Menú Principal',
        options=[
            'Principal', 
            'Sistema de Detección de Fraude', 
            'Transacciones', 
            'Análisis General', 
            'Análisis Tiempo', 
            'Análisis Rango Etario', 
            'Análisis Trabajo', 
            'Análisis Genero', 
            'Análisis Ubicación',
            'Análisis Categorías'
        ],
        menu_icon='gear',
        icons=[
            'house',               # Icono para "Principal"
            'search',              # Icono para "Sistema de Detección de Fraude" (lupa)
            'file-earmark-text',   # Icono para "Transacciones"
            'cash-stack',          # Icono para "Análisis Monto" (dinero)
            'clock',               # Icono para "Análisis Tiempo"
            'calendar',            # Icono para "Análisis Edad"
            'person',              # Icono para "Análisis Trabajo"
            'gender-ambiguous',    # Icono para "Análisis Sexo"
            'map',                 # Icono para "Análisis Ubicación"
            'grid'                 # Icono para "Análisis Categorías"
        ],
        default_index=0,
        orientation='vertical',
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "red", "font-size": "16px"},
            "nav-link": {
                "font-size": "14px", 
                "text-align": "left", 
                "margin": "0px", 
                "--hover-color": "#eee"
            },
            "nav-link-selected": {"background-color": "lightblue"},
        }
    )


# Función para cargar el DataFrame de vencimientos desde un archivo Parquet
def cargar_df():
    try:
        # Leer archivo Parquet
        df = pd.read_parquet('data/credit_card_transactions.parquet')
        
        # Eliminar la columna 'Unnamed: 0' si existe
        if 'Unnamed: 0' in df.columns:
            df = df.drop(columns=['Unnamed: 0'])
        
        return df
    except FileNotFoundError:
        # Mostrar un mensaje de error en Streamlit si el archivo no se encuentra
        st.error("El archivo 'credit_card_transactions.parquet' no se encontró.")
        return None  # Retornar None para indicar que no se pudo cargar el DataFrame

###########################################################################################################


# Mostrar contenido específico según la opción seleccionada
if selected == 'Principal':
    st.title("Proyecto Fintech:")
    st.image('Streamlit/phishing-bancario.jpg')
    
    '''## **Detección de Fraudes con Tarjetas de Créditos:**'''
    
    st.markdown(
        """
    Esta aplicación te permite identificar posibles transacciones fraudulentas en tiempo real mediante un sistema avanzado de detección de fraudes basado en machine learning.

    Con nuestra app, podrás:

    - **Visualizar los datos:** Accede a un conjunto de transacciones, organizadas en tablas fáciles de interpretar, donde podrás explorar los detalles clave de cada operación.
    - **Análisis gráfico:** Descubre patrones y anomalías mediante gráficos interactivos que te mostrarán las tendencias y comportamientos sospechosos en las transacciones.
    - **Predicciones de fraude:** Obtén alertas sobre posibles transacciones fraudulentas basadas en el análisis de datos históricos y comportamientos anómalos.
    
    Esta herramienta está diseñada para ofrecerte una visión clara y detallada de la seguridad en las transacciones financieras, ayudándote a prevenir fraudes.""")


############################################################################################################


elif selected == 'Sistema de Detección de Fraude':
    
    # Título de la aplicación
    st.title("Sistema de Detección de Fraude 🔍")
    
    st.write('\n')
   


########################################################################################################################   
    
elif selected == 'Transacciones':
    # Título de la aplicación
    st.title("Transacciones 📈")
    st.write('\n')
    
    st.subheader('Visualizar el Dataframe:', help=None)
    st.write('El Dataframe posee 13 paginas para visualizar:')
    
    # Cargar el DataFrame
    df = cargar_df()

    # Definir el tamaño de página (cantidad de filas a mostrar)
    page_size = 100000

    # Verificamos de que el DataFrame no esté vacío antes de calcular el número máximo de páginas
    if not df.empty:
        # Calcular el número máximo de páginas
        max_pages = (len(df) // page_size) + 1  
        page_number = st.number_input('Selecciona la página', min_value=1, max_value=max_pages, step=1)

        # Mostrar solo los datos correspondientes a la página seleccionada
        start_idx = (page_number - 1) * page_size
        end_idx = start_idx + page_size
        st.dataframe(df.iloc[start_idx:end_idx])
    else:
        st.write("No hay datos disponibles para mostrar.")

    st.write('---')
    st.markdown('## **Diccionario:**')
    st.markdown(' **Descripción de las columnas del DataFrame:**')
    st.markdown( """     
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
        23. **merch_zipcode:** Código postal del comerciante."""
    )
    st.write('---')
    st.subheader('Podes descargar el Dataframe desde:', help=None)
    st.link_button("Ir a Kaggle", "https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset")
    
#############################################################################################################

elif selected == 'Análisis General':
    
    # Título de la aplicación
    st.title("Análisis General 💰")
    st.write('\n')
    
    df = cargar_df()
    
    filter_frauds = df.query('is_fraud == 1')
    filter_normal = df.query('is_fraud == 0')
    
    st.subheader('Gráficas General:', help=None)
    
    options = st.multiselect(
        "Selecciona Gráfico de Categorías",
        [
            "Porcentaje de fraude", 
            "Histograma", 
            "Violin"
        ]
    )

    # Bucle para mostrar cada gráfico seleccionado
    for option in options:
        if option == "Porcentaje de fraude":
            st.write("Porcentaje de fraude")
            st.image("Streamlit/image/Analisis General/Porcentaje_fraude.png", caption="Porcentaje de fraude")

        elif option == "Histograma":
            st.write("Mostrando gráfico: Histograma")
            st.image("Streamlit/image/Analisis General/Histograma_df.png", caption="Histograma")

        elif option == "Violin":
            st.write("Mostrando gráfico: Violin")
            st.image("Streamlit/image/Analisis General/Violin_plot_df.png", caption="Violin")


    # Mostrar conclusiones una sola vez, fuera del bucle
    st.subheader('**Comentarios:**\n\n')
    st.markdown(
                '- El DataFrame posee un total de __1296675__ registros y __23__ columnas, únicamente posee una sola columna con datos nulos, la columna __merch_zipcode__.\n\n'
                '- Se puede observar que hay columnas que deberían modificarse para mejorar su tratamiento, ``trans_date_trans_time``, ``dob``, ``unix_time`` que corresponden a datos de tiempo, se encuentran en otro formato. Igualmente, merch_zipcode debería ser de tipo int64.\n\n'
                '- Además, se creará una columna __age__ que permita la clasificación de los clientes en función de su edad con el objetivo de observar la distribución de fraudes por edad.\n\n'
                '- La única columna con valores faltantes es __merch_zipcode__, con un total de 195,973 registros ausentes, lo que representa un 0.66% del total de los datos. Dado que este porcentaje es relativamente bajo, es importante evaluar si la ausencia de esta información afecta de manera significativa los registros clasificados como fraudulentos. Un análisis detallado sobre cómo estos valores nulos podrían influir en la detección de fraudes permitirá decidir si es necesario aplicar técnicas de imputación, eliminación de registros, o si su impacto es lo suficientemente marginal como para ser ignorado.')
    
    # Mostrar conclusiones una sola vez, fuera del bucle
    st.subheader('**Conclusión:**\n\n')
    st.markdown('Este análisis revela que:\n\n'
                '- Las transacciones tienen una gran variabilidad en términos de monto.\n\n'
                '- Las ciudades involucradas en las transacciones varían ampliamente en tamaño, pero la mayoría de las transacciones ocurren en ciudades pequeñas.\n\n'
                '- La distribución de los años de nacimiento muestra una concentración de usuarios de entre 40 y 60 años, siendo la mayoría mayores de 48 años.\n\n'
               ' **Observaciones sobre las Variables:**\n\n'

               ' 1. **monto**:\n\n'  
                'La variable **`amt`** presenta una gran dispersión en sus valores, lo que sugiere una amplia variedad en el monto de las transacciones. Sin embargo, también se observan varios **outliers**, lo que podría indicar transacciones con valores extremadamente elevados, o en su defecto, errores de entrada de datos. Estos valores atípicos deben ser revisados con más detalle para determinar si son casos válidos o errores de ingreso.'

                '2. **Población de la Ciudad**:\n\n'  
                'La variable **`city_pop`** muestra un rango extremadamente amplio, con algunos valores que son significativamente grandes. Esto sugiere la posibilidad de **errores de registro** o **registros excepcionales** relacionados con ciertas ubicaciones geográficas. Es recomendable investigar la fuente de estos valores para asegurarse de que la información sea precisa y confiable.'

                '3. **Edad**:\n\n'  
                'A diferencia de las otras variables, la **`dob`** no presenta **outliers**, lo que indica que los datos relacionados con la edad son **relativamente homogéneos** y están dentro del rango esperado. Esto sugiere que no hay errores significativos en la recopilación de datos de edad, y los valores parecen ser consistentes y confiables.')
#########################################################################################################

elif selected == 'Análisis Tiempo':
    # Título de la aplicación
    st.title("Análisis Tiempo  ⏰")    
    st.write('\n')
    
    df = cargar_df()

    # Definir opciones y preseleccionar algunas
    options = st.multiselect(
        "Selecciona Gráfico de Categorías",
        [   "Numero Fraude por Trimestre",
            "Cantidad Operaciones por Dia", 
            "Cantidad Operaciones por Mes", 
            "Cantidad Operaciones por Cuatrimestre"
        ]
    )

    # Bucle para mostrar cada gráfico seleccionado
    for option in options:
        if option == "Numero Fraude por Trimestre":
            st.write("Mostrando gráfico: Numero Fraude por Trimestre")
            st.image("Streamlit/image/Tiempo/tiempo_fraude_por_trimestre.png", caption="Numero Fraude por Trimestre")
        
        if option == "Cantidad Operaciones por Dia":
            st.write("Mostrando gráfico: Cantidad Operaciones por Dia")
            st.image("Streamlit/image/Tiempo/T_operaciones_dia.png", caption="Cantidad Operaciones por Dia")

        elif option == "Cantidad Operaciones por Mes":
            st.write("Mostrando gráfico: Cantidad Operaciones por Mes")
            st.image("Streamlit/image/Tiempo/T_operaciones_mes.png", caption="Cantidad Operaciones por Mes")

        elif option == "Cantidad Operaciones por Cuatrimestre":
            st.write("Mostrando gráfico: Cantidad Operaciones por Cuatrimestre")
            st.image("Streamlit/image/Tiempo/tiempo_fraude_por_trimestre.png", caption="Cantidad Operaciones por Cuatrimestre")
                        
#########################################################################################################

elif selected == 'Análisis Rango Etario':
    
    # Título de la aplicación
    st.title("Análisis Rango Etario")
    # st.image('')
    st.write("\n")
    
    df = cargar_df()
    
    options = st.multiselect(
        "Selecciona Gráfico de Categorías",
        [
            "Total Perdidas por Grupo Etario", 
            "Distribución de Fraude por Género y Grupo Etario (Cat)", 
            "Distribución de Fraude por Género y Estados", 
            "Distribución de Fraude por Género y Grupo Etario", 
            "Tasa Fraude Grupo Etario", 
            "Tasa Fraude Nivel Consumo GE"
        ]
    )

    # Bucle para mostrar cada gráfico seleccionado
    for option in options:
        if option == "Total Perdidas por Grupo Etario":
            st.write("Total Perdidas por Grupo Etario")
            st.image("Streamlit/image/Grupo Etario/ge_cantidad_dinero.png", caption="Total Perdidas por Grupo Etario")

        elif option == "Distribución de Fraude por Género y Grupo Etario (Cat)":
            st.write("Mostrando gráfico: Distribución de Fraude por Género y Grupo Etario (Cat)")
            st.image("Streamlit/image/Grupo Etario/ge_distribucionCategoriasSegunGEET.png", caption="Distribución de Fraude por Género y Grupo Etario (Cat)")

        elif option == "Distribución de Fraude por Género y Estados":
            st.write("Mostrando gráfico: Distribución de Fraude por Género y Estados")
            st.image("Streamlit/image/Grupo Etario/ge_DistribuciongePorEstadosFraude.png", caption="Distribución de Fraude por Género y Estados")

        elif option == "Distribución de Fraude por Género y Grupo Etario":
            st.write("Mostrando gráfico: Distribución de Fraude por Género y Grupo Etario")
            st.image("Streamlit/image/Grupo Etario/ge_DistribucionporGenero.png", caption="Distribución de Fraude por Género y Grupo Etario")

        elif option == "Tasa Fraude Grupo Etario":
            st.write("Mostrando gráfico: Tasa de Fraude por Grupo Etario")
            st.image("Streamlit/image/Grupo Etario/ge_tasa_fraude.png", caption="Tasa de Fraude por Grupo Etario")

        elif option == "Tasa Fraude Nivel Consumo GE":
            st.write("Mostrando gráfico: Tasa de Fraude según Nivel de Consumo GE")
            st.image("Streamlit/image/Grupo Etario/ge_tasaSegunNivelDeConsumo.png", caption="Tasa de Fraude según Nivel de Consumo GE")

    st.subheader('**Conclusión**')
    st.markdown(
                '- Los fraudes tienden a concentrarse en las personas de mediana edad, especialmente en los rangos de **40-55 años** y **25-40 años**. \n\n'
                '- En la mayoría de los rangos etarios, los hombres son ligeramente más propensos a ser víctimas de fraudes, excepto en los grupos de **25-40 años** y **mayores de 70 años**, donde las mujeres superan en número a los hombres.\n\n'
               ' - Las personas **menores de 25 años** son las menos afectadas, lo cual puede estar relacionado con factores como menor actividad financiera o menor exposición a situaciones de riesgo.\n\n'
                '- El análisis sugiere que las estrategias de prevención de fraudes deberían enfocarse en los grupos etarios de **40 a 70 años**, dado que son los más vulnerables.\n\n'
               ' - No necesariamente los comercios con mayor cantidad de transacciones son los más propensos a fraudes, ya que algunos con muchas operaciones tienen un porcentaje bajo de fraude.\n\n'
            '- Los comercios con un alto porcentaje de fraude, aunque no lideran en número total de transacciones, pueden representar un riesgo elevado debido a la mayor proporción de fraudes en comparación con las operaciones legítimas.'
            )
            
#####################################################################################################   
########################################################################################################################   
    
elif selected == 'Análisis Genero':
    
            
    # Título de la aplicación
    st.title("Análisis Sexo ⚧")
    # st.image('')
    st.write('\n') 
    
    df = cargar_df()
    
    st.subheader('Graficas por Estados:', help=None)
    
    # Definir opciones y preseleccionar algunas
    options = st.multiselect(
        "Selecciona Gráfico de Categorías",
        [
            "5 Categorias menos consumida por Genero", 
            "5 Categorias mas consumida por Genero", 
            "Distribución de Fraude por Género", 
            "Distribución de consumo por Género y Categoria"
        ]
    )



    # Bucle para mostrar cada gráfico seleccionado
    for option in options:
        if option == "5 Categorias menos consumida por Genero":
            st.write("Mostrando gráfico: 5 Categorias menos consumida por Genero")
            st.image("Streamlit/image/Genero/G_top5_cat_menos_consumo_porgenero.png", caption="5 Categorias menos consumida por Genero")

        elif option == "5 Categorias mas consumida por Genero":
            st.write("Mostrando gráfico: 5 Categorias mas consumida por Genero")
            st.image("Streamlit/image/Genero/G_5cat_masporgenero.png", caption="5 Categorias mas consumida por Genero")

        elif option == "Distribución de Fraude por Género":
            st.write("Mostrando gráfico: Distribución de Fraude por Género")
            st.image("Streamlit/image/Genero/G_distfraudegenero.png", caption="Distribución de Fraude por Género")

        elif option == "Distribución de consumo por Género y Categoria":
            st.write("Mostrando gráfico: Distribución de consumo por Género y Categoria")
            st.image("Streamlit/image/Genero/G_distribuicion_por_consumo.png", caption="Distribución de consumo por Género y Categoria")


    st.subheader('**Conclusiones:**')
    st.markdown(
                '**Predomina el Fraude Masculino**:\n\n'
                '- En general, el fraude parece ser más común entre los hombres en la mayoría de los estados. Esto se observa claramente en estados como **CA**, **TX**, y **MI**, donde los hombres tienen una mayor participación en las actividades fraudulentas.\n\n'
                
                '**Estados con Mayor Frecuencia de Fraudes**:\n\n'
                '- Los estados con el mayor número de fraudes incluyen **NY**, **TX**, y **PA**. Estos estados también presentan un volumen considerable de fraudes por género, lo que indica que podrían ser focos clave de atención para la prevención de fraudes.\n\n'
                
                '**Diferencia Menor en Alabama**:\n\n'
                '- En **AL**, la diferencia entre fraudes masculinos y femeninos es muy pequeña. Esto sugiere que, en este estado en particular, las estrategias de prevención de fraudes deberían tener en cuenta una distribución más equilibrada entre géneros.\n\n'

                '**Relevancia de las Estrategias de Prevención**:\n\n'
                '- Los estados con más fraudes (como **NY**, **TX**, **PA**) podrían requerir estrategias de prevención de fraudes más rigurosas debido al alto volumen de fraudes en estos lugares.\n\n'
                '- Además, las diferencias de género observadas sugieren que las campañas de prevención de fraudes podrían beneficiarse de una segmentación según el género, especialmente en estados con una gran diferencia entre el número de fraudes masculinos y femeninos.')
    
########################################################################################################################   
    
elif selected == 'Análisis Ubicación':
    
    
    # Título de la aplicación
    st.title("Análisis Ubicación 📍")
    # st.image('')
    st.write('\n')
     
    
    df = cargar_df()
    
    filter_frauds = df.query('is_fraud == 1')
    filter_normal = df.query('is_fraud == 0')
    
    st.subheader('Graficas por Estados:', help=None)

    # Definir opciones y preseleccionar algunas
    options = st.multiselect(
        "Selecciona Gráfico de Categorías",
        [
            "10 Ciudades con mas Fraude", 
            "10 Ciudades con mas Operaciones", 
            "10 Estados con mas Fraude", 
            "10 Estados con mas Operaciones"
        ]
    )

    # Bucle para mostrar cada gráfico seleccionado
    for option in options:
        if option == "10 Ciudades con mas Fraude":
            st.write("Mostrando gráfico: 10 Ciudades con mas Fraude")
            st.image("Streamlit/image/Ubicacion/10_ciudades_mas_fraudes.png", caption="10 Ciudades con mas Fraude")

        elif option == "10 Ciudades con mas Operaciones":
            st.write("Mostrando gráfico: 10 Ciudades con mas Operaciones")
            st.image("Streamlit/image/Ubicacion/10_ciudades_mas_operaciones.png", caption="10 Ciudades con mas Operaciones")

        elif option == "10 Estados con mas Fraude":
            st.write("Mostrando gráfico: 10 Estados con mas Fraude")
            st.image("Streamlit/image/Ubicacion/10_estados_mas_fraudess.png", caption="10 Estados con mas Fraude")

        elif option == "10 Estados con mas Operaciones":
            st.write("Mostrando gráfico: 10 Estados con mas Operaciones")
            st.image("Streamlit/image/Ubicacion/ub_estados_monto_mas_fraude.png", caption="10 Estados con mas Operaciones")

    st.subheader('Conclusion:')
    st.markdown('**Conclusiones**\n\n'
'- **Houston** es el estado con la mayor actividad tanto en operaciones como en fraudes, lo que podría indicar la necesidad de implementar controles más estrictos en las transacciones en esta región.\n\n'
'- Es recomendable realizar un análisis más detallado en **Warren**, **Huntsville**, **Naples**, y **Dallas** para entender mejor los patrones de fraude y posibles áreas de riesgo.\n\n'
'- La diferencia entre los estados con más transacciones y los estados con más fraudes sugiere que el volumen transaccional no siempre correlaciona directamente con el riesgo de fraude. Esto puede ser importante al diseñar estrategias para mitigar fraudes en áreas de alto volumen transaccional.\n\n'
'- Al comparar ambos gráficos, se observa que los estados con mayor número de operaciones no siempre coinciden con los estados con mayor número de fraudes. Sin embargo, estados como **Houston**, **Warren**, y **Huntsville** aparecen en ambos listados, lo que sugiere que estos estados no solo tienen una alta actividad transaccional, sino también un mayor riesgo de fraude.')
    
########################################################################################################################   
    
elif selected == 'Análisis Categorías':
        
    # Título de la aplicación
    st.title("Análisis Categorías 📊")
    # st.image('')
    st.write('\n')
   

    df = cargar_df()
    
    filter_frauds = df.query('is_fraud == 1')
    filter_normal = df.query('is_fraud == 0')
    
    st.subheader('Graficas por Categorias:', help=None)
    
    
    # Definir opciones y preseleccionar algunas
    options = st.multiselect(
        "Selecciona Gráfico de Categorías",
        [
            "10 Categorias con mas Fraude", 
            "10 Categorias con mas Operaciones", 
            "Distribucion Consumo por Genero y Categoria", 
            "Tasa Fraude por Categoria"
        ]
    )

    # Bucle para mostrar cada gráfico seleccionado
    for option in options:
        if option == "10 Categorias con mas Fraude":
            st.write("Mostrando gráfico: 10 Categorias con mas Fraude")
            st.image("Streamlit/image/Categoria/10_categorias_mas_fraude.png", caption="10 Categorias con mas Fraude")

        elif option == "10 Categorias con mas Operaciones":
            st.write("Mostrando gráfico: 10 Categorias con mas Operaciones")
            st.image("Streamlit/image/Categoria/10_categorias_mas_operaciones.png", caption="10 Categorias con mas Operaciones")

        elif option == "Distribucion Consumo por Genero y Categoria":
            st.write("Mostrando gráfico: Distribucion Consumo por Genero y Categoria")
            st.image("Streamlit/image/Categoria/cat_DIstribucionGE.png", caption="Distribucion Consumo por Genero y Categoria")

        elif option == "Tasa Fraude por Categoria":
            st.write("Mostrando gráfico: Tasa Fraude por Categoria")
            st.image("Streamlit/image/Categoria/tasa_categoria.png", caption="Tasa Fraude por Categoria")
    
    st.subheader('**Conclusiones**:')
    st.markdown(
'- Las categorías con mayor número de transacciones, como **Gas_transport**, **Grocery_pos**, y **Home**, son claves en la vida diaria de los usuarios. Sin embargo, la alta incidencia de fraudes en **Grocery_pos** y **Shopping_net** requiere una atención particular.\n\n'
'- Las categorías más frecuentes como **Gas_transport** y **Grocery_pos** reflejan transacciones cotidianas y necesarias, como el transporte y la compra de alimentos. Esto podría indicar que son áreas clave en la vida financiera de los usuarios.\n\n'
'- Las categorías como **Shopping_pos** y **Entertainment** demuestran que también existe una alta actividad en el comercio de bienes de consumo y ocio.\n\n'
'- Las categorías que combinan un alto volumen de transacciones con un número elevado de fraudes, como **Grocery_pos** y **Shopping_net**, deben ser priorizadas para implementar medidas de prevención y control de fraudes.\n\n'
'- La presencia de **Misc_net** y **Shopping_pos** en la lista de fraudes indica que las transacciones en línea, tanto en servicios diversos como en puntos de venta, son particularmente susceptibles a fraudes.\n\n'
'- **Grocery_pos** y **Shopping_net** lideran tanto en términos de volumen de transacciones como en incidencias de fraude. Esto sugiere que las categorías de productos de consumo diario y compras en línea son especialmente vulnerables a fraudes.\n\n'
'- Aunque **Gas_transport** es una categoría con un alto volumen de transacciones, el hecho de que también aparezca en la lista de categorías con fraude podría indicar que, a pesar de su prevalencia, las medidas de seguridad podrían necesitar revisión.\n\n'
'- Las medidas de prevención de fraude podrían beneficiarse de un enfoque en las transacciones en línea, dado que **Shopping_net** y **Misc_net** están entre las categorías más susceptibles a actividades fraudulentas.')
