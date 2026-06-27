import qrcode


class GeneradorQR:
    def __init__(self):
        self.tabla_tamanos = {"Pequeño": 5, "Mediano": 10, "Grande": 15}
        self.tabla_colores = {"Negro": "black", "Azul": "blue", "Rojo": "red", "Verde": "green"}
        self.url_defecto = "https://www.python.org/"

    def crear_codigo_qr(self, url, tamano_texto, color_texto):
        #Genera y guarda la imagen del QR basado en los parámetros recibidos
        box_size_real = self.tabla_tamanos.get(tamano_texto, 10)
        color_real = self.tabla_colores.get(color_texto, "black")

        qr = qrcode.QRCode(
            version=1,
            box_size=box_size_real,
            border=4
        )
        qr.add_data(url)
        qr.make(fit=True)

        imagen_qr = qr.make_image(fill_color=color_real, back_color="white")
        nombre_archivo = "qr_url.png"
        imagen_qr.save(nombre_archivo)
        return nombre_archivo