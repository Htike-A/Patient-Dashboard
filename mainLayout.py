from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QStackedLayout, QPushButton)
from patientCard import PatientCard
from csvProcessor import process_csv
from patientWindow import PatientDisplay
class mainDisplay(QVBoxLayout):
	def __init__(self, data = None):
		super().__init__()
		filter_layout = QHBoxLayout()
		filter_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

		self.filter_options = QLabel("Filter")
		self.dropdown = QComboBox()
		self.dropdown.addItems(["None", "Referred", "Not Referred"])
		self.selection = self.dropdown.currentText
		#self.dropdown.currentTextChanged.connect(self.update_display)

		filter_layout.addWidget(self.filter_options)
		filter_layout.addWidget(self.dropdown)

		self.addLayout(filter_layout)

		self.stackedLayout = QStackedLayout()
		self.addLayout(self.stackedLayout)
		self.data = data		
		if self.data == None:
			data = process_csv('Feeding Dashboard data.csv')
		else: data = self.data
		display = PatientDisplay(self.stackedLayout, data, self.selection)
		self.pages = display.pages
		""" self.patients = data		
		self.patients_per_page = 12
		self.pages = []
		self.total_pages = math.ceil(len(self.patients) / self.patients_per_page)

		for page_index in range(self.total_pages):
			start = page_index * self.patients_per_page
			end = start + self.patients_per_page
			patient_subset = self.patients[start:end]
			page = self.create_patient_page(patient_subset)
			self.pages.append(page)
			self.stackedLayout.addWidget(page)	 """

		navLayout = QHBoxLayout()
		navLayout.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.btn_prev = QPushButton("⬅")
		
		self.btn_prev.setStyleSheet(
			"""
				QPushButton {
					color: black;

					
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
		self.btn_prev.clicked.connect(self.prev_page)

		self.page_counter = QLabel("")
		self.page_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.page_counter.setStyleSheet(
			"""
				QLabel {
					color: black;
					font-size: 14px;
				
				}
		  	"""
		)
		self.btn_next = QPushButton("➡")

		self.btn_next.setStyleSheet(
			"""
				QPushButton {
					color: black;
					
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
		self.btn_next.clicked.connect(self.next_page)
		navLayout.addWidget(self.btn_prev)
		navLayout.addWidget(self.page_counter)
		navLayout.addWidget(self.btn_next)
		self.addLayout(navLayout)

		self.current_page = 0
		self.update_page_number()

	""" def create_patient_page(self, patients):
		page = QWidget()
		layout = QGridLayout()
		row = 3
		cols = 4
		for index, patient in enumerate(patients):
			card = PatientCard(patient)
			row = index // cols 
			col = index % cols   
			layout.addWidget(card, row, col, alignment=Qt.AlignmentFlag.AlignTop)
		page.setLayout(layout)
		return page """

	def next_page(self):
		if self.current_page < len(self.pages ) - 1:
			self.current_page += 1
			self.stackedLayout.setCurrentIndex(self.current_page)
		self.update_page_number()
		""" if self.current_page > self.total_pages - 2:
			self.btn_next.setEnabled(False) """
	def prev_page(self):
		if self.current_page > 0:
			self.current_page -= 1
			self.stackedLayout.setCurrentIndex(self.current_page)
		self.update_page_number()
		""" if self.current_page < 1:
			self.btn_prev.setEnabled(False) """
	def update_page_number(self):

		self.btn_next.setEnabled(self.current_page < len(self.pages) - 1)
		self.btn_prev.setEnabled(self.current_page > 0)
		self.page_counter.setText(f"Page {self.current_page + 1} of {len(self.pages)}")
