import sys
from PyQt5 import QtWidgets
from app.main import MainApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())