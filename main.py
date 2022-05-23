import cv2
import numpy as np
from pyzbar.pyzbar import decode
import database

class QR():
    cap = cv2.VideoCapture(0)

    # Establecemos el ancho y largo 
    cap.set(3,640)
    cap.set(4,480)

    # Preparar la conexion a una pequeña base de datos
    # Para trabajar con el modulo de Insertar Foto al usuario debemos pasar la ruta completa
    db=database.Conexion()

    # Abrimos la camara
    def __init__(self):
         while True:
            # Se almacena la entrada de la camara
            succes, img=self.cap.read()

            for barcode in decode(img):
                # Se obtiene el texto del codigo de barra
                mydata= barcode.data.decode('utf-8')

                # Visualizamos
                print(mydata)
            # Se muestra el frame
            cv2.imshow('Result', img)

            # Se espera antes de terminar la camara
            cv2.waitKey(1)

if __name__=='__main__':
    QR()
