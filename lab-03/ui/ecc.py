# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 381)
        MainWindow.setStyleSheet("background-color: rgb(176, 207, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 0, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(410, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_gen_keys.setFont(font)
        self.btn_gen_keys.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        self.txt_info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(140, 40, 451, 121))
        self.txt_info.setStyleSheet("background-color: rgb(215, 243, 255)")
        self.txt_info.setObjectName("txt_info")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(140, 290, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_sign.setFont(font)
        self.btn_sign.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(500, 290, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_verify.setFont(font)
        self.btn_verify.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_verify.setObjectName("btn_verify")
        self.txt_sign = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(140, 180, 451, 91))
        self.txt_sign.setStyleSheet("background-color: rgb(215, 243, 255)")
        self.txt_sign.setObjectName("txt_sign")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ECC CIPHER"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.label_3.setText(_translate("MainWindow", "Information:"))
        self.label_5.setText(_translate("MainWindow", "Signature:"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
