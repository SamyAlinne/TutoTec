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
    n = datos.getvalue("nombre")
    ap = datos.getvalue("apellido_pa")
    am = datos.getvalue("apellido_ma")
    a = datos.getvalue("academia")
    g = datos.getvalue("grupo")
    p = datos.getvalue("password")
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd')
    cursor = con.cursor()
    sql = "INSERT INTO tutores VALUES('{}','{}','{}','{}','{}','{}',sha1('{}'))".format(c,n,ap,am,a,g,p)
    cursor.execute(sql)
    con.commit()
    con.close()
    print("<h1>Tutor Agregado</h1>")
else: 
    print("<h1>Metodo no permitido</h1>")