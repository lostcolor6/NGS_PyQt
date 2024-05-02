import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton

# Define the main window class
class TableSortingExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Table Sorting Example')
        self.setGeometry(100, 100, 600, 400)

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create the table widget
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Set table properties
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name', 'Age', 'Country'])

        # Populate the table with sample data
        data = [
            ('John', 30, 'USA'),
            ('Alice', 25, 'Canada'),
            ('Bob', 35, 'UK'),
            ('Diana', 27, 'Australia')
        ]
        for row_index, (name, age, country) in enumerate(data):
            self.table.insertRow(row_index)
            self.table.setItem(row_index, 0, QTableWidgetItem(name))
            self.table.setItem(row_index, 1, QTableWidgetItem(str(age)))
            self.table.setItem(row_index, 2, QTableWidgetItem(country))

        # Create a button for sorting
        self.sort_button = QPushButton('Sort by Age')
        self.layout.addWidget(self.sort_button)

        # Connect the button click event to the sorting method
        self.sort_button.clicked.connect(self.sort_table_by_age)

    # Method to sort the table by age
    def sort_table_by_age(self):
        self.table.sortItems(1)  # Sort by column 1 (Age)

# Main entry point of the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableSortingExample()
    window.show()
    sys.exit(app.exec_())