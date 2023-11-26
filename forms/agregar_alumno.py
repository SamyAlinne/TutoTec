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
    nc = datos.getvalue("no_control")
    n = datos.getvalue("nombre")
    ap = datos.getvalue("apellido_pa")
    am = datos.getvalue("apellido_ma")
    c = datos.getvalue("carrera")
    g = datos.getvalue("grupo")
    p = datos.getvalue("password")
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd')
    cursor = con.cursor()
    sql = "INSERT INTO alumnos VALUES('{}','{}','{}','{}','{}','{}',sha1('{}'))".format(nc,n,ap,am,c,g,p)
    cursor.execute(sql)
    con.commit()
    con.close()
    print("<h1>Alumno Agregado</h1>")
else: 
    print("<h1>Metodo no permitido</h1>")