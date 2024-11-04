import pandas as pd

# Ruta del archivo de origen
input_file = r'F:\txt\RAW_OGTI.MARCA.TXT'

# Leer el archivo con delimitador "|"
df = pd.read_csv(input_file, delimiter="|", dtype=str, on_bad_lines='skip')

# Eliminar las columnas FECHA_ACT y FECHA_BAJA
df = df.drop(columns=['FECHA_ACT', 'FECHA_ALTA', 'FECHA_BAJA'], errors='ignore')

# Guardar el archivo sin las columnas eliminadas
output_file = r'F:\txt\RAW_OGTI.MARCA_SIN_FECHAS.TXT'
df.to_csv(output_file, sep="|", index=False)

print(f"Archivo guardado sin las columnas FECHA_ACT y FECHA_BAJA en: {output_file}")
