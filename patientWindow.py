import math
from PyQt6.QtWidgets import QWidget, QGridLayout
from patientCard import PatientCard
from PyQt6.QtCore import Qt

class PatientDisplay():
    def __init__(self, layout, data, selected=None):
        super().__init__()
        self.patients = data
        self.patients_per_page = 12
        self.pages = []
        self.selected = selected

        filtered_patients = self.filter_patients()

        total_pages = math.ceil(len(filtered_patients) / self.patients_per_page)

        for page_index in range(total_pages):
            start = page_index * self.patients_per_page
            end = start + self.patients_per_page
            patient_subset = filtered_patients[start:end]

            if not patient_subset:
                continue  

            page = self.create_patient_page(patient_subset)
            self.pages.append(page)
            layout.addWidget(page)

    def filter_patients(self):
        """Filters patients based on the 'selected' criteria."""
        if self.selected == "Referred":
            return [p for p in self.patients if p.get("referral") == 1]
        elif self.selected == "Not Referred":
            return [p for p in self.patients if p.get("referral") == 0]
        return self.patients

    def create_patient_page(self, patients):
        """Creates a page layout displaying patient cards in a grid."""
        page = QWidget()
        layout = QGridLayout()
        cols = 4  

        for index, patient in enumerate(patients):
            card = PatientCard(patient)
            row, col = divmod(index, cols)  
            layout.addWidget(card, row, col, alignment=Qt.AlignmentFlag.AlignTop)

        page.setLayout(layout)
        return page