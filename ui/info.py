# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("""
            QWidget {
                background-color: #202020;
            }
            QLabel {
                font-family: "Press Start 2P", monospace;
                font-size: 9pt;
                color: #00FF88;
            }
            QPushButton {
                background-color: #00FF88;
                color: #000000;
                font-family: "Press Start 2P", monospace;
                font-size: 8pt;
                border: 2px solid #00FF88;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #00CC66;
            }
            QPushButton:pressed {
                background-color: #009955;
            }
        """)

        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setGeometry(QtCore.QRect(50, 30, 400, 40))
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setStyleSheet("""
            QLabel {
                font-size: 12pt;
                color: #00FF88;
            }
        """)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 120, 400, 80))
        self.label.setObjectName("Success")
        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 400, 80))
        self.label_2.setObjectName("Failed")
        self.label_2.setWordWrap(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 400, 80))
        self.label_3.setObjectName("Timer")
        self.label_3.setWordWrap(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

     
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 400, 150, 45))
        self.pushButton.setObjectName("stopbutton")
        self.pushButton.setText("STOP")
        self.pushButton.clicked.connect(Form.close)

        self.retranslateUi(Form)


        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Info Window"))
        self.titleLabel.setText(_translate("Form", "STATUS SENDER"))
        self.label.setText(_translate("Form", "Success: 0"))
        self.label_2.setText(_translate("Form", "Failed: 0"))
