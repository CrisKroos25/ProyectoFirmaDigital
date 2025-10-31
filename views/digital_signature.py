from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from functions.message import mostrar_mensaje
import rsa

class DigitalSignature(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/digital_signature.ui", self)

        # Conectar botones
        self.btn_load_file.clicked.connect(self.load_file)
        self.btn_signature.clicked.connect(self.crear_firma)
        self.btn_verification_key.clicked.connect(self.verificar_firma)
    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo de texto",
            "",
            "Archivos de texto (*.txt);;Todos los archivos (*)"
        )

        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                contenido = f.read()

            # Mostrar contenido en el cuadro de texto
            self.text_edit.setPlainText(contenido)

        except Exception as e:
            mostrar_mensaje("Error", f"No se pudo leer el archivo:\n{e}", "error")

    def crear_firma(self):
        try:
            # Generar claves RSA
            public_key, private_key = rsa.newkeys(1024)  # mejor 1024 que 512

            # Guardar claves
            with open("clave_publica.pem", "wb") as f:
                f.write(public_key.save_pkcs1("PEM"))

            with open("clave_privada.pem", "wb") as f:
                f.write(private_key.save_pkcs1("PEM"))

            # Obtener texto a firmar
            mensaje = self.text_edit.toPlainText().encode("utf-8")  # pasar a bytes

            # Crear firma digital
            firma = rsa.sign(mensaje, private_key, "SHA-256")

            # Guardar mensaje y firma
            with open("mensaje.txt", "wb") as f:
                f.write(mensaje)

            with open("firma.bin", "wb") as f:
                f.write(firma)

            mostrar_mensaje("Éxito", "Firma generada y archivos guardados.", "info")

        except Exception as e:
            mostrar_mensaje("Error", f"No se pudo firmar el mensaje:\n{e}", "error")

    def verificar_firma(self):

        # Cargar clave pública del remitente
        with open("clave_publica.pem", "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        # Cargar mensaje y firma
        with open("mensaje.txt", "rb") as f:
            mensaje = f.read()

        with open("firma.bin", "rb") as f:
            firma = f.read()

        # Verificar la firma digital
        try:
            rsa.verify(mensaje, firma, public_key)
            mostrar_mensaje("Info", f"La firma es válida. El mensaje proviene del remitente auténtico.", "Info")
        except rsa.VerificationError:
            mostrar_mensaje("Error", f"La firma no es válida. El mensaje pudo haber sido alterado.", "Error")

        #  Mostrar el mensaje decodificado
        print(" Mensaje recibido:", mensaje.decode('utf-8'))