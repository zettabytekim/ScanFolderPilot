#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    특정 데렉토리 내 파일 리스트를 엑셀로 저장
    Pandas
Author: Zetta Kim
Last edited: 2019.01.26
"""
import sys, mainUI_Win
import os.path
import pandas as pd
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QPushButton, QApplication

class MainDialog(QDialog, mainUI_Win.Ui_MainDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.scan_pushButton.clicked.connect(self.scan_buttonClicked)
        self.about_pushButton.clicked.connect(self.about_buttonClicked)
        self.quit_pushButton.clicked.connect(QApplication.instance().quit)

    def scan_buttonClicked(self):
        dir_name = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print("on" + dir_name)
        df = pd.DataFrame(columns=('no', 'directory', 'd_link', 'file', 'f_link'))

        i = 1
        for path, dirs, files in os.walk(dir_name):
            if files:
                for filename in files:
                    fullname = os.path.join(path, filename)
                    df2 = pd.DataFrame(
                        data=[
                            [i, path, f'=HYPERLINK("{path}", "DirView")',
                            filename, f'=HYPERLINK("file:///{fullname}", "FileView")']
                            ], columns=('no', 'directory', 'd_link', 'file', 'f_link'))
                    df = df.append(df2, ignore_index=True)
                    i += 1

        df.to_excel('folder_scan.xlsx', sheet_name='Scan Result', index=False, header=True)
        
        if dir_name != '':
            # os.system("open " + 'folder_scan.xlsx') # macOS
            os.system("start " + 'folder_scan.xlsx') # Windows
    
    def about_buttonClicked(self):
        reply = QMessageBox.about(self, 'About', '   eXScan \n       v0.5\n\n Jan, 2019\n Zetta Kim')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                "Are you sure to quit?", QMessageBox.Yes |
                 QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainDialog()
    ex.show()
    sys.exit(app.exec_())
