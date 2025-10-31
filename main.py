# main.py
import sys
from PyQt6.QtWidgets import QApplication
from views.home import Home

def main():
    app = QApplication(sys.argv)

    # Cargar estilo
    with open("styles/stylesdark.qss", "r") as f:
        qss = f.read()
        app.setStyleSheet(qss)

    # Solo crear la ventana si hay usuario válido
    w = Home()
    w.setMinimumWidth(520)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
