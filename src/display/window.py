import sys

import PySide2
from PySide2.QtWidgets import QApplication, QLabel

class MainWindow(PySide2.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Clang Format Diff Tool')

def run(argv):
    """ Main display loop of the program, which will be run from
        the main function after initial loading and processing has
        been done """
    app = QApplication()

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
