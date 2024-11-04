import os
import pandas as pd

# Ruta a la carpeta donde están los archivos Excel
carpeta_excel = "D:\\PROGRAMACION\\QUIMICOSFARMACEUTICOS"

# Lista para almacenar los DataFrames de cada archivo
listado_dfs = []

# Selección de columnas deseadas
columnas_deseadas = ['codigo_eje', 'nombre_eje', 'coddisa', 'nomdisa', 'codred', 'red', 'codmef',
                     'uemef', 'codigo_pre', 'establec', 'tipo', 'CATEGORIA', 'est_act', 'ue', 'quintil',
                     'vraem', 'europ', 'indig', 'codigo_med', 'nombre_med', 'formaf', 'tipomed', 'subtipo',
                     'Nomsubtipo', 'petitorio', 'estrategic', 'tipsum', 'oct23tot', 'nov23tot', 'dic23tot',
                     'ene24tot', 'feb24tot', 'mar24tot', 'abr24tot', 'may24tot', 'jun24tot', 'jul24tot',
                     'ago24tot', 'set24tot', 'precio', 'ingre', 'reingre', 'distri',
                     'fecha_venc', 'mesano', 'stk_sismed', 'stk_dona', 'con_sismed', 'con_dona', 'stock_tot',
                     'cons_tot', 'cpa', 'disp', 'indicador', 'stk_almstk', 'stk_almdon']

# Contador de archivos leídos
contador_archivos = 0

# Recorrer todos los archivos en la carpeta
for archivo in os.listdir(carpeta_excel):
    if archivo.endswith('.xlsx'):
        ruta_archivo = os.path.join(carpeta_excel, archivo)
        
        # Leer la segunda hoja del archivo Excel (índice 1)
        df = pd.read_excel(ruta_archivo, sheet_name=1, skiprows=3)
        
        # Verificar que las columnas se han leído correctamente
        print(f"Nombres de las columnas en {archivo}:", df.columns)

        # Seleccionar las columnas deseadas
        df = df[columnas_deseadas]

        # Agregar el DataFrame a la lista
        listado_dfs.append(df)
        
        # Incrementar el contador de archivos
        contador_archivos += 1

# Concatenar todos los DataFrames en uno solo
df_total = pd.concat(listado_dfs, ignore_index=True)

# Exportar a CSV con ';' como delimitador
df_total.to_csv('data_uni.csv', index=False, sep=';')

# Mostrar la cantidad de archivos procesados
print(f"Archivo CSV exportado correctamente. Se procesaron {contador_archivos} archivos Excel.")
