import openpyxl
import numpy as np

import streamlit as st
from funciones import *

# Header y descripción
with st.container():
    st.title('Traducción de textos')
    st.markdown('App para traducir testimonios al inglés de forma automática')

# Componente para subir archivo
archivo = st.file_uploader('Proporciona el archivo a leer:')

# Comprobar si se ha subido un archivo
if archivo is not None:
    workbook = openpyxl.load_workbook(archivo)
    hojas = workbook.sheetnames
    hoja = st.selectbox(
        'Elige hoja del excel',
        ['<Selecciona una opción>'] + hojas
    )

    # Enseñar datos para la hoja seleccionada
    if hoja != '<Selecciona una opción>':
        datos = pd.read_excel(archivo, sheet_name=hoja)

        # Muestra los datos
        st.write('Cinco primeras observaciones de los datos:')
        st.write(datos.head())
        columnas = st.multiselect(
            '¿Qué columna(s) quieres traducir?',
            datos.columns
        )
        st.write('')
        _, col2, _ = st.columns(3)
        with col2:
            # Botón para empezar traducción
            traducir = st.button('Traducir testimonios')

            if traducir:
                with st.spinner('Traduciendo...'):
                    datos.loc[:, columnas] = datos.loc[:, columnas].applymap(
                        traduccion,
                        na_action='ignore'
                    )

        if traducir:
            # Enseñar resultados
            st.write(datos.head())

            _, col2, _ = st.columns(3)
            with col2:
                # Permitir descarga de datos
                datos_xlsx = to_excel(datos)
                st.download_button(
                    label='📥 Descargar datos',
                    data=datos_xlsx,
                    file_name='traduccion.xlsx'
                )
