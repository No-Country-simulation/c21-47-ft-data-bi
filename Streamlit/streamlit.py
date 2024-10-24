import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from streamlit_option_menu import option_menu
from datetime import datetime


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
from streamlit_option_menu import option_menu
import streamlit as st

# Configuración del menú principal en la barra lateral
with st.sidebar:
    selected = option_menu(
        menu_title='Menú Principal',
        options=[
            'Principal', 
            'Sistema de Detección de Fraude', 
            'Transacciones', 
            'Análisis Monto', 
            'Análisis Tiempo', 
            'Análisis Edad', 
            'Análisis Trabajo', 
            'Análisis Sexo', 
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
        df = pd.read_parquet('credit_card_transactions.parquet')
        
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
    st.image('phishing-bancario.jpg')
    
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


if selected == 'Sistema de Detección de Fraude':
    
    # Título de la aplicación
    st.title("Sistema de Detección de Fraude 🔍")
    # st.image('')
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

elif selected == 'Análisis Monto':

    # Título de la aplicación
    st.title("Análisis Monto 💰")
    # st.image('')
    st.write('\n')
    # st.subheader('Selecciona una Opción', help=None)

    
#########################################################################################################

elif selected == 'Análisis Tiempo':
    # Título de la aplicación
    st.title("Análisis Tiempo  ⏰")    
    # st.image('')
    st.write('\n')
    # st.subheader('Selecciona una Opcion', help=None)  

                  
#########################################################################################################

elif selected == 'Análisis Edad':
    
    # Título de la aplicación
    st.title("Análisis Edad👶👴")
    # st.image('')
    st.write("\n")
    st.subheader('Selecciona una Opcion')
         
                    
                    
#####################################################################################################   

elif selected == 'Análisis Trabajo':
    
    # Título de la aplicación
    st.title("Análisis Trabajo 💼")
    # st.image('')
    st.write('\n')   
    st.subheader('Selecciona una Opcion', help=None)
    
    
   

    
########################################################################################################################   
    
elif selected == 'Análisis Sexo':
    
            
    # Título de la aplicación
    st.title("Análisis Sexo ⚧")
    # st.image('')
    st.write('\n')
    st.subheader('Selecciona una Opcion', help=None) 
    
    
########################################################################################################################   
    
elif selected == 'Análisis Ubicación':
    
    
    # Título de la aplicación
    st.title("Análisis Ubicación 📍")
    # st.image('')
    st.write('\n')
    st.subheader('Selecciona una Opcion', help=None) 
    
########################################################################################################################   
    
elif selected == 'Análisis Categorías':
        
    # Título de la aplicación
    st.title("Análisis Categorías 📊")
    # st.image('')
    st.write('\n')
    st.subheader('Selecciona una Opcion', help=None) 