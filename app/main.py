import qr_generador as generador
import qr_lector as lector
import database as db

print("""
----------------------------------------------------------
Sistema de Tarjetas QR
----------------------------------------------------------
Menú

* Insertar Usuarios: 1
* Monitor QR (Solo monitor): 2
* Proyecto COMPLETO: 3
""")
usuario= int(input("Elección: "))

if usuario==1:
    nombre= str(input("Ingresa el nombre del usuario: "))
    cargo= str(input("Ingrese el cargo (Estudiante, Profesor, Inspector)"))
    foto= str(input("Ingresa la direccion de la foto (usuario/usuario.jpeg):"))
    #nombre= "Zharick Nikol Conde Chango"
    conn= db.Conexion()
    conn.insertarUsuarios(nombre, cargo, foto)
    salida=conn.leerUsuariosNombre(nombre)
    for i in salida:
        print(i[0])
        generador.generador(i[0], nombre)
