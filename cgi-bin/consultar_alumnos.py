#!C:/Python311/python.exe
import mysql.connector
import json

# Establecer la conexión a la base de datos
con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd', charset='utf8')
cursor = con.cursor()

# Realizar la consulta
sql = "SELECT * FROM alumnos"
cursor.execute(sql)

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Convertir los resultados a formato JSON para enviarlos a la página HTML
resultados_json = json.dumps(resultados)
print("Content-type: application/json")
print()
print(resultados_json)

