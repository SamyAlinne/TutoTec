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
    c = datos.getvalue("emailTutor")
    n = datos.getvalue("txtNombreTutor")
    ap = datos.getvalue("txtAPatTutor")
    am = datos.getvalue("txtAMatTutor")
    a = datos.getvalue("txtAcademia")
    g = datos.getvalue("txtGrupoTutor")
    p = datos.getvalue("passTutor")

    if c is None or not c.strip():  # Verificar si c es None o una cadena vacía
        print("<script>alert('Correo no proporcionado. Complete el campo.');</script>")
    elif not "@" in c:
        print("<script>alert('Correo inválido. Intente nuevamente.');</script>")
    else:

        try:
            con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd', charset='utf8')
            cursor = con.cursor()

            # Ejemplo de consulta parametrizada para evitar inyección SQL
            sql = "INSERT INTO tutores VALUES(%s, %s, %s, %s, %s, %s, %s)"
            values = (c, n, ap, am, a, g, p)
            cursor.execute(sql, values)

            con.commit()
            con.close()

            print("<meta http-equiv='refresh' content='1;url=/tutotec/iniciosesion.html' />")
            print("<script>alert('Tutor agregado correctamente');</script>")

        except mysql.connector.Error as err:
            print("<script>alert('Hubo un error al agregar el tutor. Intente nuevamente.');</script>")
            print("<meta http-equiv='refresh' content='1;url=/tutotec/registro_tutor.html' />")
            # Para depuración, puedes imprimir el error
            print("Error:", err)

else:
    print("<script>alert('Método no permitido');</script>")


    