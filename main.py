import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
import PyQt5
from pages import login2

import sys

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = login2.Ui_Form()
ui.setupUi(Form)

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(
        QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(
        QtCore.Qt.AA_UseHighDpiPixmaps, True)


icon = QIcon('.\\ui\\../images/logo.png')
Form.setWindowTitle("TRABALHO LBDI | 2023 | CEFET-MG | " + str(os.getlogin()))
Form.setWindowIcon(icon)
Form.show()
sys.exit(app.exec_())