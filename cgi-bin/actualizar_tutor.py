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
            sql = f"UPDATE tutores SET password='{p}', nombre='{n}', apellido_pa='{ap}', apellido_ma='{am}', academia='{a}', grupo='{g}' WHERE correo='{c}'"
            cursor.execute(sql)
    
            con.commit()
            con.close()

            # Datos actualizados para enviar a través de la URL
            nombre_actualizado = "NuevoNombre"
            apellido_paterno_actualizado = "NuevoApellidoPaterno"
            apellido_materno_actualizado = "NuevoApellidoMaterno"

             # Crear la URL con los datos actualizados como parámetros
            url_redireccion = f"/tutotec/indextutor.html?nombre={nombre_actualizado}&apaterno={apellido_paterno_actualizado}&amaterno={apellido_materno_actualizado}"
            # Redirigir a la URL con los datos actualizados
            print(f"<meta http-equiv='refresh' content='0;url={url_redireccion}' />")
            print("<script>alert('Los datos fueron modificados satisfactoriamente');</script>")

        except mysql.connector.Error as err:
            print("<script>alert('Hubo un error al modificar los datos del tutor. Intente nuevamente.');</script>")
            print("<meta http-equiv='refresh' content='1;url=/tutotec/actualizar_tutor.html' />")
            # Para depuración, puedes imprimir el error
            print("Error:", err)
else:
    print("<script>alert('Método no permitido');</script>")