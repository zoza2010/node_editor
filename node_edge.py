from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from node_graphics_edge import QDMGraphicsEdgeDirect, QDMGraphicsEdgeBezier

EDGE_TYPE_DIRECT = 1
EDGE_TYPE_BEZIER = 2


class Edge(object):
    def __init__(self, scene, start_socket, end_socket, type=1):

        self.scene = scene
        self.start_socket = start_socket
        self.end_socket = end_socket

        self.grEdge = QDMGraphicsEdgeDirect(self) if type==EDGE_TYPE_DIRECT else QDMGraphicsEdgeBezier(self)

        self.scene.grScene.addItem(self.grEdge)