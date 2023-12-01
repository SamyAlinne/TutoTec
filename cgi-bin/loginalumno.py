#!C:/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
from urllib.parse import urlencode
cgitb.enable()
print("Content-type: text/html")
print()

metodo = os.environ["REQUEST_METHOD"]

if metodo == "POST":
    datos = cgi.FieldStorage()
    c = datos.getvalue("emailAlumno")
    p = datos.getvalue("passwordAlumno")

    try:
        con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd', charset='utf8')
        cursor = con.cursor()
        sql = "SELECT * FROM alumnos WHERE no_control='{}' AND password='{}'".format(c, p)
        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            no_control = result [0]
            nombre = result[1]  
            apellido_paterno = result[2] 
            apellido_materno = result[3] 

             # Codificar los valores con urlencode para manejar caracteres especiales
            nombre_encoded = urlencode({'nombre': nombre})
            apellido_paterno_encoded = urlencode({'apaterno': apellido_paterno})
            apellido_materno_encoded = urlencode({'amaterno': apellido_materno})

            print("<meta http-equiv='refresh' content='0;url=/tutotec/indexalumno.html?{}&{}&{}&{}' />".format(no_control, nombre_encoded, apellido_paterno_encoded, apellido_materno_encoded))
            
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




