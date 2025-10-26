import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread
from ui.main import Ui_MainWindow
from app import Trd, info, validation

class MainApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("asset/icons"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.workers = []
        self.threads = []
        self.windows = []

        self.ui.submit.clicked.connect(self.kirim)

        self.input_content = ""
        self.input_auth = ""
        self.input_link = None
        self.input_proxy = None
        self.input_delay = 0

        #automatic validation
        self.ui.inputdelay.textChanged.connect(self.validasi_delay)
        self.ui.inputproxy.textChanged.connect(self.validasi_proxy)

    def take_input(self):
        self.input_content = self.ui.inputcontent.toPlainText().strip()
        self.input_auth = self.ui.inputauthorization.toPlainText().strip()
        self.input_link = self.ui.inputlink.toPlainText().strip()

    def validasi_delay(self):
        self.input_delay = validation.v_delay(self.ui.inputdelay, self)

    def validasi_proxy(self):
        self.input_proxy = validation.v_proxy(self.ui.inputproxy, self)

    def kirim(self):
        self.take_input()
        parent = None

        #validation before send to thread
        if not self.input_delay :
            self.ui.show_custom_warning(parent, "Error", "Delay cannot be empty")
            return
        if not self.input_link :
            self.ui.show_custom_warning(parent, "Error", "Link cannot be empty")
            return
        if not self.input_link.startswith(("http://", "https://")) :
            self.ui.show_custom_warning(parent, "Error", "Link must start with http:// or https://")
            self.ui.inputlink.clear()
            return
    
        if not self.input_link or not self.input_delay:
            return

        #thread
        thread = QThread()
        worker = Trd.Worker(
            auth=self.input_auth,
            proxy=self.input_proxy,
            delays_list=self.input_delay,
            content=self.input_content,
            link=self.input_link
        )
        worker.moveToThread(thread)

        info_window = info.infowindow()
        info_window.show()

        thread.started.connect(worker.run)
        worker.log_signal.connect(info_window.update_log)
        worker.flog_signal.connect(info_window.update_flog)
        worker.cooldown.connect(info_window.start)
        worker.finished.connect(worker.stop)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(info_window.close)
        

        info_window.ui.pushButton.clicked.connect(worker.stop)

        thread.start()

        self.workers.append(worker)
        self.threads.append(thread)
        self.windows.append(info_window)
