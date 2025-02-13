from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QFrame, QLabel, QVBoxLayout, QPushButton)
from patientDetail import PatientDetailDialog
from csvProcessor import process_csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas




class PatientCard(QFrame):
	def __init__(self, data):
		super().__init__()
		self.setFixedSize(210, 185)
		self.setStyleSheet("""
            background-color: #728281;
            border-radius: 5px;
			padding: 5px;

        """)
		self.data = data

		name_label = QLabel(f"👤 ID: {self.data["encounterId"]}")
		bmi_label = QLabel(f"BMI: {self.data["bmi"]:.2f}")
		if self.data['referral'] == 1:
			condition_label = QLabel(f"Referral: Yes")
		else:
			condition_label = QLabel(f"Referral: No")
		layout = QVBoxLayout(self)

		# Aligning text
		name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		bmi_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		condition_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		if self.data["referral"] == 0 :
			condition_label.setStyleSheet(
				"""
				color: green;
				"""
			)
		else:
			condition_label.setStyleSheet(
				"""
				color: red;
				"""
			)

		""" condition_label.setStyleSheet(
            
		) """

		layout.addWidget(name_label)
		layout.addWidget(bmi_label)
		layout.addWidget(condition_label)
		self.view_detail_button = QPushButton("View Patient Details")
		self.view_detail_button.clicked.connect(self.view_detail)
		self.view_detail_button.setStyleSheet(
			"""
				QPushButton {
					color: black;

					border: 1px solid black;
				}
				QPushButton:hover {
					color: black;
					background-color: #7baba7;
				}
				QPushButton:pressed {
					background-color: #0aa89b;
				}
			"""
		)
		layout.addWidget(self.view_detail_button)


	def view_detail(self):
		detail_window = PatientDetailDialog(self.data)
		detail_window.exec()