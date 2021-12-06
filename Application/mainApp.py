from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from backend.backend import MainRack, Centrifuge
from frontend import customWidgets, MainWindow, SetupWindow
from mecademicpy.robot import CommunicationError, Robot
import os
import re

class SetupWindow(QtWidgets.QMainWindow, SetupWindow.Ui_MainWindow):
    def __init__(self, rack, centrifuge, *args, **kwargs):
        self.rack = rack
        self.centrifuge = centrifuge
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.save_position)

    def save_position(self):
        if self.cent_pos_1.text():
            pos = self._text_to_list(self.cent_pos_1.text())
            self.centrifuge.update_position(0, pos)

        if self.cent_pos_2.text():
            pos = self._text_to_list(self.cent_pos_2.text())
            self.centrifuge.update_position(1, pos)

        if self.cent_pos_3.text():
            pos = self._text_to_list(self.cent_pos_3.text())
            self.centrifuge.update_position(2, pos)

        if self.cent_pos_4.text():
            pos = self._text_to_list(self.cent_pos_4.text())
            self.centrifuge.update_position(3, pos)

        if self.cent_pos_5.text():
            pos = self._text_to_list(self.cent_pos_5.text())
            self.centrifuge.update_position(4, pos)

        if self.cent_pos_6.text():
            pos = self._text_to_list(self.cent_pos_6.text())
            self.centrifuge.update_position(5, pos)

        if self.rack_pos_1.text():
            pos = self._text_to_list(self.rack_pos_1.text())
            self.rack.update_position(0, pos)

        if self.rack_pos_2.text():
            pos = self._text_to_list(self.rack_pos_2.text())
            self.rack.update_position(1, pos)
            
        if self.rack_pos_3.text():
            pos = self._text_to_list(self.rack_pos_3.text())
            self.rack.update_position(2, pos)

        if self.rack_pos_4.text():
            pos = self._text_to_list(self.rack_pos_4.text())
            self.rack.update_position(3, pos)

        if self.rack_pos_5.text():
            pos = self._text_to_list(self.rack_pos_5.text())
            self.rack.update_position(4, pos)

        if self.rack_pos_6.text():
            pos = self._text_to_list(self.rack_pos_6.text())
            self.rack.update_position(5, pos)





    def _text_to_list(self, text):
        text = re.sub('[()]', '', text)
        text_split = text.split(',')
        num_list = [float(i) for i in text_split]
        return num_list
        


class Application(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        ### Frontend setup ###
        
        self.setStyleSheet("background-color:white")

        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        pixmap_logo = QPixmap(os.path.join(parent_dir, 'frontend/images/mecademic-logo.png'))
        pixmap_logo = pixmap_logo.scaledToWidth(400)
        self.logo.setPixmap(pixmap_logo)

        ### Backend setup ###
        self.robot = Robot()
        self.rack = MainRack(6)
        self.centrifuge = Centrifuge(6)

        ### Setup Window Setup ###
        self.setup_window = SetupWindow(self.rack, self.centrifuge)

        self.actionSetup.triggered.connect(self.open_setup)

        ### Button connections ###

        self.LoadButton.clicked.connect(self.load_centrifuge)
        self.RackSelection.button_list[0].clicked.connect(lambda: self.toggle_select_vial(0))
        self.RackSelection.button_list[1].clicked.connect(lambda: self.toggle_select_vial(1))
        self.RackSelection.button_list[2].clicked.connect(lambda: self.toggle_select_vial(2))
        self.RackSelection.button_list[3].clicked.connect(lambda: self.toggle_select_vial(3))
        self.RackSelection.button_list[4].clicked.connect(lambda: self.toggle_select_vial(4))
        self.RackSelection.button_list[5].clicked.connect(lambda: self.toggle_select_vial(5))

        self.buttonCentrifuge.clicked.connect(self.start_centrifuge)
        self.buttonRobot.clicked.connect(self.connect_to_robot)


    def open_setup(self):
        self.setup_window.show()

    def toggle_select_vial(self, n):
        self.rack.vial_selected[n] = not self.rack.vial_selected[n]

    def connect_to_robot(self):
        if not self.robot.IsConnected():
            try:
                self.robot.Connect()
                self.robot.ActivateAndHome()
                self.robot.WaitHomed()
                self.buttonRobot.setStyleSheet("background-color:rgba(0,255,0,255)")
            except CommunicationError as e:
                print(e)
        else:
            self.robot.Disconnect()
            self.buttonRobot.setStyleSheet("background-color:rgba(0,0,0,125)")

    def load_centrifuge(self):
        # Check centrifuge status
        if not self.centrifuge.cent_status:
            msgbox = QtWidgets.QMessageBox()
            msgbox.setIcon(QtWidgets.QMessageBox.Information)
            msgbox.setText("Centrifuge is not ready to be loaded.")
            msgbox.setWindowTitle("Centrifuge Warning")
            msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

            msgbox.exec()
            return

        if True in self.centrifuge.rack_status:
            msgbox = QtWidgets.QMessageBox()
            msgbox.setIcon(QtWidgets.QMessageBox.Information)
            msgbox.setText("There are still vials in the centrifuge.")
            msgbox.setWindowTitle("Centrifuge Warning")
            msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

            msgbox.exec()
            return
        # Check selected vials status
        if not (True in self.rack.vial_selected):
            msgbox = QtWidgets.QMessageBox()
            msgbox.setIcon(QtWidgets.QMessageBox.Information)
            msgbox.setText("Please select one or multiple vials before loading.")
            msgbox.setWindowTitle("Rack Warning")
            msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

            msgbox.exec()
            return
        # Load them in the centrifuge

        for i, st in enumerate(self.rack.vial_selected):
            if st:
                self.RackStatusDisplay.turn_vial_off(i)
                # Move to pick
                pick_pos = self.rack.rack_position[i].copy()
                pick_approach = pick_pos.copy()
                pick_approach[2] += 30
                self.robot.MovePose(*pick_approach)
                self.robot.MoveLin(*pick_pos)
                self.robot.MovePose(*self.centrifuge.rack_position[i])
                cp = self.robot.SetCheckpoint(50)
                cp.wait()
                self.RackSelection.button_list[i].setChecked(False)
                self.RackSelection.button_list[i]._on_pressed_col_change()
                self.RackSelection.button_list[i].setEnabled(False)
                self.CentStatusDisplay.toggle_led(i)
                QCoreApplication.processEvents()

    def start_centrifuge(self):
        # Reset everything
        for but in self.RackSelection.button_list:
            but.setEnabled(True)
        
        for i in range(6):
            self.RackStatusDisplay.turn_vial_on(i)
            if self.CentStatusDisplay.led_state[i]:
                self.CentStatusDisplay.toggle_led(i)

        self.centrifuge.cent_status = True


    def closeEvent(self, event):
        if not self.robot.IsConnected():
            self.robot.Connect()
        self.robot.DeactivateRobot()
        self.robot.Disconnect()
        super().closeEvent(event)


    ### Test functions ###
    def print_data(self):
        print(self.centrifuge.rack_position[0])