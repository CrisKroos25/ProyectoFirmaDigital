from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QStackedWidget
)
from PyQt6.QtCore import Qt

from views.digital_signature import DigitalSignature

class Home(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel Principal")
        self.setGeometry(200, 100, 900, 600)

        # ---------- CONTENEDOR PRINCIPAL ----------
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        # ---------- PANEL SUPERIOR DE BOTONES ----------
        button_bar = QHBoxLayout()
        self.btn_keys = QPushButton("🔑")
        self.btn_encryptaption = QPushButton("🔒")
        self.btn_digital = QPushButton("📝")

        for btn in (self.btn_keys, self.btn_encryptaption, self.btn_digital):
            btn.setFixedHeight(40)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)

        button_bar.addWidget(self.btn_keys)
        button_bar.addWidget(self.btn_encryptaption)
        button_bar.addWidget(self.btn_digital)
        button_bar.addStretch()

        # ---------- STACK DE CONTENIDOS ----------
        self.stack = QStackedWidget()

        # Página 2: Firma digital
        self.digital_signature_page = DigitalSignature()

        # Agregar al stack

        self.stack.addWidget(self.digital_signature_page)

        # ---------- Agregar al layout principal ----------
        main_layout.addLayout(button_bar)
        main_layout.addWidget(self.stack)

        # ---------- Conexiones ----------

        self.btn_digital.clicked.connect(self.show_signature_page)

        # Página inicial
        self.stack.setCurrentIndex(1)

    # Métodos de cambio de vista

    def show_signature_page(self):
        self.stack.setCurrentWidget(self.digital_signature_page)

