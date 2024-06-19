import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QAbstractItemView, QMenu, QFileDialog,
    QPushButton, QHBoxLayout, QCheckBox, QMessageBox, QLineEdit
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1200, 600)  # Set the window geometry
        self.setWindowTitle('PyQt5 Table Example')  # Set the window title

        # Set up the main layout
        self.centralWidget = QWidget()
        self.mainLayout = QHBoxLayout(self.centralWidget)

        # Create the table
        self.createTable()
        self.mainLayout.addWidget(self.tableWidget)

        # Create the side panel with buttons, checkboxes, and text field
        self.sidePanel = QVBoxLayout()
        self.addWidgetsToSidePanel()
        self.mainLayout.addLayout(self.sidePanel)

        self.setCentralWidget(self.centralWidget)

        self.taskbar()

        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()  # Initialize the table widget
        self.tableWidget.setRowCount(10)  # Set the row count
        self.tableWidget.setColumnCount(5)  # Set the column count

        # Set the horizontal header labels
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Column 1"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Column 2"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Column 3"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Column 4"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Column 5"))

        # Set some initial cell items
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell 1"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell 2"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Cell 3"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Cell 4"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Cell 5"))

        # Allow editing cells on double-click
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)

        # Connect header section click to sort function
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.onSectionClicked)

    def onSectionClicked(self, index):
        self.tableWidget.sortByColumn(index)  # Sort the table by the clicked column

    def taskbar(self):
        self.statusBar().showMessage('Ready')  # Set the status bar message

        menubar = self.menuBar()  # Get the menu bar
        fileMenu = menubar.addMenu('File')  # Create a File menu


        # Add Open action to the File menu
        openAction = fileMenu.addAction('Open')
        openAction.triggered.connect(self.openFile)

        # Add Save action to the File menu
        saveAction = fileMenu.addAction('Save')
        saveAction.triggered.connect(self.saveFile)

        # Add Exit action to the File menu
        exitAction = fileMenu.addAction('Exit')
        exitAction.triggered.connect(self.close)

        fileMenu = menubar.addMenu('Variant')  # Create a File menu
        variantAction = fileMenu.addAction('Show Var')
        variantAction.triggered.connect(self.showVariant)

        fileMenu = menubar.addMenu('Help')  # Create a File menu
        helpAction = fileMenu.addAction('Open Doc')
        helpAction.triggered.connect(self.showDocumentation)



    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '.', 'CSV Files (*.csv)')
        if filename:
            self.tableWidget.clearContents()  # Clear the table contents
            with open(filename, 'r') as f:
                lines = f.readlines()
                for row, line in enumerate(lines[:-1]):  # Read all lines except the last one
                    items = line.strip().split(',')
                    for col, item in enumerate(items):
                        self.tableWidget.setItem(row, col, QTableWidgetItem(item))

                # Read the last line for the checkbox states and text field
                last_line = lines[-1].strip().split(',')
                self.checkbox1.setChecked(last_line[0] == 'True')
                self.checkbox2.setChecked(last_line[1] == 'True')
                self.checkbox3.setChecked(last_line[2] == 'True')
                self.textField.setText(last_line[3] if len(last_line) > 3 else '')

    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '.', 'CSV Files (*.csv)')
        if filename:
            with open(filename, 'w') as f:
                for row in range(self.tableWidget.rowCount()):
                    row_items = []
                    for col in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, col)
                        if item:
                            row_items.append(item.text())
                        else:
                            row_items.append('')
                    f.write(','.join(row_items) + '\n')

                # Save the checkbox states and text field in the last line
                last_line = [
                    str(self.checkbox1.isChecked()),
                    str(self.checkbox2.isChecked()),
                    str(self.checkbox3.isChecked()),
                    self.textField.text()
                ]
                f.write(','.join(last_line) + '\n')

    def showDocumentation(self):
        QMessageBox.information(self, "Doc", "This is the Doc:")

    def showVariant(self):
        QMessageBox.information(self, "Variant", "Something with Variants")

    def addWidgetsToSidePanel(self):
        # Button to sort the first column
        self.sortButton = QPushButton('Sort Column 1')
        self.sortButton.clicked.connect(self.sortFirstColumn)
        self.sidePanel.addWidget(self.sortButton)

        # Button to open a popup window
        self.popupButton = QPushButton('Open Popup')
        self.popupButton.clicked.connect(self.openPopup)
        self.sidePanel.addWidget(self.popupButton)

        # Adding checkboxes
        self.checkbox1 = QCheckBox('Option 1')
        self.checkbox2 = QCheckBox('Option 2')
        self.checkbox3 = QCheckBox('Option 3')

        self.sidePanel.addWidget(self.checkbox1)
        self.sidePanel.addWidget(self.checkbox2)
        self.sidePanel.addWidget(self.checkbox3)

        # Adding text field
        self.textField = QLineEdit()
        self.textField.setPlaceholderText("Enter some text")
        self.sidePanel.addWidget(self.textField)

    def sortFirstColumn(self):
        self.tableWidget.sortByColumn(0, Qt.AscendingOrder)  # Sort the first column in ascending order

    def openPopup(self):
        # Show a message box as a popup
        QMessageBox.information(self, "Popup", "This is a popup window")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
