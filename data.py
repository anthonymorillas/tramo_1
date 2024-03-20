# import streamlit as st
# import pandas as pd

# # @st.cache_data
# def load_data():
#     # Cargar datos y especificar tipo de datos para la columna problemática
#     df = pd.read_excel('PUB_EMPRESAS_DATA_1.xlsx', nrows=60000, dtype={'column_name': str})
#     return df

# data_load_state = st.text('Cargando data...')
# df = load_data()
# data_load_state.text('Cargando data... Hecho!')

# st.subheader('Raw data')
# st.write(df)


import streamlit as st
import pandas as pd

# Función para cargar los datos desde el archivo Excel
def load_data():
    df = pd.read_excel('PUB_EMPRESAS_DATA_1.xlsx', dtype={'column_name': str}) #nrows=60000
    return df

# Cargar los datos
data_load_state = st.text('Cargando data...')
df = load_data()
data_load_state.text('Cargando data... Hecho!')

# Agregar un buscador
search_query = st.text_input("Buscar por RUT", "")
if search_query:
    # Filtrar el DataFrame según el texto ingresado por el usuario en la columna RUT
    filtered_df = df[df['RUT'].str.contains(search_query, case=False)]
    # Mostrar solo la primera fila que coincide con la búsqueda
    if not filtered_df.empty:
        st.subheader('Resultado de la búsqueda')
        st.write(filtered_df.iloc[0])
    else:
        st.write("No se encontraron resultados")