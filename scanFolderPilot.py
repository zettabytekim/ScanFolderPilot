#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    특정 데렉토리 내 파일 리스트를 엑셀로 저장
    Pandas
Author: Zetta Kim
Last edited: 2019.01.25
"""
import sys
import os.path
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QWidget, QPushButton, QApplication

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        actbtn = QPushButton('폴더 선택', self)
        actbtn.clicked.connect(self.buttonClicked)
        actbtn.resize(actbtn.sizeHint())
        actbtn.move(70, 40)

        qbtn = QPushButton('종료', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(70, 80)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Scanning Folder')
        self.show()

    def buttonClicked(self):
        dir_name = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        # folder = os.getcwd()
        # folder = '/test'
        # print('Scan folder : %s' % folder)
        # print('Directory Name : %s' % dir_name)

        df = pd.DataFrame(columns=('no', 'directory', 'd_link', 'file', 'f_link'))

        i = 1
        for path, dirs, files in os.walk(dir_name):
            if files:
                for filename in files:
                    fullname = os.path.join(path, filename)
                    df2 = pd.DataFrame(
                        data=[
                            [i, path, f'=HYPERLINK("{path}", "DirView")',
                            filename, f'=HYPERLINK("{fullname}", "FileView")']
                        ], columns=('no', 'directory', 'd_link', 'file', 'f_link'))
                    df = df.append(df2, ignore_index=True)
                    i += 1

        df.to_excel('folder_scan.xlsx', sheet_name='Scan Result', index=False, header=True)
        os.system("open " + 'folder_scan.xlsx') # macOS
        # os.system("start " + filename) # Windows

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())
