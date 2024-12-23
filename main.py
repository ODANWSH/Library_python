from PyQt5 import QtWidgets, QtGui
import sys
from src.views.general.login import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())