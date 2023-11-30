#!C:/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print("Content-type: text/html")
print()
print("<h1>Consulta Usuarios: Tutores</h1>")
print("<hr>")

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd')
cursor = con.cursor()
sql = "SELECT * FROM tutores"
cursor.execute(sql)
for (correo, nombre, apellido_pa, apellido_ma, academia, grupo, password) in cursor:
    print("{},{},{},{},{},{},{}".format(correo, nombre, apellido_pa, apellido_ma, academia, grupo, password))
    print("<hr>")