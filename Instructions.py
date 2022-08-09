from PyQt5 import QtCore, QtGui, QtWidgets
from Options import Ui_Options_Page
import pandas as pd

class Ui_Reference_Page(object):

    def Previous_Window(self):
        from Start import Ui_Start_Page

        self.window_pac = QtWidgets.QMainWindow()
        self.big = Ui_Start_Page()
        self.big.setupUi(self.window_pac)
        self.window_pac.show()

    def Options_Page(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Options_Page()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, Reference_Page):
        Reference_Page.setObjectName("Reference_Page")
        Reference_Page.resize(820, 600)
        self.centralwidget = QtWidgets.QWidget(Reference_Page)
        self.centralwidget.setObjectName("centralwidget")

        self.back_page_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_page_button.setGeometry(QtCore.QRect(25, 520, 130, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_page_button.setFont(font)
        self.back_page_button.setStyleSheet("background-color: rgb(216, 216, 162);")
        self.back_page_button.setObjectName("back_page_button")

        self.last_check_button = QtWidgets.QPushButton(self.centralwidget)
        self.last_check_button.setGeometry(QtCore.QRect(175, 520, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_check_button.setFont(font)
        self.last_check_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.last_check_button.setObjectName("last_check_button")
        
        self.begin_button = QtWidgets.QPushButton(self.centralwidget)
        self.begin_button.setGeometry(QtCore.QRect(495, 520, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.begin_button.setFont(font)
        self.begin_button.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.begin_button.setObjectName("begin_button")
        self.begin_button.setEnabled(False)
        
        self.ability_label = QtWidgets.QLabel(self.centralwidget)
        self.ability_label.setGeometry(QtCore.QRect(10, 10, 800, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ability_label.setFont(font)
        self.ability_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ability_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ability_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ability_label.setObjectName("ability_label")
        
        self.boom_label = QtWidgets.QLabel(self.centralwidget)
        self.boom_label.setGeometry(QtCore.QRect(10, 70, 800, 363))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boom_label.setFont(font)
        self.boom_label.setFrameShape(QtWidgets.QFrame.Box)
        self.boom_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.boom_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.boom_label.setWordWrap(True)
        self.boom_label.setObjectName("boom_label")
        self.boom_label.setText("""1) CSV file Cleaner Programm can do following operations: 
        a) Display ColumnNames with their data type
        b) Work with Null values (remove or replace them with new values) 
        c) Change data type of Columns 
        d) Remove or Replace wrong data in each Column
        e) Remove Dublicate rows from the CSV file
        \n2) In Clean Empty Cell section, User can:
        a) Remove All Null values from the file
        b) Replace All Nulls with new Value in the whole file or in each Column (it is optional)
        c) Replace All Nulls with Mean, Median or Mode. This function is available only for Numeric Columns (int, float)
        \n3) In Clean Wrong Format section User can:
        a) Convert Column's data into str, int, float, boolean or datetime format
        \n4) In Clean Wrong Data section User can:
        a) Remove rows, that contain WRONG - Dirty data, from the CSV file
        b) Replace WRONG Values with another - New values in each column
        \n5) In Remove Dublicates section - User can remove Duplicate Rows permanently
        \n6) User can open CSV file and see changes made by him/her""")
        
        self.check_exist_label = QtWidgets.QLabel(self.centralwidget)
        self.check_exist_label.setGeometry(QtCore.QRect(10, 443, 800, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_exist_label.setFont(font)
        self.check_exist_label.setFrameShape(QtWidgets.QFrame.Box)
        self.check_exist_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.check_exist_label.setAlignment(QtCore.Qt.AlignCenter)
        self.check_exist_label.setWordWrap(True)
        self.check_exist_label.setObjectName("boom_label")
        
# ----------------------------------------- secret labels ----------------------------------------- #
        self.Real_File_Name_label = QtWidgets.QLabel(self.centralwidget)
        self.Real_File_Name_label.setGeometry(QtCore.QRect(10, 492, 381, 20))
        self.Real_File_Name_label.setText("")
        self.Real_File_Name_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.Real_File_Name_label.setWordWrap(True)
        self.Real_File_Name_label.setObjectName("Real_File_Name_label")
        
        self.New_File_Name_label = QtWidgets.QLabel(self.centralwidget)
        self.New_File_Name_label.setGeometry(QtCore.QRect(490, 492, 381, 20))
        self.New_File_Name_label.setText("")
        self.New_File_Name_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.New_File_Name_label.setWordWrap(True)
        self.New_File_Name_label.setObjectName("New_File_Name_label")
# ------------------------------------------------------------------------------------------------ #
        
        Reference_Page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Reference_Page)
        self.statusbar.setObjectName("statusbar")
        Reference_Page.setStatusBar(self.statusbar)

        self.retranslateUi(Reference_Page)
        QtCore.QMetaObject.connectSlotsByName(Reference_Page)

# ----------------------------------------- logic ------------------------------------------------ #
        # call methods:
        self.back_page_button.clicked.connect(self.Previous_Window)
        self.back_page_button.clicked.connect(Reference_Page.close)

        self.begin_button.clicked.connect(self.Options_Page)
        self.begin_button.clicked.connect(self.Write_On_Options)
        self.begin_button.clicked.connect(Reference_Page.close)
        
        self.last_check_button.clicked.connect(self.Create_New_File)
    
    # define methods:
    def Write_On_Options(self):
        screen = self.New_File_Name_label.text()
        self.ui.secret_label.setText(f'{screen}')
    
    # create copy:
    def Create_New_File(self):
        realfile = self.Real_File_Name_label.text()
        newfile = self.New_File_Name_label.text()
        
        try:
            self.file = pd.read_csv(f'{realfile}')
            self.file.to_csv(f'{newfile}', index=False)
            self.check_exist_label.setText("File exists, Now you can press the button and Begin Cleaning of Dirty Data!")
            self.check_exist_label.setStyleSheet("background-color: rgb(170, 255, 127);")
            self.begin_button.setEnabled(True)
            self.last_check_button.setEnabled(False)
        except FileNotFoundError:
            self.check_exist_label.setText("File does not exist, please Go back to previous page and Enter valid file name!")
            self.check_exist_label.setStyleSheet("background-color: rgb(255, 80, 83);")

# ------------------------------------------ end ------------------------------------------------- #

    def retranslateUi(self, Reference_Page):
        _translate = QtCore.QCoreApplication.translate
        Reference_Page.setWindowTitle(_translate("Reference_Page", "MainWindow"))
        self.begin_button.setText(_translate("Reference_Page", "Begin Cleaning Of Dirty Data"))
        self.ability_label.setText(_translate("Reference_Page", "Abilities Of Programm!"))
        self.check_exist_label.setText(_translate("Reference_Page", ""))
        self.back_page_button.setText(_translate("Reference_Page", "Previous Page"))
        self.last_check_button.setText(_translate("Reference_Page", "Check File Existense"))
        self.Real_File_Name_label.setText(_translate("Reference_Page", ""))
        self.New_File_Name_label.setText(_translate("Reference_Page", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reference_Page = QtWidgets.QMainWindow()
    ui = Ui_Reference_Page()
    ui.setupUi(Reference_Page)
    Reference_Page.show()
    sys.exit(app.exec_())
