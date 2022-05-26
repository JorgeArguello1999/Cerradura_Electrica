# Lector y Camara
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Modulo de Base de Datos
import database

cap = cv2.VideoCapture(0)
# Establecemos el ancho y largo 
cap.set(3,640)
cap.set(4,480)
db=database.Conexion()

# Abrimos la camara
def camara():
    succes, img=cap.read()
    datos= db.leerUsuariosID()

    for barcode in decode(img):
        # Se obtiene el texto del codigo de barra
        mydata= barcode.data.decode('utf-8')
        mydata= str(mydata)
        acumulador=0 # Se intenta crear un sistema que contabilize el nivel de exito
        color= (0,0,0)
        for i in datos:
            try:
                if int(i[0])==int(mydata):
                    # Recuadro para autorizado
                    color= (0,255,0)
                    salida= True
                    print("Esta es la salida: ",salida, "Usuario:", i[0])
                    myouput= i[1]
                    # Cuadrado para el texto
                    pts2=barcode.rect
                    # Contenido del cuadro
                    cv2.putText(img,
                        myouput,
                        (pts2[0], pts2[1]),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        color,
                        3)
            except:
                print("La entrada no es de las tarjetas: ", mydata)
                color= (0,0,255)

            # Coordenadas del codigo de barras
            puntos= np.array([barcode.polygon], np.int32)
            puntos.reshape((-1,1,2))
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
    while True:
        camara()
