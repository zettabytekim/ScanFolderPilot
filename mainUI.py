# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.setWindowModality(QtCore.Qt.WindowModal)
        MainDialog.setFixedSize(240, 242)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainDialog.sizePolicy().hasHeightForWidth())
        MainDialog.setSizePolicy(sizePolicy)
        MainDialog.setModal(True)
        self.scan_pushButton = QtWidgets.QPushButton(MainDialog)
        self.scan_pushButton.setGeometry(QtCore.QRect(8, 60, 221, 61))
        self.scan_pushButton.setAutoDefault(False)
        self.scan_pushButton.setObjectName("scan_pushButton")
        self.label = QtWidgets.QLabel(MainDialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.about_pushButton = QtWidgets.QPushButton(MainDialog)
        self.about_pushButton.setGeometry(QtCore.QRect(8, 117, 221, 61))
        self.about_pushButton.setAutoDefault(False)
        self.about_pushButton.setObjectName("about_pushButton")
        self.quit_pushButton = QtWidgets.QPushButton(MainDialog)
        self.quit_pushButton.setGeometry(QtCore.QRect(9, 173, 221, 61))
        self.quit_pushButton.setAutoDefault(False)
        self.quit_pushButton.setObjectName("quit_pushButton")

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "eXCan v0.1"))
        self.scan_pushButton.setText(_translate("MainDialog", "Scan Folder"))
        self.label.setText(_translate("MainDialog", "Scan Folder to Excel"))
        self.about_pushButton.setText(_translate("MainDialog", "About"))
        self.quit_pushButton.setText(_translate("MainDialog", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainDialog = QtWidgets.QDialog()
    ui = Ui_MainDialog()
    ui.setupUi(MainDialog)
    MainDialog.show()
    sys.exit(app.exec_())

