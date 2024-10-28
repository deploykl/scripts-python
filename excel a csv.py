import pandas as pd

# Ruta del archivo Excel
ruta_excel = r'D:\PROGRAMACION\scripts-python\data-final.xlsx'

# Cargar el archivo Excel
df = pd.read_excel(ruta_excel)

# Exportar el DataFrame a CSV delimitado por ';'
ruta_csv = r'D:\PROGRAMACION\scripts-python\data-final.csv'
df.to_csv(ruta_csv, sep=';', index=False)

print("Conversión completada. El archivo CSV se ha guardado en:", ruta_csv)
