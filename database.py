import sqlite3 as sql

class Conexion():

    def __init__(self):
        try:
            self.conn= sql.connect("Usuarios.db")

        except sql.Error as e:
            print("Ocurrio Error en la conexion\n", e)

    def crearBaseDatos(self):
        cursor= self.conn.cursor()
        try:
            cursor.execute("""
            CREATE TABLE "Usuarios" (
	        "ID"	    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	        "Nombre"    TEXT NOT NULL,
                "Cargo"	    TEXT NOT NULL,
	        "Foto"	BLOB
            );
            """)
        except sql.Error as e:
            print("La Base de datos ya ha sido creada", e)

        self.conn.commit()
        self.conn.close()

    # El parametro de Foto es para la ruta, la funcion interna convertira la imagen en binario
    def insertarUsuarios(self, nombre, cargo, foto):
        # Abrimos la ruta completa del archivo ej(/imagenes/usuarioA.jpeg) 
        foto= open(foto, 'rb')
        foto= foto.read()

        cursor= self.conn.cursor()
        cursor.execute("INSERT INTO Usuarios (Nombre, Cargo, Foto) VALUES ({nombre}, {cargo},{foto}) ")

        self.conn.commit()
        self.conn.close()

    def leerUsuarios(self):
        cursor= self.conn.cursor()
        cursor.execute("SELECT * FROM ID")
        datos= cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return datos


if __name__=='__main__':
    db= Conexion()
