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

def load_rut_column():
    # Cargar solo la columna RUT
    rut_column = pd.read_excel('PUB_EMPRESAS_DATA_1.xlsx', usecols=['RUT'])
    return rut_column

def find_row_by_rut(rut_column, target_rut):
    # Iterar sobre las filas y encontrar la coincidencia
    for index, row in rut_column.iterrows():
        if row['RUT'] == target_rut:
            return index

def load_data(row_index):
    # Cargar solo la fila que coincide con el índice
    df = pd.read_excel('PUB_EMPRESAS_DATA_1.xlsx', skiprows=row_index, nrows=1)
    return df

data_load_state = st.text('Cargando data...')
rut_column = load_rut_column()
data_load_state.text('Cargando columna RUT... Hecho!')

# Buscar el RUT deseado
target_rut = st.text_input("Ingrese el RUT que desea buscar:")

if st.button("Buscar"):
    # Buscar el índice de la fila que coincide con el RUT
    row_index = find_row_by_rut(rut_column, target_rut)
    if row_index is not None:
        data_load_state.text('Cargando fila... Hecho!')
        # Cargar y mostrar la fila completa
        df = load_data(row_index)
        st.subheader('Fila encontrada:')
        st.write(df)
    else:
        st.write("RUT no encontrado.")