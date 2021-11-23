from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget

class RackStatus(QWidget):
    
    def __init__(self, *args, **kwargs):
        super(RackStatus, self).__init__(*args, **kwargs)
        grid = QGridLayout()
        rack_list = []
        for i in range(6):
            rack_list.append(QPushButton(f'Rack {i}'))
        

class CentStatus(QWidget):
    pass

class RackButtons(QWidget):
    pass


