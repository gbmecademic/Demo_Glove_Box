from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os.path


class CustomButton(QPushButton):
    pass

class StatusImage(QLabel):
    def __init__(self, parent=None):
        super(StatusImage, self).__init__(parent=parent)
        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.im_height = 150
        self.pixmap_on = QPixmap(os.path.join(current_dir, 'images/vial.png'))
        self.pixmap_on = self.pixmap_on.scaledToHeight(self.im_height)
        self.pixmap_off = QPixmap(os.path.join(current_dir, 'images/Vial_grey.png'))
        self.pixmap_off = self.pixmap_off.scaledToHeight(self.im_height)

        self.setPixmap(self.pixmap_on)

    def switch_on(self):
        self.setPixmap(self.pixmap_on)

    def switch_off(self):
        self.setPixmap(self.pixmap_off)


class RackStatus(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super(RackStatus, self).__init__(parent=parent, *args, **kwargs)
        self.grid = QGridLayout()
        self.rack_list = []
        for i in range(6):
            self.rack_list.append(StatusImage())
        positions = [(i, j) for i in range(2) for j in range(3)]

        for i in range(6):
            self.grid.addWidget(self.rack_list[i], *positions[i])
        self.setLayout(self.grid)

    def turn_vial_off(self, pos):
        self.rack_list[pos].switch_off()

    def turn_vial_on(self, pos):
        self.rack_list[pos].switch_on()

class CentStatus(QWidget):
    pass

class RackButtons(QWidget):
    pass


