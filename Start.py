from PyQt5 import QtCore, QtGui, QtWidgets
from Instructions import Ui_Reference_Page


class Ui_Start_Page(object):

    def Instruction_Window(self):
        self.window10 = QtWidgets.QMainWindow()
        self.us = Ui_Reference_Page()
        self.us.setupUi(self.window10)
        self.window10.show()

    def setupUi(self, Start_Page):
        Start_Page.setObjectName("Start_Page")
        Start_Page.resize(601, 620)
        self.centralwidget = QtWidgets.QWidget(Start_Page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(110, 455, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.file_name.setFont(font)
        self.file_name.setText("")
        self.file_name.setAlignment(QtCore.Qt.AlignCenter)
        self.file_name.setObjectName("file_name")
        
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(305, 530, 145, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.next_button.setObjectName("next_button")
        self.next_button.setEnabled(False)

        self.check_button_level_1 = QtWidgets.QPushButton(self.centralwidget)
        self.check_button_level_1.setGeometry(QtCore.QRect(150, 530, 145, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_button_level_1.setFont(font)
        self.check_button_level_1.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.check_button_level_1.setObjectName("submit_button")       
        
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(20, 30, 551, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.welcome_label.setFont(font)
        self.welcome_label.setFrameShape(QtWidgets.QFrame.Box)
        self.welcome_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")

        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(20, 335, 551, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.error_label.setFont(font)
        self.error_label.setFrameShape(QtWidgets.QFrame.Box)
        self.error_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("welcome_label")
        
        self.instruction_label = QtWidgets.QLabel(self.centralwidget)
        self.instruction_label.setGeometry(QtCore.QRect(110, 230, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instruction_label.setFont(font)
        self.instruction_label.setAlignment(QtCore.Qt.AlignCenter)
        self.instruction_label.setWordWrap(True)
        self.instruction_label.setObjectName("instruction_label")
        
        Start_Page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Start_Page)
        self.statusbar.setObjectName("statusbar")
        Start_Page.setStatusBar(self.statusbar)

        self.retranslateUi(Start_Page)
        QtCore.QMetaObject.connectSlotsByName(Start_Page)

# ----------------------------------------- LOGIC ----------------------------------- #
        # call functions: 
        self.next_button.clicked.connect(self.Instruction_Window)
        self.next_button.clicked.connect(self.WriteNext)
        self.next_button.clicked.connect(Start_Page.close)
        self.check_button_level_1.clicked.connect(self.Check_File)
    
    # define next page write method:
    def WriteNext(self):
        screen = self.file_name.text()
        self.us.Real_File_Name_label.setText(f'{screen}')
        self.us.New_File_Name_label.setText(f'New_{screen}')
    
    # define check Function:
    def Check_File(self):
        screen = self.file_name.text()
        if screen[-4:] == '.csv' and screen.count('.') == 1:
            self.next_button.setEnabled(True)
            self.error_label.setText("The Type of file is suitable for this Programm, Now click the Next button!")
            self.error_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        else:
            self.error_label.setText("The Type of file is not suitable for this Programm, It works only on 'CSV' files!")
            self.error_label.setStyleSheet("background-color: rgb(255, 80, 83);")

# ------------------------------------------ END ------------------------------------ #

    def retranslateUi(self, Start_Page):
        _translate = QtCore.QCoreApplication.translate
        Start_Page.setWindowTitle(_translate("Start_Page", "MainWindow"))
        self.next_button.setText(_translate("Start_Page", "Next"))
        self.welcome_label.setText(_translate("Start_Page", "Welcome To CSV File - \"Cleaning Data\" Programm!"))
        self.instruction_label.setText(_translate("Start_Page", "Please Enter File Name, Check it's type and then Press Next Button! ( example: chincho.csv )"))
        self.error_label.setText(_translate("Start_Page", ""))
        self.check_button_level_1.setText(_translate("Start_Page", "Check Type of File"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Start_Page = QtWidgets.QMainWindow()
    ui = Ui_Start_Page()
    ui.setupUi(Start_Page)
    Start_Page.show()
    sys.exit(app.exec_())
