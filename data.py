# import streamlit as st
# import pandas as pd

# # @st.cache_data
# def load_data():
#     # Cargar datos y especificar tipo de datos para la columna problemática
#     chunk_size = 1000
#     chunks = pd.read_csv('PUB_EMPRESAS_DATA_1.csv', chunksize=chunk_size, encoding='latin1', dtype={'column_name': str}) #nrows=100000
#     df = pd.concat(chunks)
#     df['column_name'] = df['column_name'].astype(str)
#     return df

# data_load_state = st.text('Cargando data...')
# df = load_data()
# data_load_state.text('Cargando data... Hecho!')

# st.subheader('Raw data')
# st.write(df)


import streamlit as st
import pandas as pd

# @st.cache_data
def load_data():
    # Cargar datos y especificar tipo de datos para la columna problemática
    # Cambia 'PUB_EMPRESAS_DATA_1.xlsx' por el nombre de tu archivo Excel
    chunk_size = 40000
    df = pd.read_excel('PUB_EMPRESAS_DATA_1.xlsx', dtype={'column_name': str}) #nrows=100000
    
    # Dividir el DataFrame en chunks de tamaño chunk_size
    chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]
    
    return chunks

data_load_state = st.text('Cargando data...')
chunks = load_data()
data_load_state.text('Cargando data... Hecho!')

st.subheader('Raw data')
# Mostrar todos los chunks
for i, chunk in enumerate(chunks):
    st.subheader(f'Chunk {i+1}')
    st.write(chunk)