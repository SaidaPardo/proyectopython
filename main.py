import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#inserta datos a la base de datos
def insertar(datos,opcion):
    #conexion a la base de datos
    con_bd = sqlite3.connect('data1.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()

    if opcion == '1':
        #consultas
        cursor_agenda.execute("INSERT INTO usuarios(username, contrasena, correo) VALUES(?, ?, ?)", (datos))
    elif opcion == '2':
        #consultas
        cursor_agenda.execute("INSERT INTO clientes(nombre, apellido, correo, id, direccion) VALUES(?, ?, ?, ?, ?)", (datos))
    elif opcion == '3':
        #consultas
        cursor_agenda.execute("INSERT INTO producto(nombre, descripcion, imagen, precio) VALUES(?, ?, ?, ?)", (datos))
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()


    print("EXITO EN LA OPERACION")


def eliminar(datos,opcion):

    #conexion a la base de datos
    con_bd = sqlite3.connect('data1.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()

    if opcion == '1':
        #consultas
        cursor_agenda.execute("DELETE FROM usuarios WHERE username=?", (datos,))
    elif opcion == '2':
        #consultas
        cursor_agenda.execute("DELETE FROM clientes WHERE id=?", (datos,))
    elif opcion == '3':
        #consultas
        cursor_agenda.execute("DELETE FROM producto WHERE codigo=?", (datos,))
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()
    print("LA ELIMINICACION FUE EXITOSA")

    
def consulta_especifica(datos,opcion):
    #conexion a la base de datos
    con_bd = sqlite3.connect('data1.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()

    if opcion == '1':
        #consultas
        consulta = cursor_agenda.execute("SELECT username,correo FROM usuarios WHERE username=?", (datos,))
    elif opcion == '2':
        #consultas
        consulta = cursor_agenda.execute("SELECT nombre,apellido,correo FROM clientes WHERE id=? ", (datos,))
    elif opcion == '3':
        #consultas
        consulta = cursor_agenda.execute("SELECT nombre,descripcion FROM producto WHERE precio<=?", (datos,))

    #impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()

def consultar_todo():
    #conexion a la base de datos
    con_bd = sqlite3.connect('data1.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas
    consulta = cursor_agenda.execute("SELECT * FROM usuarios")
    #impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()


def actualizar(datos,opcion,actualizacion1,actualizacion2=None):

    #conexion a la base de datos
    con_bd = sqlite3.connect('data1.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()

    if opcion == '1':
        #consultas
        cursor_agenda.execute("UPDATE usuarios SET correo=? WHERE username=?", (actualizacion1,datos,))
    elif opcion == '2':
        #consultas
        cursor_agenda.execute("UPDATE clientes SET correo=?,direccion=? WHERE id=?", (actualizacion1,actualizacion2,datos,))
    elif opcion == '3':
        #consultas
        cursor_agenda.execute("UPDATE producto SET descripcion=?,precio=? WHERE codigo=?", (actualizacion1,actualizacion2,datos,))
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()
    print("LA ACTUALIZACION FUE EXITOSA")




def registrarUsuarios():
    usuarios=()
    username=input("Digite nombre usuario >> ")
    contrasena=input("Digite password >> ")
    correo=input("Digite correo >> ")
    usuarios=(username,contrasena,correo)
    return usuarios

def registrarClientes():
    clientes=()
    nombre=input("Digite nombre del cliente").upper()
    apellido=input("Digite apellido del cliente").upper()
    correo=input("Digite correo electronico")
    identificador=int(input("Digite su numero de identificacion"))
    direccion=input("Digite la direccion").upper()
    clientes=(nombre,apellido,correo,identificador,direccion)
    return clientes

def registrarProducto():
    producto=()
    nombre=input("Digite nombre del producto").upper()
    descripcion=input("Ingrese la descripcion/precio del producto").upper()
    imagen=input("Digite ruta de la imagen")
    precio=float(input("Digite el precio del producto"))
    producto=(nombre,descripcion,imagen,precio)
    return producto

def insercion_datos():
    opcion=0
    while opcion!='4':
        print("1 Crear usuario nuevo")
        print("2 Crear cliente nuevo")
        print("3 Crear un nuevo producto")
        print("4 Regresar menu principal")
        opcion=input()
        if opcion=="1":
            usuarios = registrarUsuarios()
            insertar(usuarios,opcion)
        elif opcion =="2":
            clientes = registrarClientes()
            insertar(clientes,opcion)
        elif opcion == "3":
            producto = registrarProducto()
            insertar(producto,opcion)

def consultar_datos():
    opcion=0
    while opcion!='4':
        print("1 Consultar usuario registrado")
        print("2 Consultar clientes registrados")
        print("3 Consultar producto por precios")
        print("4 Regresar menu principal")
        opcion=input()
        if opcion == "1":
            username=input("Digite el username a buscar")
            consulta_especifica(username,'1')
        elif opcion == "2":
            username=input("Digite la cedula del cliente a buscar")
            consulta_especifica(username,'2')
        elif opcion == '3':
            precio=input("Digite su presupuesto")
            consulta_especifica(precio,'3')
            
def enviar_correo():
    #conexion a la base de datos
    con_bd = sqlite3.connect('data1.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas
    consulta = cursor_agenda.execute("SELECT correo FROM clientes WHERE ciudad=?", ('Armenia',))
    #impresion de todos los campos
    listaCorreos=[]
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
            listaCorreos.append(campo)
    print(listaCorreos)
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()
    return listaCorreos
    
    
"""def clientes_correo(listaCorreos):
    for i in range (len(listaCorreos)):
        #credenciales
        proveedor_correo = 'smtp.gmail.com: 587'
        remitente = 'saidapardo79@gmail.com'
        password = '89002997'
        #conexion a servidor
        servidor = smtplib.SMTP(proveedor_correo)
        servidor.starttls()
        servidor.ehlo()
        #autenticacion
        servidor.login(remitente, password)
        #mensaje 
        mensaje = "Dios te Ama y Bendice tu Hogar"
        msg = MIMEMultipart()
        msg.attach(MIMEText(mensaje, 'html'))
        msg['From'] = remitente
        msg['To'] = listaCorreos[i]
        msg['Subject'] = 'Prueba'
        servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
"""

def clientes_correo(listaCorreos):
    
    #credenciales
    proveedor_correo = 'smtp.gmail.com: 587'
    remitente = 'saidapardo79@gmail.com'
    password = '89002997'
    #conexion a servidor
    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()
    #autenticacion
    servidor.login(remitente, password)
    #mensaje 
    mensaje = "Dios te Ama y Bendice tu Hogar"
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'html'))
    msg['From'] = remitente
    msg['To'] = ", ".join(listaCorreos)
    msg['Subject'] = 'Prueba'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())



        
def eliminar_datos():
        opcion=0
        while opcion!='4':
            print("1 Eliminar usuario registrado")
            print("2 Eliminar clientes registrados")
            print("3 Eliminar producto por precios")
            print("4 Regresar menu principal")
            opcion=input()
            if opcion == "1":
                username=input("Digite el username a eliminar")
                eliminar(username,opcion)
            elif opcion == "2":
                identificador=input("Digite la cedula del cliente a eliminar")
                eliminar(identificador,opcion)
            elif opcion == '3':
                codigo=input("Digite el codigo del producto a eliminar")
                eliminar(codigo,opcion)

def actualizar_datos():
    opcion=0
    while opcion!='4':
        print("1 Actualizar usuario registrado")
        print("2 Actualizar clientes registrados")
        print("3 Actualizar producto por precios")
        print("4 Regresar menu principal")
        opcion=input()
        if opcion == "1":
            username=input("Digite el username a Actualizar")
            correo=input("Digite nuevo correo")
            actualizar(username,opcion,correo)
        elif opcion == "2":
            identificador=input("Digite la cedula del cliente a Actualizar")
            correo=input("Digite nuevo correo")
            direccion=input("Diite nueva dierccion")
            actualizar(identificador,opcion,correo,direccion)
        elif opcion == '3':
            codigo=input("Digite el codigo del producto a Actualizar")
            descripcion=input("Digite nueva descripción")
            precio=float(input("Digite nuevo precio"))
            actualizar(codigo,opcion,descripcion,precio)


def menu_principal():
    continuar="si"
    while continuar=="si":
        enviar_correo()
        print("Digite una opcion")
        print("1 Insertar datos")
        print("2 Consultar datos")
        print("3 Eliminar datos")
        print("4 Actualizar datos")
        
        opcion=input()
        if opcion == '1':
            insercion_datos()
        elif opcion == '2':
            consultar_datos()
        elif opcion == '3':
            eliminar_datos()
        elif opcion == '4':
            actualizar_datos()
        continuar=input("si/no  mostrar menu").lower()

#menu_principal()

listaCorreos1=enviar_correo()
clientes_correo(listaCorreos1)

menu_principal()
