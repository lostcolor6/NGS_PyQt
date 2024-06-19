import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QAbstractItemView, QMenu, QFileDialog,
    QPushButton, QHBoxLayout, QCheckBox, QMessageBox, QLineEdit,
    QLabel, QHeaderView, QGridLayout, QDialog
)
from PyQt5.QtCore import Qt

# VCF data as a string (normaly this would be read from a file)
vcf_data = """\
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	NA12878_73
chr1	2556714	.	A	G	5200	.	MQM=60;SAP=23;SAR=123;SAF=80;ABP=19	GT:DP:AO:GQ	0/1:465:203:136
chr2	2559766	.	C	T	4507	off-target	MQM=60;SAP=262;SAR=17;SAF=164;ABP=13	GT:DP:AO:GQ	0/1:324:181:138
chr3	2562891	.	G	A	10042	.	MQM=60;SAP=228;SAR=310;SAF=103;ABP=12	GT:DP:AO:GQ	0/1:886:413:141
chr4	2563346	.	G	A	3516	off-target	MQM=60;SAP=158;SAR=122;SAF=21;ABP=7	GT:DP:AO:GQ	0/1:265:143:136
chr5	4789324	.	T	C	7281	.	MQM=60;SAP=13;SAR=121;SAF=156;ABP=12	GT:DP:AO:GQ	0/1:603:277:160
chr6	4895802	.	C	T	12548	.	MQM=60;SAP=32;SAR=209;SAF=291;ABP=58	GT:DP:AO:GQ	0/1:1172:500:160
chr7	4896010	.	T	C	584	off-target	MQM=60;SAP=70;SAR=31;SAF=0;ABP=3	GT:DP:AO:GQ	0/1:62:31:144
chr8	6197766	.	T	C	9275	.	MQM=60;SAP=321;SAR=308;SAF=72;ABP=44	GT:DP:AO:GQ	0/1:889:380:133
chr9	6197796	.	G	A	6672	off-target	MQM=60;SAP=451;SAR=263;SAF=21;ABP=10	GT:DP:AO:GQ	0/1:611:284:160
chr10	7374483	.	C	T	7314	.	MQM=60;SAP=3;SAR=140;SAF=148;ABP=45	GT:DP:AO:GQ	0/1:691:288:133
chr11	7460069	.	C	T	14337	.	MQM=60;SAP=7;SAR=297"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1600, 800)  # Set the window geometry
        self.setWindowTitle('GUI')  # Set the window title


        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.gridLayout = QGridLayout()
        centralWidget.setLayout(self.gridLayout)

        # Adding widgets to the grid layout
        #Table at top left Corner
        self.createTable()
        self.gridLayout.addWidget(self.tableWidget, 0, 0)

        #Adding side panel at top right corner cell
        self.filterSidePanel = QVBoxLayout()
        self.addWidgetsToSidePanel()
        self.gridLayout.addLayout(self.filterSidePanel, 0, 10)


        # Stretching the second column
        self.gridLayout.setColumnStretch(0, 2)  # Stretch column 1 to occupy twice the space of column 0

        #add taskbar
        self.taskbar()

        #to make window visiable
        self.show()





    def createTable(self):
        self.tableWidget = QTableWidget()  # Initialize the table widget
        self.tableWidget.setColumnCount(12)  # Set the column count

        # Set the horizontal header labels
        headers = ["#CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "NA12878_73"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Populate table with VCF data
        self.populateTableWithVCFData(vcf_data)

        # Allow editing cells on double-click
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)

        # Connect header section click to sort function
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.onSectionClicked)

        # Stretch headers to fill the table
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QHeaderView.Stretch)  # Stretch INFO column
        self.tableWidget.horizontalHeader().setSectionResizeMode(8, QHeaderView.Stretch)  # Stretch FORMAT column

        # Enable interactive resizing of columns
        self.tableWidget.horizontalHeader().setSectionsMovable(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)






    def populateTableWithVCFData(self, vcf_data):
        lines = vcf_data.strip().split('\n')
        self.tableWidget.setRowCount(len(lines) - 1)  # Exclude header line

        for row, line in enumerate(lines[1:]):  # Skip the header line
            items = line.split('\t')
            for col, item in enumerate(items):
                self.tableWidget.setItem(row, col, QTableWidgetItem(item))





    def onSectionClicked(self, index):
        # Sort the table by the clicked column
        self.tableWidget.sortByColumn(index, Qt.AscendingOrder)




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

        fileMenu = menubar.addMenu('Help')  # Create a Help menu
        helpAction = fileMenu.addAction('Open Doc')
        helpAction.triggered.connect(self.showDocumentation)






    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '.', 'VCF Files (*.vcf);;All Files (*)')
        if filename:
            self.tableWidget.clearContents()  # Clear the table contents
            with open(filename, 'r') as f:
                vcf_data = f.read()
                self.populateTableWithVCFData(vcf_data)






    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '.', 'CSV Files (*.csv);;All Files (*)')
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
                    f.write('\t'.join(row_items) + '\n')





    def showDocumentation(self):
        QMessageBox.information(self, "Documentation", "This is the documentation.")




    def addWidgetsToSidePanel(self):
        # Button to sort the first column
        self.sortButton = QPushButton('Sort by QUAL')
        self.sortButton.clicked.connect(self.sortByQUAL)
        self.filterSidePanel.addWidget(self.sortButton)

        # Button to open a popup window
        #self.popupButton = QPushButton('Open Popup')
        #self.popupButton.clicked.connect(self.openPopup)
        #self.filterSidePanel.addWidget(self.popupButton)


        # Adding buttons to the grid layout
        self.openPopupButton = QPushButton('Open Window')
        self.openPopupButton.clicked.connect(self.openPopupWindow)
        self.filterSidePanel.addWidget(self.openPopupButton)

        # Adding checkboxes for filtering
        self.filterOffTarget = QCheckBox('Show Off-Target')
        self.filterOffTarget.setChecked(True)
        self.filterOffTarget.stateChanged.connect(self.filterTable)
        self.filterSidePanel.addWidget(self.filterOffTarget)

        # Adding text field for filtering by minimum QUAL
        self.minQualLabel = QLabel('Min QUAL:')
        self.filterSidePanel.addWidget(self.minQualLabel)

        self.minQualField = QLineEdit()
        self.minQualField.setPlaceholderText("Enter min QUAL")
        self.minQualField.textChanged.connect(self.filterTable)
        self.filterSidePanel.addWidget(self.minQualField)

        # Add stretch to push widgets to the top
        self.filterSidePanel.addStretch()


    def openPopupWindow(self):
        popup = PopupWindow()
        popup.exec_()


    def sortByQUAL(self):
        self.tableWidget.sortByColumn(5, Qt.AscendingOrder)  # Sort the QUAL column in ascending order

    def filterTable(self):
        showOffTarget = self.filterOffTarget.isChecked()
        try:
            minQual = float(self.minQualField.text())
        except ValueError:
            minQual = 0

        for row in range(self.tableWidget.rowCount()):
            qual = float(self.tableWidget.item(row, 5).text())
            filter_status = self.tableWidget.item(row, 6).text()
            hide_row = (not showOffTarget and filter_status == 'off-target') or (qual < minQual)
            self.tableWidget.setRowHidden(row, hide_row)






    #def openPopup(self):
        # Show a message box as a popup
     #   QMessageBox.information(self, "Popup", "This is a popup window")






class PopupWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Popup Window')
        self.setGeometry(200, 200, 400, 300)

        layout = QGridLayout()

        label = QLabel('PopupWindow')
        layout.addWidget(label,0,1)

        closeButton = QPushButton('Close')
        closeButton.clicked.connect(self.close)
        layout.addWidget(closeButton,0,0)

        self.setLayout(layout)











if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


