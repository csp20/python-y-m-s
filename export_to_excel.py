import pandas as pd
import sqlite3

# Conexión a la base de datos SQLite (cambia esto según tu base de datos)
conn = sqlite3.connect('tu_base_de_datos.db')

# Consulta SQL para obtener los datos de la tabla
query = "SELECT * FROM juegos_anita"

# Leer los datos en un DataFrame de pandas
df = pd.read_sql_query(query, conn)

# Volcar los datos a un archivo Excel
df.to_excel('juegos_anita.xlsx', index=False)

# Cerrar la conexión a la base de datos
conn.close()
