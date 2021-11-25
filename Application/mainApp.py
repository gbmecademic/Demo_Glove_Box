from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from backend import backend
from frontend import customWidgets, MainWindow, SetupWindow
import os

class SetupWindow(QtWidgets.QMainWindow, SetupWindow.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


class Application(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.setStyleSheet("background-color:white")

        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        pixmap_logo = QPixmap(os.path.join(parent_dir, 'frontend/images/mecademic-logo.png'))
        pixmap_logo = pixmap_logo.scaledToWidth(400)
        self.logo.setPixmap(pixmap_logo)

        ### Setup Window Setup ###
        self.setup_window = SetupWindow(self)


        self.RackSelection.button_list[0].clicked.connect(lambda: self.CentStatusDisplay.toggle_led(0))

        self.actionSetup.triggered.connect(self.open_setup)

    def open_setup(self):
        self.setup_window.show()