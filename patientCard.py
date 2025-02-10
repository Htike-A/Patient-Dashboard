from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QFrame, QLabel, QVBoxLayout, QPushButton)
from patientDetail import PatientDetailDialog

class PatientCard(QFrame):
	def __init__(self, data):
		super().__init__()
		self.setFixedSize(210, 185)
		self.setStyleSheet("""
            background-color: #728281;
            border-radius: 5px;
			padding: 5px;

            border: 1px solid black;
        """)
		self.data = data

		name_label = QLabel(f"👤 ID: {data["id"]}")
		bmi_label = QLabel(f"BMI: ")
		condition_label = QLabel(f"Referral: {data["status"]}")
		layout = QVBoxLayout(self)

		# Aligning text
		name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		bmi_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		condition_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		if data["status"] == 'Yes' :
			condition_label.setStyleSheet(
				"""
				color: red;
				"""
			)
		else:
			condition_label.setStyleSheet(
				"""
				color: green;
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

					border: 1px solid gray;
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