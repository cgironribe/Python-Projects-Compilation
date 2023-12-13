#PROGRAM DEVELOPED IN SPANISH - WILL CONTAIN SPANISH VARIABLES AND CODE GUIDANCE
#El programa le pide al usuario que introduzca una palabra y basandose en una lista que puedes modificar, comprueba qué palabras riman con su input.


"""import sqlite3

# Conectarse a la base de datos o crearla si no existe
conn = sqlite3.connect('palabras.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla para almacenar las palabras
cursor.execute('''
    CREATE TABLE IF NOT EXISTS palabras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        palabra TEXT UNIQUE
    )
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()"""

import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('palabras.db')
cursor = conn.cursor()

# Leer el archivo de palabras y almacenarlas en la base de datos
with open('/Users/carla/Downloads/palabras_esp_rae.txt', encoding='utf-8') as archivo:
    for linea in archivo:
        palabra = linea.strip()  # Eliminar espacios en blanco y saltos de línea
        cursor.execute('INSERT OR IGNORE INTO palabras (palabra) VALUES (?)', (palabra,))

# Guardar los cambios
conn.commit()

# Conectarse a la base de datos
conn = sqlite3.connect('palabras.db')
cursor = conn.cursor()

# Ejecutar una consulta SQL para obtener todas las palabras
cursor.execute('SELECT palabra FROM palabras')
palabras = [fila[0] for fila in cursor.fetchall()]

# Obtener entrada del usuario
entrada_usuario = input("Ingrese una palabra o parte de una palabra: ")

# Obtener las últimas dos letras de la entrada del usuario
ultimas_tres_letras = entrada_usuario[-3:]

# Crear una lista para almacenar las palabras que coinciden
resultados = []

# Buscar palabras que terminen con las mismas dos letras que la entrada del usuario
for palabra in palabras:
    if palabra.endswith(ultimas_tres_letras):
        resultados.append(palabra)


# Imprimir las palabras que coinciden
if resultados:
    print(f"Palabras que riman con {entrada_usuario}:")
    for palabra in resultados:
        print(f"-{palabra}")
else:
    print("No se encontraron palabras que coincidan.")

# Cerrar la conexión
conn.close()
