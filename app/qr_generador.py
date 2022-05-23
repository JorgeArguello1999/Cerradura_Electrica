import qrcode
from PIL import Image

def generador(ID, nombre):
    cadena=ID
    cadena= str(cadena)
    image= qrcode.make(cadena)
    ruta= "imagenes/"
    nombre= nombre

    nombre_imagen= nombre +".png"
    archivo_imagen= open(ruta+nombre_imagen, 'wb')

    image.save(archivo_imagen)
    archivo_imagen.close()

if __name__=='__main__':
    generador(1, "Jorge Alexander Arguello Gusqui")
