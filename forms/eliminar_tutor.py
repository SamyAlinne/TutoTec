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
    c = datos.getvalue("correo")
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd')
    cursor = con.cursor()
    sql = f"DELETE from tutores WHERE correo='{c}'"
    cursor.execute(sql)
    con.commit()
    con.close()
    print("<h1>Tutor Eliminado</h1>")
else: 
    print("<h1>Metodo no permitido</h1>")