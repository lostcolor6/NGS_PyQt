import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import QtWidgets






#backend code for button b1 (when clicked prints to console)
def clicked():
    print("clickedYES")




#Window with sys.argv to know witch system its running on / what to execute
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    #window with param x,y cords where topleft corner is and width, height
    win.setGeometry(0,0,1200,800)
    #name of window
    win.setWindowTitle("basicTableGUI")

    #create a Label (where we want the label -> in the window ("win")
    label = QtWidgets.QLabel(win)
    label.setText("Chief")
    label.move(50,50)

    #Create button
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked)
    #but how to change a label for example when clicking button for example?
    #Becouse the clicked() method cant accsess the label (it is out of reach)
    #solution new class and inherit from this class "basicTable"








    #show window
    win.show()
    #exit when pressing exit button
    sys.exit(app.exec_())






    #calling function so it shows up
window()
