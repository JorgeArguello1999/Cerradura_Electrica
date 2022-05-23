import qrcode
from PIL import Image


cadena=input("Introduzca el texto para el codigo QR: ")
image= qrcode.make(cadena)
ruta= "imagenes/"

nombre_imagen= input("Nombre de la imagen: ")+".png"
archivo_imagen= open(ruta+nombre_imagen, 'wb')

image.save(archivo_imagen)
archivo_imagen.close()
