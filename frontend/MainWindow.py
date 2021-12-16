# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton.setGeometry(QtCore.QRect(150, 540, 151, 91))
        self.LoadButton.setObjectName("LoadButton")
        self.CentStatusDisplay = CentStatus(self.centralwidget)
        self.CentStatusDisplay.setGeometry(QtCore.QRect(150, 100, 400, 400))
        self.CentStatusDisplay.setObjectName("CentStatusDisplay")
        self.labelRackStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelRackStatus.setGeometry(QtCore.QRect(770, 4, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.labelRackStatus.setFont(font)
        self.labelRackStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRackStatus.setObjectName("labelRackStatus")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 424, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(149, 10, 400, 75))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.StatusFrame = QtWidgets.QFrame(self.centralwidget)
        self.StatusFrame.setGeometry(QtCore.QRect(770, 64, 305, 355))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StatusFrame.setFont(font)
        self.StatusFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.StatusFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StatusFrame.setLineWidth(4)
        self.StatusFrame.setObjectName("StatusFrame")
        self.RackStatusDisplay = RackStatus(self.StatusFrame)
        self.RackStatusDisplay.setGeometry(QtCore.QRect(2, 2, 300, 350))
        self.RackStatusDisplay.setObjectName("RackStatusDisplay")
        self.ButtonsFrame = QtWidgets.QFrame(self.centralwidget)
        self.ButtonsFrame.setGeometry(QtCore.QRect(770, 464, 305, 255))
        self.ButtonsFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.ButtonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonsFrame.setLineWidth(4)
        self.ButtonsFrame.setObjectName("ButtonsFrame")
        self.RackSelection = RackButtons(self.ButtonsFrame)
        self.RackSelection.setGeometry(QtCore.QRect(2, 2, 300, 250))
        self.RackSelection.setObjectName("RackSelection")
        self.buttonCentrifuge = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCentrifuge.setGeometry(QtCore.QRect(400, 540, 151, 91))
        self.buttonCentrifuge.setObjectName("buttonCentrifuge")
        self.buttonRobot = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRobot.setGeometry(QtCore.QRect(150, 680, 401, 41))
        self.buttonRobot.setObjectName("buttonRobot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSetup = QtWidgets.QAction(MainWindow)
        self.actionSetup.setObjectName("actionSetup")
        self.menuOptions.addAction(self.actionSetup)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Centrifuge Controls 9000"))
        self.LoadButton.setText(_translate("MainWindow", "Load selected vials"))
        self.labelRackStatus.setText(_translate("MainWindow", "Vial Rack Status"))
        self.label.setText(_translate("MainWindow", "Select which vial to load"))
        self.buttonCentrifuge.setText(_translate("MainWindow", "Start Centrifuge"))
        self.buttonRobot.setText(_translate("MainWindow", "Robot Connection"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionSetup.setText(_translate("MainWindow", "Setup"))
from frontend.customWidgets import CentStatus, RackButtons, RackStatus


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
