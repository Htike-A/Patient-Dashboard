import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel

class PatientDetailDialog(QDialog):
    """Dialog to show patient details"""
    def __init__(self, patient_data):
        super().__init__()

        self.setWindowTitle("Patient Details")
        self.setGeometry(300, 200, 300, 200)

        layout = QVBoxLayout()
        
        for key, value in patient_data.items():
            layout.addWidget(QLabel(f"{key}: {value}"))
        self.setLayout(layout)