import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QHBoxLayout



class SubWindow(QWidget):
    def __init__(self, label_text):
        super().__init__()
        self.setWindowTitle("Sub Window")
        self.setGeometry(200, 200, 300, 100)

        layout = QVBoxLayout()
        label = QLabel(label_text)
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(layout)

        self.sub_windows = []  # Store references to SubWindow instances

        labels = ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]
        button_layout = QHBoxLayout()  # Horizontal layout for buttons
        for i, label_text in enumerate(labels):
            button = QPushButton(f"Button {i+1}")
            button.clicked.connect(lambda _, text=label_text: self.open_window(text))
            button_layout.addWidget(button)
        layout.addLayout(button_layout)

    def open_window(self, label_text):
        sub_window = SubWindow(label_text)
        sub_window.show()
        self.sub_windows.append(sub_window)  # Store reference to the SubWindow instance


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())