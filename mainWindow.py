from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QWidget,
    QLabel, QPushButton, QFileDialog, QMenuBar, QMessageBox
)
from PyQt6.QtGui import QAction
from csvProcessor import process_csv
from mainLayout import mainDisplay

class DashboardWindow(QMainWindow):
	def __init__(self, data=None):
		super().__init__()
		self.setWindowTitle("Patient Dashboard")
		self.resize(1000, 600)
		self.data = data	

		
		self.create_menu()
		self.setup_styles()

		self.mainLayout = mainDisplay(self.data)
		centralWidget = QWidget(self)
		centralWidget.setLayout(self.mainLayout)
		self.setCentralWidget(centralWidget)

	def setup_styles(self):
		self.setStyleSheet("""
			background-color: #C3CEDA;
			border-radius: 5px;
			padding: 10px;
		""")

	def create_menu(self):
		menu_bar = QMenuBar(self)
		menu_bar.setStyleSheet("""
            QMenuBar { background-color: #1cb3ff; }
            QMenuBar::item:selected { background-color: #87CEFA; }
            QMenu { background-color: white; color: black; }
            QMenu::item { background-color: white; color: black; }
            QMenu::item:selected { background-color: #B0C4DE; }
        """)
		file_menu = menu_bar.addMenu("&File")
		open_action = QAction("Open a new csv", self)
		file_menu.addAction(open_action)
		open_action.triggered.connect(self.open_file)

		logout_button = QPushButton("Log Out")
		logout_button.clicked.connect(self.logout)
		menu_bar.setCornerWidget(logout_button, Qt.Corner.TopRightCorner)
		self.setMenuBar(menu_bar)

		logout_button.setStyleSheet("""
			QPushButton {
				background-color: transparent;
				border: none;
				padding: 5px;
			}
			QPushButton:hover {
				background-color: #e0e0e0;
				border-radius: 5px;
			}
		""")
	
		
	def open_file(self):
		file_dialog = QFileDialog()
		file_name, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)")
		print(_)
		
		if file_name and is_csv(file_name):
			data = process_csv(file_name)

			self.create_new_window(data)
		else:
			QMessageBox.warning(self, "Error", "The file must be in csv format!")

	def create_new_window(self, data=None):
		self.new_window = DashboardWindow(data)
		self.new_window.show()
		self.new_window.activateWindow()
		self.new_window.raise_()

	def logout(self):
		from login import Login
		self.dashboard = Login() 
		self.dashboard.show()  
		self.close()  

def is_csv(file_path):
	return file_path.lower().endswith('.csv')		
			