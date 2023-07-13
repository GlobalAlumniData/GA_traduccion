from deep_translator import GoogleTranslator
import pandas as pd
from io import BytesIO


def traduccion(x: str) -> str:
    """Traduce textos al inglés"""
    x = GoogleTranslator(source='auto', target='en').translate(x)
    return x


def to_excel(dataframe: pd.DataFrame) -> bytes:
    """Transforma un pandas DataFrame a excel"""
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    # Transformar datos a una hoja de excel
    dataframe.to_excel(writer, index=False, sheet_name='Hoja 1')
    workbook = writer.book
    worksheet = writer.sheets['Hoja 1']

    # Especificar formato
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)

    # Guardar resultados
    writer.close()
    processed_data = output.getvalue()
    return processed_data
