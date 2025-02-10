import sys, math
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QStackedLayout, QFileDialog
)
from PyQt6.QtGui import QAction
from patientCard import PatientCard
from csvProcessor import process_csv

class DashboardWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Patient Dashboard")
		self.resize(1000, 600)

		self.setStyleSheet("""
            background-color: #1b2423;
            border-radius: 5px;
			padding: 10px;
        """)	
		self.mainLayout = QVBoxLayout()
		menuBar = self.menuBar()
		file_menu = menuBar.addMenu("File")

		open_action = QAction("Open", self)
		open_action.triggered.connect(self.open_file)

		file_menu.addAction(open_action)

		open_menu = menuBar.addMenu("Placeholder")
		open_menu.addAction("Go")
				
		centralWidget = QWidget(self)
		centralWidget.setLayout(self.mainLayout)
		self.setCentralWidget(centralWidget)

		self.stackedLayout = QStackedLayout()
		self.mainLayout.addLayout(self.stackedLayout)
		#data
		data = process_csv('Feeding Dashboard data.csv')
		""" self.patients = [
            {"id": f"{100 + i}", "name": f"Patient {i}", "bmi": f"{18 + i*0.5:.1f}", "status": "Yes" if i % 2 == 0 else "No"}
            for i in range(100) 
        ] """
		#self.patients = [{"id": f"{data['encounterId']}", "bmi": f"{18 + i*0.5:.1f}", "status": "Yes" if i % 2 == 0 else "No"} for i in range(len(data))]
		ids = []
		encounterIDs = data['encounterId']
		for key, item in encounterIDs.items():
			ids.append(item)
		self.patients = [{"id": f"{i}", "bmi": f"{18 + i*0.5:.1f}", "status": "Yes" if i % 2 == 0 else "No"} for i in ids]
		self.patients_per_page = 12
		self.pages = []
		self.total_pages = math.ceil(len(self.patients) / self.patients_per_page)

		for page_index in range(self.total_pages):
			start = page_index * self.patients_per_page
			end = start + self.patients_per_page
			patient_subset = self.patients[start:end]
			page = self.create_patient_page(patient_subset)
			self.pages.append(page)
			self.stackedLayout.addWidget(page)	

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

		self.page_counter = QLabel("", self)
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
		self.mainLayout.addLayout(navLayout)

		self.current_page = 0
		self.update_page_number()

	def create_patient_page(self, patients):
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
		return page

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
		

	def open_file(self):
		file_dialog = QFileDialog()
		file_path, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)")
		if file_path:
			self.process_csv(file_path)

	def process_csv(file_path):
		pass