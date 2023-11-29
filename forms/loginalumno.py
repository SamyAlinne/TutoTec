#!/usr/bin/env python3
import cgi
import cgitb
import firebase_admin
from firebase_admin import credentials, auth

cgitb.enable()
print("Content-type: text/html")
print()

cred = credentials.Certificate("assets/bd/google-services.json")
firebase_admin.initialize_app(cred)

metodo = os.environ["REQUEST_METHOD"]

if metodo == "POST":
    datos = cgi.FieldStorage()
    c = datos.getvalue("emailAlumno")
    p = datos.getvalue("passwordAlumno")

    try:
        user = auth.get_user_by_email(c)
        if auth.verify_password(p, user.password_hash):
            print("Content-type: text/html")
            print("Location: /tutotec/index.html")
            print()
            print("<meta http-equiv='refresh' content='0;url=/tutotec/index.html' />")
        else:
            print("Content-type: text/html")
            print()
            print("<h1>Inicio de sesión incorrecto</h1>")
    except auth.UserNotFoundError:
        print("Content-type: text/html")
        print()
        print("<h1>Usuario no encontrado</h1>")
    except auth.InvalidPasswordError:
        print("Content-type: text/html")
        print()
        print("<h1>Contraseña incorrecta</h1>")
else:
    print("Content-type: text/html")
    print()
    print("<h1>Método no permitido</h1>")
