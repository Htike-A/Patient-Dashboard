import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QComboBox, QMessageBox, QMenuBar
)
from PyQt6.QtGui import QAction
from db import register_user
from mainWindow import DashboardWindow

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Panel")
        self.resize(1000, 600)

        self.setStyleSheet("""
            background-color: #C3CEDA;
            padding: 10px;
        """)

        self.mainLayout = QVBoxLayout()

        menu_bar = QMenuBar(self)
        menu_bar.setStyleSheet("""
            QMenuBar { background-color: #1cb3ff; }
            QMenuBar::item:selected { background-color: #87CEFA; }
            QMenu { background-color: white; color: black; }
            QMenu::item { background-color: white; color: black; }
            QMenu::item:selected { background-color: #B0C4DE; }
        """)

        file_menu = menu_bar.addMenu("File")
        main_dashboard_action = QAction("View Patient Data", self)
        file_menu.addAction(main_dashboard_action)
        logout_button = QPushButton("Log Out")
        menu_bar.setCornerWidget(logout_button, Qt.Corner.TopRightCorner)

        main_dashboard_action.triggered.connect(self.open_dashboard)
        logout_button.clicked.connect(self.logout)
        self.setMenuBar(menu_bar)

        # 🟢 Input form area with background color from uploaded image
        self.formWidget = QWidget()
        self.formWidget.setStyleSheet("""
            background-color: #6E8AAE;
            border-radius: 10px;
            padding: 20px;
        """)
        formLayout = QVBoxLayout(self.formWidget)
        formLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title_label = QLabel("Admin Panel - Add New User", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        formLayout.addWidget(self.title_label)

        input_style = """
            QLineEdit {
                background-color: white;
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
                color: black;
            }
            
            QComboBox {
                background-color: white;
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
                color: black;
            }

            QComboBox::drop-down {
                border: none;
                width: 25px;
            }

            QComboBox::down-arrow {
                image: url(arrow_down.png);  /* Custom dropdown arrow */
                width: 10px;
                height: 10px;
            }
        """

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter New Username")
        self.username_input.setFixedWidth(250)
        self.username_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.username_input.setStyleSheet(input_style)
        formLayout.addWidget(self.username_input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedWidth(250)
        self.password_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_input.setStyleSheet(input_style)
        formLayout.addWidget(self.password_input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.role_dropdown = QComboBox(self)
        self.role_dropdown.addItems(["user", "admin"])
        self.role_dropdown.setFixedWidth(250)
        self.role_dropdown.setStyleSheet(input_style)
        formLayout.addWidget(self.role_dropdown, alignment=Qt.AlignmentFlag.AlignCenter)

        self.add_user_button = QPushButton("Add User", self)
        self.add_user_button.setFixedWidth(150)
        self.add_user_button.setStyleSheet("""
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            background-color: #5D9CEC;
            color: white;
            border-radius: 5px;
        """)
        self.add_user_button.clicked.connect(self.add_user)
        formLayout.addWidget(self.add_user_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.formWidget, alignment=Qt.AlignmentFlag.AlignCenter)

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)

    def add_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        role = self.role_dropdown.currentText()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter a username and password.")
            return

        if register_user(username, password, role):
            QMessageBox.information(self, "Success", f"User '{username}' added successfully with role '{role}'!")
            self.username_input.clear()
            self.password_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Username already exists!")

    def open_dashboard(self):
        self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.close()

    def logout(self):
        from login import Login
        self.login_window = Login()
        self.login_window.show()
        self.close()
