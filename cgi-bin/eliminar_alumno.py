#!C:/Python311/python.exe
import mysql.connector
import os
import cgi

print("Content-type: text/html")
print()

# Obtener el método de solicitud (GET, POST, etc.)
metodo = os.environ["REQUEST_METHOD"]

# Verificar si la solicitud es GET
if metodo == "GET":
    parametros = cgi.FieldStorage()
    nc = parametros.getvalue("no_control")  # Obtener el número de control del parámetro GET

    if nc:
        try:
            # Establecer la conexión a la base de datos MySQL
            con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd', charset='utf8')
            cursor = con.cursor()

            # Consulta SQL para eliminar el registro del alumno con el número de control especificado
            sql = "DELETE FROM alumnos WHERE no_control = %s"
            cursor.execute(sql, (nc,))  # Ejecutar la consulta SQL con el número de control
            con.commit()  # Confirmar los cambios en la base de datos
            con.close()  # Cerrar la conexión

            print("<h1>Alumno Eliminado</h1>")  # Imprimir mensaje de éxito
        except mysql.connector.Error as err:
            print(f"<h1>Error al eliminar alumno: {err}</h1>")  # Imprimir mensaje de error en caso de falla
    else:
        print("<h1>Parámetro 'no_control' no proporcionado</h1>")  # Manejar el caso de falta de parámetro
else:
    print("<h1>Método no permitido</h1>")  # Manejar otros métodos que no sean GET
