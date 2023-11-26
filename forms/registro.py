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
    sql = "INSERT INTO alumnos VALUES('{}','{}','{}','{}','{}','{}','{}')".format(nc,n,ap,am,c,g,p)
    cursor.execute(sql)
    con.commit()
    if cursor.rowcount > 0:
        print("Content-type: text/html")
        print("Location: /tutotec/iniciosesion.html")
        print()
        print("<meta http-equiv='refresh' content='0;url=/tutotec/iniciosesion.html' />")
    else:
        print("Content-type: text/html")
        print()
        print("<h1>Registro incorrecto</h1>")
    con.close()
else: 
    print("<h1>Metodo no permitido</h1>")