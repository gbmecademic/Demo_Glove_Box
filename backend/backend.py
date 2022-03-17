from mecademicpy.robot import Robot
from scipy.spatial.transform import Rotation
import numpy as np
import socket


class MainRack():
    def __init__(self, n) -> None:
        self.rack_status = [True]*n       # True if vial is present False if not
        self.rack_position = list()     # List of positions for every rack point
        self.rack_pick_dir = list()
        self.vial_selected = [False]*n

        for i in range(n):
            self.rack_position.append([0,0,0,0,0,0])
            self.rack_pick_dir.append(True)             # True for regular False for front pick
    
    def update_position(self, n, pos):
        self.rack_position[n] = pos

    def update_status(self, n, status):
        self.rack_status[n] = status
    

class Centrifuge():
    def __init__(self, n) -> None:
        self.rack_status = [False]*n        # True if vial is present False if not
        self.rack_position = list()         # List of positions for every rack point
        self.cent_status = True             # True if ready to be loaded
        
        for i in range(n):
            self.rack_position.append([0,0,0,0,0,0])

    def update_position(self, n, pos):
        self.rack_position[n] = pos

    def update_status(self, n, status):
        self.rack_status[n] = status


def projectvector(mov_vect, rot_vect):
    rot_mat = Rotation.from_euler('ZYX', rot_vect)
    rot_mat_num = rot_mat.as_matrix().transpose()
    return np.dot(rot_mat_num, mov_vect)


class Camera():
    def __init__(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._barcode = ""
        self.valid_barcode = False

    def connect(self) -> None:
        self._socket.connect(('192.168.0.102', 5024))

    def _send(self, msg: str) -> None:
        msg_enc = msg+'\r'
        msg_enc = msg_enc.encode('ascii')
        self._socket.sendall(msg_enc)

    def take_picture(self, msg = "Trig") -> None:
        self._send(msg)

    def _recv(self) -> str:
        raw = self._socket.recv(1024)
        decoded = raw.decode('ascii')
        return decoded

    def check_barcode(self) -> None:
        self._barcode = self._recv()
        if len(self._barcode) == 13:
            self.valid_barcode = True









