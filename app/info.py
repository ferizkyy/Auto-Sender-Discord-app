from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer
from ui.info import Ui_Form

class infowindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("asset/icons"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.label.setText("Processing...")
        self.ui.label_2.setText("No error")

        self.timer = QTimer(self)
        
        

        self.ui.pushButton.clicked.connect(self.stop_timer)

    #success log 
    def update_log(self, message, count, delay):
        self.ui.label.setText(f"{message}    Success: {count}\nDelay: {delay}")
    #fail log
    def update_flog(self, message, count, delays):
        self.ui.label_2.setText(f"{message}     Failed: {count}\nDelay: {delays}s")

    def start(self, times):

        self.countdown = times
        self.ui.label_3.setText(f"{str(self.countdown)} Seconds for next massage")

        self.timer.stop()

        try :
            self.timer.timeout.disconnect(self.update)

        except TypeError:
            pass


        self.timer.timeout.connect(self.update)
        self.timer.start(1000)


    def update(self):
        self.countdown -= 1
        self.ui.label_3.setText(f"{str(self.countdown)} Seconds for next massage")
        
    def stop_timer(self):
        self.timer.stop()