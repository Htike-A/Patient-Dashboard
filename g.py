import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
from mainWindow import DashboardWindow


def main():
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    