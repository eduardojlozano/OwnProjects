# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 500, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        # creating a tool bar
        toolbar = QToolBar(self)

        # setting geometry to the tool bar
        toolbar.setGeometry(50, 100, 300, 35)

        # creating QAction Instances
        action1 = QAction("First Action", self)
        action2 = QAction("Second Action", self)
        action3 = QAction("Third Action", self)

        # adding these actions to the tool bar
        toolbar.addAction(action1)
        toolbar.addAction(action2)
        toolbar.addAction(action3)

        # creating a label
        label = QLabel("GeeksforGeeks", self)

        # setting geometry to the label
        label.setGeometry(100, 150, 200, 50)

        # adding triggered action to the first action
        action1.triggered.connect(lambda: label.setText("First Action Triggered"))

        # adding triggered action to the second action
        action2.triggered.connect(lambda: label.setText("Second Action Triggered"))

        # adding triggered action to the third action
        action3.triggered.connect(lambda: label.setText("Third Action Triggered"))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
