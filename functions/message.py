from PyQt6.QtWidgets import QMessageBox

def mostrar_mensaje(titulo, mensaje, tipo="info"):
    msg = QMessageBox()
    if tipo == "error":
        msg.setIcon(QMessageBox.Icon.Critical)
    else:
        msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowTitle(titulo)
    msg.setText(mensaje)
    msg.exec()
