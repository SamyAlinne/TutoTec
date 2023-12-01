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
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd')
    cursor = con.cursor()
    sql = f"DELETE from alumnos WHERE no_control='{nc}'"
    cursor.execute(sql)
    con.commit()
    con.close()
    print("<meta http-equiv='refresh' content='0;url=/tutotec/indextutor.html' />")
    print("<script>alert('Alumno eliminado correctamente');</script>")
else: 
    print("<h1>Metodo no permitido</h1>")