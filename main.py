# Lector y Camara
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Modulo de Base de Datos
import database

# Interfaz grafica
import tkinter

class QR():
    cap = cv2.VideoCapture(0)

    # Establecemos el ancho y largo 
    cap.set(3,640)
    cap.set(4,480)

    # Preparar la conexion a una pequeña base de datos
    # Para trabajar con el modulo de Insertar Foto al usuario debemos pasar la ruta completa
    db=database.Conexion()

    # Iniciamos el modulo Grafico
    def __init__(self):
        global datos
        datos= self.db.leerUsuariosID()

    # Abrimos la camara
    def camara(self):
         while True:
            # Se almacena la entrada de la camara
            succes, img=self.cap.read()

            for barcode in decode(img):
                # Se obtiene el texto del codigo de barra
                mydata= barcode.data.decode('utf-8')
                mydata= str(mydata)

                for i in datos:
                    try:
                        if int(i[0])==int(mydata):
                            print("Iguales")
                            # print("Base de datos= ",i[0], " tipo de dato:", type(i[0]))
                            # print("Lector=", mydata, " tipo de dato:", type(mydata))
                            # Recuadro para autorizado
                            color= (0,255,0)
                            salida= True

                    except:
                        print(mydata)
                        color= (0,0,255)

                    # Coordenadas del codigo de barras
                    puntos= np.array([barcode.polygon], np.int32)
                    puntos.reshape((-1,1,2))
                    # puntos= tuple([tuple(e) for e in puntos])
                    cv2.polylines(img,
                                  [puntos],
                                  True,
                                  color,
                                  10)
            # Se muestra el frame
            cv2.imshow('Cerradura Electrica', img)

            # Se espera antes de terminar la camara
            cv2.waitKey(1)

if __name__=='__main__':
    start= QR()
    start.camara()
