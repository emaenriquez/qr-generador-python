
import qrcode

# Texto o datos que deseas codificar en el QR
data = "Hola, este es un código QR generado con Python."

# Crear un objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Versión del código QR (1-40, 1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel de corrección de errores (H para alta)
    box_size=10,  # Tamaño de cada cuadro en el código QR
    border=4,  # Tamaño del borde del código QR
)

# Agregar los datos al código QR
qr.add_data(data)
qr.make(fit=True)

# Crear una imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen en un archivo
img.save("codigo_qr.png")

# Mostrar la imagen (opcional)
img.show()
