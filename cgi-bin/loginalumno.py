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
    c = datos.getvalue("emailAlumno")
    p = datos.getvalue("passwordAlumno")

    try:
        con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd')
        cursor = con.cursor()
        sql = "SELECT * FROM alumnos WHERE no_control='{}' AND password='{}'".format(c, p)
        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            print("<meta http-equiv='refresh' content='0;url=/tutotec/indexalumno.html' />")
            print()  # Imprimir una línea en blanco para finalizar las cabeceras
            print("<script>alert('Inicio de sesión correcto. Redirigiendo...');</script>")
        else:
            print("<script>alert('Inicio de sesión incorrecto. Vuelva a intentarlo');</script>")
            print("<meta http-equiv='refresh' content='0;url=/tutotec/iniciosesion.html' />")

        con.commit()
        con.close()

    except mysql.connector.Error as err:
        print("Error:", err)

else:
    print("<h4>Método no permitido</h4>")




