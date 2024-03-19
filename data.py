import streamlit as st
import pandas as pd

# @st.cache_data
def load_data():
    # Cargar datos y especificar tipo de datos para la columna problemática
    df = pd.read_excel('PUB_EMPRESAS_DATA_1.xlsx', dtype={'column_name': str}) #nrows=1000
    return df

data_load_state = st.text('Cargando data...')
df = load_data()
data_load_state.text('Cargando data... Hecho!')

st.subheader('Raw data')
st.write(df)