import sys
import numpy as np
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel, QDialogButtonBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        # Create a Matplotlib figure and axis
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

        # Sample bar chart data between 0 and 1
        categories = ["A", "B", "C", "D", "E"]
        values = np.random.rand(len(categories))  # Random values between 0 and 1

        # Create the bar chart
        self.ax.bar(categories, values, color="skyblue", edgecolor="black")
        self.ax.set_ylim(0, 1)  # Ensure y-axis is between 0 and 1
        self.ax.set_title("Bar Graph (0 to 1)")
        self.ax.set_ylabel("Value (0-1)")
        self.ax.grid(axis="y", linestyle="--", alpha=0.7)

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


        self.canvas = MplCanvas()
        layout.addWidget(self.canvas)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        ctrl_w_shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        ctrl_w_shortcut.activated.connect(self.close)

        close_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        close_shortcut.activated.connect(self.close)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)       