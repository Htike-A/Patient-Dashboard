from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit
import sys

class FilterableList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Searchable List")

        # Layout
        layout = QVBoxLayout()

        # Search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search...")
        layout.addWidget(self.search_box)

        # List widget with items
        self.list_widget = QListWidget()
        self.items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grapes", "Honeydew"]
        self.list_widget.addItems(self.items)
        layout.addWidget(self.list_widget)

        # Connect search box to filter function
        self.search_box.textChanged.connect(self.filter_list)

        self.setLayout(layout)

    def filter_list(self):
        search_text = self.search_box.text().lower()  # Get text in lowercase
        self.list_widget.clear()  # Clear current list
        for item in self.items:
            if search_text in item.lower():  # Check if item contains search text
                self.list_widget.addItem(item)  # Add matching items back

# Run the app
app = QApplication(sys.argv)
window = FilterableList()
window.show()
sys.exit(app.exec())
