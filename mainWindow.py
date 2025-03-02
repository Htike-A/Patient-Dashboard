import sys, math
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
	QApplication,
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QStackedLayout, QFileDialog, QComboBox, QMenuBar
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
		menu_bar = QMenuBar(self)
		menu_bar.setStyleSheet("""
            QMenuBar { background-color: #1cb3ff; }
            QMenuBar::item:selected { background-color: #87CEFA; }
            QMenu { background-color: white; color: black; }
            QMenu::item { background-color: white; color: black; }
            QMenu::item:selected { background-color: #B0C4DE; }
        """)
		file_menu = menu_bar.addMenu("File")
		open_action = QAction("Open a new csv", self)
		file_menu.addAction(open_action)
		logout_button = QPushButton("Log Out")
		menu_bar.setCornerWidget(logout_button, Qt.Corner.TopRightCorner)
		open_action.triggered.connect(self.open_file)
		logout_button.clicked.connect(self.logout)
		self.setMenuBar(menu_bar)
				
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

	def logout(self):
		from login import Login
		self.dashboard = Login() 
		self.dashboard.show()  
		self.close()  
			