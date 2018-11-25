# Copyright 2018 Galen Helfter
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

import PySide2
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QKeySequence

import display.menu_actions
from core.core import Core

class MainWindow(PySide2.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(Core.PROGRAM_NAME)

        # File menu and actions
        self.file_menu = None
        self.file_menu_actions = display.menu_actions.FileMenuActions()

        self.init_menu()

    def init_menu(self):
        """ Initializes the top menus for the main window """
        self.file_menu = PySide2.QtWidgets.QMenu('&File')
        open_name = '{}+O'.format(display.menu_actions.CTRL)
        self.file_menu.addAction('&Open', self.file_menu_actions,
                                 SIGNAL('open_signal()'),
                                 QKeySequence.Open)

        self.menuBar().addMenu(self.file_menu)

def run(argv):
    """ Main display loop of the program, which will be run from
        the main function after initial loading and processing has
        been done """
    app = QApplication()

    # Display the main application window
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
