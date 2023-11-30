#!C:/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print("Content-type: text/html")
print()

metodo = os.environ["REQUEST_METHOD"]


if metodo == "POST":
    datos = cgi.FieldStorage()
    nc = datos.getvalue("txtNoControl")
    n = datos.getvalue("txtNombreAlumno")
    ap = datos.getvalue("txtAPatAlumno")
    am = datos.getvalue("txtAMatAlumno")
    c = datos.getvalue("txtCarrera")
    g = datos.getvalue("txtGrupoAlumno")
    co = datos.getvalue("emailAlumno")
    p = datos.getvalue("passAlumno")

    if co is None or not co.strip():  # Verificar si co es None o una cadena vacía
        print("<script>alert('Correo no proporcionado. Complete el campo.');</script>")
    elif not "@" in co:
        print("<script>alert('Correo inválido. Intente nuevamente.');</script>")
    else:

        try:
            con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd')
            cursor = con.cursor()

            # Ejemplo de consulta parametrizada para evitar inyección SQL
            sql = "INSERT INTO alumnos VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (nc, n, ap, am, c, g, co, p)
            cursor.execute(sql, values)

            con.commit()
            con.close()

            print("<meta http-equiv='refresh' content='1;url=/tutotec/iniciosesion.html' />")
            print("<script>alert('Alumno agregado correctamente');</script>")

        except mysql.connector.Error as err:
            print("<script>alert('Hubo un error al agregar el alumno. Intente nuevamente.');</script>")
            print("<meta http-equiv='refresh' content='1;url=/tutotec/registro_alumno.html' />")
            # Para depuración, puedes imprimir el error
            print("Error:", err)

else:
    print("<script>alert('Método no permitido');</script>")
