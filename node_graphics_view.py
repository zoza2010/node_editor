from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDMGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(QDMGraphicsView, self).__init__(parent)
        self.grScene = scene

        self.initUI()

        self.setScene(self.grScene)

    def initUI(self):
        # fix antialiasing
        self.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
