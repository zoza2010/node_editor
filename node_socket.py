from node_graphics_socket import QDMGraphicsSocket
import logging

logger = logging.getLogger(__name__)

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4

class Socket(object):
    def __init__(self, node, index=0, position=LEFT_TOP, socket_type=1):

        self.node = node
        self.index = index
        self.position = position
        self.socket_type = socket_type

        logger.debug(f"Socket -- creating  with {self.index} {self.position} for node {self.node}")


        self.grSocket = QDMGraphicsSocket(self.node.grNode, self.socket_type)

        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

        self.edge = None

    def getSocketPosition(self):
        return self.node.getSocketPosition(self.index, self.position)

    def setConnectedEdge(self, edge=None):
        self.edge = edge

    def hasEdge(self):
        return self.edge is not None