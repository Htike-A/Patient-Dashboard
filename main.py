import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
from login import Login

QApplication.setAttribute(Qt.ApplicationAttribute.AA_DontUseNativeMenuBar)

def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
    