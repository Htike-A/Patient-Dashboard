import sys, math
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
	QApplication,
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QStackedLayout, QFileDialog, QComboBox
)
from PyQt6.QtGui import QAction
from patientCard import PatientCard
from csvProcessor import process_csv
from patientWindow import PatientDisplay
from mainLayout import mainDisplay
from new_window import NewWindow


class DashboardWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Patient Dashboard")
		self.resize(1000, 600)

		self.setStyleSheet("""
            background-color: #C3CEDA;
            border-radius: 5px;
			padding: 10px;
        """)	
		
		self.mainLayout = mainDisplay()
		menuBar = self.menuBar()
		file_menu = menuBar.addMenu("File")

		open_action = QAction("Open a new csv", self)
		open_action.triggered.connect(self.open_file)

		file_menu.addAction(open_action)

		open_menu = menuBar.addMenu("Placeholder")
		open_menu.addAction("Go")
				
		centralWidget = QWidget(self)
		centralWidget.setLayout(self.mainLayout)
		self.setCentralWidget(centralWidget)

	def open_file(self):
		file_dialog = QFileDialog()
		file_name, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)")
		if file_name:
			#self.stackedLayout.removeWidget(display.pages)
			data = process_csv(file_name)

			self.newWindow = NewWindow(data)
			self.newWindow.show()
			