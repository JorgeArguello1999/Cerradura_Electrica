# Cerradura_Electrica
Sistema de verificación utilizando QR Code para habilitar la cerradura, uso de arduino para la creación del mecanismo 
# Requisitos
## Instalar qrcode
Es un conjunto de herramientas necesarias para la creacion del QrCode, esto es muy primitivo
```bash
pip install qrcode
```
## Instalar opencv
Librerias especializadas en el uso de la camara para reconocimiento de elementos en este caso el QrCode
```bash
pip install opencv-contrib-python
```
## Instalar libzbar
Modulo importante para la gestión de codigo de barras
```bash
sudo apt install libzbar.dev
pip install pyzbar
```
## Instalar SQLite3 
Pequeño gestor de base de datos para la gestión de todos los usuarios a trabajar
```bash
sudo apt install sqlite3
pip install pysqlite3
```
