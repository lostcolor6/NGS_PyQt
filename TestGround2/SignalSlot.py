from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QVBoxLayout, QWidget

def show_message():
    QMessageBox.information(None, "Info", "Button wurde geklickt!")

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

button = QPushButton("Klick mich!")
button.clicked.connect(show_message)  # Verbindung von Signal und Slot

layout.addWidget(button)
window.setLayout(layout)

window.show()
app.exec_()