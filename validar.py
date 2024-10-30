import pandas as pd

# Cargar los archivos de Excel y forzar 'COD' como texto
req_df = pd.read_excel("REQ.xlsx", sheet_name=0, dtype=str)
medicamentos_df = pd.read_excel("MEDICAMENTOS.xlsx", sheet_name=0, dtype=str)

# Eliminar valores nulos en la columna 'COD' y convertir a enteros
req_codes = set(req_df['COD'].dropna().astype(int))
medicamentos_codes = set(medicamentos_df['COD'].dropna().astype(int))

# Encontrar los códigos que están en REQ pero no en MEDICAMENTOS, y viceversa
only_in_req = list(req_codes - medicamentos_codes)
only_in_medicamentos = list(medicamentos_codes - req_codes)

# Asegurar que ambas listas tengan la misma longitud rellenando con None
max_length = max(len(only_in_req), len(only_in_medicamentos))
only_in_req.extend([None] * (max_length - len(only_in_req)))
only_in_medicamentos.extend([None] * (max_length - len(only_in_medicamentos)))

# Crear un DataFrame para guardar el resultado
result_df = pd.DataFrame({
    "Only_in_REQ": only_in_req,
    "Only_in_MEDICAMENTOS": only_in_medicamentos
})

# Guardar el resultado en un archivo CSV
result_df.to_csv("codigos_diferentes.csv", index=False)

print("El archivo 'codigos_diferentes.csv' se ha creado con los códigos faltantes en cada archivo.")
