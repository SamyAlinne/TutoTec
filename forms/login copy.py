# get firestore data
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("/usr/firestore/database.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
    
metodo = os.environ["REQUEST_METHOD"]

if metodo == "POST":
    datos = cgi.FieldStorage()
    nc = datos.getvalue("no_control")
    p = datos.getvalue("password")

    print("No. Control:", nc)
    print("Contraseña:", p)

    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tutotecbd')
    cursor = con.cursor()
    sql = "SELECT * FROM alumnos WHERE no_control='{}' AND password='{}'".format(nc,p)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        print("Content-type: text/html")
        print("Location: /tutotec/index.html")
        print()
        print("<meta http-equiv='refresh' content='0;url=/tutotec/index.html' />")
    else:
        print("Content-type: text/html")
        print()
        print("<h1>Inicio de sesión incorrecto</h1>")
    con.commit()
    con.close()
else:
    print("Content-type: text/html")
    print()
    print("<h1>Metodo no permitido</h1>")