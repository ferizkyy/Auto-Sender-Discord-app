# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 870)
        MainWindow.setMinimumSize(QtCore.QSize(650, 870))
        MainWindow.setMaximumSize(QtCore.QSize(650, 870))
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #202020;
            }
            QLabel {
                font-family: "Press Start 2P", monospace;
                font-size: 8pt;
                color: #00FF88;
            }
            QPlainTextEdit {
                background-color: #111111;
                border: 2px solid #00FF88;
                border-radius: 6px;
                padding: 10px;
                font-size: 13pt;
                font-family: "VT323", monospace;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: #00FF88;
                color: #000000;
                font-family: "Press Start 2P", monospace;
                font-size: 9pt;
                border: 2px solid #00FF88;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #00CC66;
            }
            QPushButton:pressed {
                background-color: #009955;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        input_height = 80
        label_height = 30
        spacing = 35
        top = 30

        
        def add_label_input(label_name):
            nonlocal top
            lbl = QtWidgets.QLabel(self.centralwidget)
            lbl.setGeometry(QtCore.QRect(30, top, 580, label_height))
            lbl.setWordWrap(True)
            lbl.setText(label_name)

            top_input = top + label_height + 5
            txt = QtWidgets.QPlainTextEdit(self.centralwidget)
            txt.setGeometry(QtCore.QRect(30, top_input, 580, input_height))

            top = top_input + input_height + spacing
            return lbl, txt

        self.label_2, self.inputdelay = add_label_input("Delay input(Separate with space)")
        self.label, self.inputcontent = add_label_input("Content")
        self.label_3, self.inputproxy = add_label_input("Proxy (Optional)")
        self.label_4, self.inputauthorization = add_label_input("Authorization")
        self.label_5, self.inputlink = add_label_input("Link")

        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(265, top, 120, 45))
        self.submit.setObjectName("submit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @staticmethod
    def show_custom_warning(parent, title, message):
        msg_box = QtWidgets.QMessageBox(parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

        msg_box.setStyleSheet("""
        QMessageBox {
            background-color: #202020;
            border: 2px solid #00FF88;
        }
        QLabel {
            color: #00FF88;
            font-family: "Press Start 2P";
            font-size: 10pt;
        }
        QPushButton {
            background-color: #00FF88;
            color: #000000;
            font-family: "Press Start 2P";
            font-size: 8pt;
            border: 2px solid #00FF88;
            border-radius: 4px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #00CC66;
        }
        QPushButton:pressed {
            background-color: #009955;
        }
        """)
        msg_box.exec_()

    def retranslateUi(self, MainWindow):
        _ = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_("MainWindow", "Auto Sender"))
        self.submit.setText(_("MainWindow", "OK"))
