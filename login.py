import sys, math
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
    QStackedLayout, QFileDialog, QComboBox, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QAction
from csvProcessor import process_csv
from new_window import NewWindow
from styles import*
from db import authenticate_user
from mainWindow import DashboardWindow
from adminWindow import AdminWindow

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Htikes Magic Medical Machine")
        self.resize(*window_default)
        self.setStyleSheet("background-color: #C3CEDA;")

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.welcome_label = QLabel("Welcome", self)
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        self.mainLayout.addWidget(self.welcome_label)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setStyleSheet(input_style)
        self.username_input.setFixedWidth(250)
        self.username_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.username_input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(input_style)
        self.password_input.setFixedWidth(250)
        self.password_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.password_input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.login_button = QPushButton("Login", self)
        self.login_button.setStyleSheet("""
            padding: 10px;
            font-size: 18px;
            font-weight: bold;
            background-color: #5D9CEC;
            color: white;
            border-radius: 5px;
        """)
        self.login_button.setFixedWidth(150)
        self.login_button.clicked.connect(self.handle_login)
        self.mainLayout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.centralWidget.setLayout(self.mainLayout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both username and password.")
            return

        is_authenticated, role = authenticate_user(username, password)

        if is_authenticated:
            QMessageBox.information(self, "Success", f"Login successful! Role: {role}")

            if role == "admin":
                self.admin_window = AdminWindow()
                self.admin_window.show()
            else:
                self.dashboard = DashboardWindow()
                self.dashboard.show()

            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password!")

    def logout(self):
        from login import Login
        self.login_window = Login()
        self.login_window.show()
        self.close()
