import math
from PyQt6.QtWidgets import (QWidget, QGridLayout)
from patientCard import PatientCard
from PyQt6.QtCore import Qt

class PatientDisplay():
	def __init__(self, layout, data, selected = None):
		super().__init__()
		self.patients = data		
		patients_per_page = 12
		self.pages = []
		total_pages = math.ceil(len(self.patients) / patients_per_page)
		self.selected = selected

		for page_index in range(total_pages):
			start = page_index * patients_per_page
			end = start + patients_per_page
			patient_subset = self.patients[start:end]
			page = self.create_patient_page(patient_subset)
			self.pages.append(page)
			layout.addWidget(page)
	def create_patient_page(self, patients):
			page = QWidget()
			layout = QGridLayout()
			row = 3
			cols = 4
			lst = []
			
			if self.selected == 'Referred':
				for i in patients:
					if i['referral'] == 1:
						lst.append(i)
			
						
			elif self.selected == 'Not Referred':
				for i in patients:
					if i['referral'] == 0:
						lst.append(i)
			elif self.selected == "All":
				lst = patients						
			else : 
				lst = patients
				
			for index, patient in enumerate(lst):
				card = PatientCard(patient)
				row = index // cols 
				col = index % cols   
				layout.addWidget(card, row, col, alignment=Qt.AlignmentFlag.AlignTop)
			page.setLayout(layout)
			return page


