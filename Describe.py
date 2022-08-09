from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import pandas as pd


class Ui_File_watcher(object):

    def BackWard_to_Options_page(self):
        from Options import Ui_Options_Page

        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Options_Page()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, File_watcher):
        File_watcher.setObjectName("File_watcher")
        File_watcher.resize(601, 635)
        self.centralwidget = QtWidgets.QWidget(File_watcher)
        self.centralwidget.setObjectName("centralwidget")
        
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(10, 10, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.open_button.setFont(font)
        self.open_button.setObjectName("open_button")
        self.open_button.setStyleSheet("background-color: rgb(0, 188, 138);")
                
        self.Describe_button = QtWidgets.QPushButton(self.centralwidget)
        self.Describe_button.setGeometry(QtCore.QRect(120, 10, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Describe_button.setFont(font)
        self.Describe_button.setObjectName("Describe_button")
        self.Describe_button.setEnabled(False)
        self.Describe_button.setStyleSheet("background-color: rgb(255, 255, 127);")

        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(490, 10, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finish_button.setFont(font)
        self.finish_button.setObjectName("finish_button")
        self.finish_button.setStyleSheet("background-color: rgb(255, 56, 59);")
        
        self.doom_label = QtWidgets.QLabel(self.centralwidget)
        self.doom_label.setGeometry(QtCore.QRect(230, 10, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.doom_label.setFont(font)
        self.doom_label.setFrameShape(QtWidgets.QFrame.Box)
        self.doom_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.doom_label.setText("")
        self.doom_label.setWordWrap(True)
        self.doom_label.setAlignment(QtCore.Qt.AlignCenter)
        self.doom_label.setObjectName("doom_label")

# --------------------------------------- SECRET LABEL --------------------------------------- #
        self.silent_label = QtWidgets.QLabel(self.centralwidget)
        self.silent_label.setGeometry(QtCore.QRect(20, 51, 300, 15))
        self.silent_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.silent_label.setObjectName("secret_label")
# -------------------------------------------------------------------------------------------- #

        self.Table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.Table_widget.setGeometry(QtCore.QRect(10, 70, 580, 530))
        self.Table_widget.setObjectName("Table_widget")
        self.Table_widget.setColumnCount(0)
        self.Table_widget.setRowCount(0)
        
        File_watcher.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(File_watcher)
        self.statusbar.setObjectName("statusbar")
        File_watcher.setStatusBar(self.statusbar)

        self.retranslateUi(File_watcher)
        QtCore.QMetaObject.connectSlotsByName(File_watcher)

# ----------------------------------------------- logic --------------------------------- #
        self.open_button.clicked.connect(self.OpenFile)
        self.Describe_button.clicked.connect(self.DescribeFile)

        self.finish_button.clicked.connect(self.BackWard_to_Options_page)
        self.finish_button.clicked.connect(self.Write_Back_on_Options_page)
        self.finish_button.clicked.connect(File_watcher.close)
    
    # define method to write file name back on Options page:
    def Write_Back_on_Options_page(self):
        file_name = self.silent_label.text()
        self.ui.secret_label.setText(f"{file_name}")
    
    # define method to open csv file:
    def OpenFile(self):
        file_name = self.silent_label.text()

        self.file_data = pd.read_csv(f"{file_name}")
        self.doom_label.setText(f"{file_name} is ready, press Show Input!")
        self.doom_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.open_button.setEnabled(False)
        self.Describe_button.setEnabled(True)
    
    # define method to show csv file:
    def DescribeFile(self):
        RowNumber = len(self.file_data.index)
        ColumnNumber = len(self.file_data.columns)

        self.Table_widget.setColumnCount(ColumnNumber)
        self.Table_widget.setRowCount(RowNumber)
        self.Table_widget.setHorizontalHeaderLabels(self.file_data.columns)

        for rows in range(RowNumber):
            for columns in range(ColumnNumber):
                self.Table_widget.setItem(rows, columns, QTableWidgetItem(str(self.file_data.iat[rows, columns])))
        
        self.Table_widget.resizeColumnsToContents()
        self.Table_widget.resizeRowsToContents()

# ------------------------------------------------ end --------------------------------- #

    def retranslateUi(self, File_watcher):
        _translate = QtCore.QCoreApplication.translate
        File_watcher.setWindowTitle(_translate("File_watcher", "MainWindow"))
        self.open_button.setText(_translate("File_watcher", "Connect File"))
        self.Describe_button.setText(_translate("File_watcher", "Show Input"))
        self.finish_button.setText(_translate("File_watcher", "End"))
        self.doom_label.setText(_translate("File_watcher", ""))
        self.silent_label.setText(_translate("File_watcher", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File_watcher = QtWidgets.QMainWindow()
    ui = Ui_File_watcher()
    ui.setupUi(File_watcher)
    File_watcher.show()
    sys.exit(app.exec_())
