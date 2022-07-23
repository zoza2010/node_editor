import sys
from PyQt5.QtWidgets import *
from node_editor_wnd import NodeEditorWnd
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    wnd = NodeEditorWnd()
    sys.exit(app.exec_())
