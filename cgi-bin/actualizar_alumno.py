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
    elif "@" not in co:
        print("<script>alert('Correo inválido. Intente nuevamente.');</script>")
    else:
        try:
            con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd', charset='utf8')
            cursor = con.cursor()

            sql = f"UPDATE alumnos SET password='{p}', nombre='{n}', apellido_pa='{ap}', apellido_ma='{am}', carrera='{c}', grupo='{g}', correo='{co}' WHERE no_control='{nc}'"
            cursor.execute(sql)

            con.commit()
            con.close()
            
            # Datos actualizados para enviar a través de la URL
            nombre_actualizado = "NuevoNombre"
            apellido_paterno_actualizado = "NuevoApellidoPaterno"
            apellido_materno_actualizado = "NuevoApellidoMaterno"

             # Crear la URL con los datos actualizados como parámetros
            url_redireccion = f"/tutotec/indexalumno.html?nombre={nombre_actualizado}&apaterno={apellido_paterno_actualizado}&amaterno={apellido_materno_actualizado}"
            # Redirigir a la URL con los datos actualizados
            print(f"<meta http-equiv='refresh' content='0;url={url_redireccion}' />")
            print("<script>alert('Los datos fueron modificados satisfactoriamente');</script>")

           

        except mysql.connector.Error as err:
            print("<script>alert('Hubo un error al modificar los datos del alumno. Intente nuevamente.');</script>")
            print("<meta http-equiv='refresh' content='1;url=/tutotec/actualizar_alumno.html' />")
            # Para depuración, puedes imprimir el error
            print("Error:", err)

else:
    print("<h1>Método no permitido</h1>")
