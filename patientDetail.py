import sys
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel, QDialogButtonBox

class PatientDetailDialog(QDialog):
    """Dialog to show patient details"""
    def __init__(self, patient_data):
        super().__init__()        
        self.setWindowTitle("Patient Details")
        self.setGeometry(300, 200, 300, 200)
        self.setStyleSheet("""
            QDialog {
                background-color: #2E3440;
                color: white;
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
            }
            QDialogButtonBox {
                background-color: #4C566A;
                color: white;
            }
        """)
        layout = QVBoxLayout()
        
        for key, value in patient_data.items():
            layout.addWidget(QLabel(f"{key}: {value}"))
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        ctrl_w_shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        ctrl_w_shortcut.activated.connect(self.close)

        close_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        close_shortcut.activated.connect(self.close)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)       