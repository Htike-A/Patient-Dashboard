from PyQt6.QtWidgets import  QMainWindow, QWidget
from mainLayout import mainDisplay
class NewWindow(QMainWindow):
	def __init__(self, data):
		super().__init__()
		self.setWindowTitle("Patient Dashboard1")
		self.setGeometry(100, 100, 1000, 600)

		self.setStyleSheet("""
            background-color: #1b2423;
            border-radius: 5px;
			padding: 10px;
        """)	
		self.data = data
		self.mainLayout = mainDisplay(self.data)

		centralWidget = QWidget(self)
		centralWidget.setLayout(self.mainLayout)
		self.setCentralWidget(centralWidget)
