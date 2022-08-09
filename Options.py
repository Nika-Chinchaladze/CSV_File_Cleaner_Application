from PyQt5 import QtCore, QtGui, QtWidgets
from EmptyRows import Ui_EmptyRows_Page
from WrongData import Ui_WrongData_page
from WrongFormat import Ui_WrongFormat_page
from Describe import Ui_File_watcher
import pandas as pd


class Ui_Options_Page(object):

    def Empty_Rows_Page(self):
        self.window3 = QtWidgets.QMainWindow()
        self.me = Ui_EmptyRows_Page()
        self.me.setupUi(self.window3)
        self.window3.show()
    
    def Wrong_Data_Page(self):
        self.window4 = QtWidgets.QMainWindow()
        self.you = Ui_WrongData_page()
        self.you.setupUi(self.window4)
        self.window4.show()
    
    def Wrong_Format_Page(self):
        self.window5 = QtWidgets.QMainWindow()
        self.we = Ui_WrongFormat_page()
        self.we.setupUi(self.window5)
        self.window5.show()
    
    def File_Watcher_page(self):
        self.window6 = QtWidgets.QMainWindow()
        self.tommas = Ui_File_watcher()
        self.tommas.setupUi(self.window6)
        self.window6.show()

    def setupUi(self, Options_Page):
        Options_Page.setObjectName("Options_Page")
        Options_Page.resize(601, 635)
        self.centralwidget = QtWidgets.QWidget(Options_Page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.clean_label = QtWidgets.QLabel(self.centralwidget)
        self.clean_label.setGeometry(QtCore.QRect(10, 10, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clean_label.setFont(font)
        self.clean_label.setFrameShape(QtWidgets.QFrame.Box)
        self.clean_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.clean_label.setAlignment(QtCore.Qt.AlignCenter)
        self.clean_label.setObjectName("clean_label")
        
        self.empty_button = QtWidgets.QPushButton(self.centralwidget)
        self.empty_button.setGeometry(QtCore.QRect(10, 445, 131, 56))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.empty_button.setFont(font)
        self.empty_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.empty_button.setObjectName("empty_button")

# --------------------------------------- SECRET LABEL --------------------------------------- #
        self.secret_label = QtWidgets.QLabel(self.centralwidget)
        self.secret_label.setGeometry(QtCore.QRect(200, 56, 300, 15))
        self.secret_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.secret_label.setObjectName("secret_label")

# -------------------------------------------------------------------------------------------- #
        
        self.wrong_format_button = QtWidgets.QPushButton(self.centralwidget)
        self.wrong_format_button.setGeometry(QtCore.QRect(160, 445, 131, 56))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wrong_format_button.setFont(font)
        self.wrong_format_button.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.wrong_format_button.setObjectName("wrong_format_button")
        
        self.wrong_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.wrong_data_button.setGeometry(QtCore.QRect(310, 445, 131, 56))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wrong_data_button.setFont(font)
        self.wrong_data_button.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.wrong_data_button.setObjectName("wrong_data_button")
        
        self.dublicate_button = QtWidgets.QPushButton(self.centralwidget)
        self.dublicate_button.setGeometry(QtCore.QRect(460, 445, 131, 56))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dublicate_button.setFont(font)
        self.dublicate_button.setStyleSheet("background-color: rgb(249, 249, 187);")
        self.dublicate_button.setObjectName("dublicate_button")

        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(65, 510, 470, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.open_button.setFont(font)
        self.open_button.setStyleSheet("background-color: rgb(0, 186, 136);")
        self.open_button.setObjectName("open_button")
        
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(141, 560, 319, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("background-color: rgb(212, 212, 159);")
        self.exit_button.setObjectName("exit_button")
        
        self.extra_label = QtWidgets.QLabel(self.centralwidget)
        self.extra_label.setGeometry(QtCore.QRect(10, 70, 581, 280))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.extra_label.setFont(font)
        self.extra_label.setFrameShape(QtWidgets.QFrame.Box)
        self.extra_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.extra_label.setText("")
        self.extra_label.setPixmap(QtGui.QPixmap("hint.jpg"))
        self.extra_label.setScaledContents(True)
        self.extra_label.setAlignment(QtCore.Qt.AlignCenter)
        self.extra_label.setWordWrap(True)
        self.extra_label.setObjectName("extra_label")

        self.done_label = QtWidgets.QLabel(self.centralwidget)
        self.done_label.setGeometry(QtCore.QRect(10, 360, 581, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.done_label.setFont(font)
        self.done_label.setFrameShape(QtWidgets.QFrame.Box)
        self.done_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.done_label.setAlignment(QtCore.Qt.AlignCenter)
        self.done_label.setObjectName("done_label")
        
        Options_Page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Options_Page)
        self.statusbar.setObjectName("statusbar")
        Options_Page.setStatusBar(self.statusbar)

        self.retranslateUi(Options_Page)
        QtCore.QMetaObject.connectSlotsByName(Options_Page)

# ------------------------------------------------ LOGIC -------------------------------------- #
        # Call button methods from here:
        self.empty_button.clicked.connect(self.Empty_Rows_Page)
        self.empty_button.clicked.connect(self.Write_On_Empty)
        self.empty_button.clicked.connect(Options_Page.close)

        self.wrong_format_button.clicked.connect(self.Wrong_Format_Page)
        self.wrong_format_button.clicked.connect(self.Write_On_WrongFormat)
        self.wrong_format_button.clicked.connect(Options_Page.close)

        self.wrong_data_button.clicked.connect(self.Wrong_Data_Page)
        self.wrong_data_button.clicked.connect(self.Write_On_WrongData)
        self.wrong_data_button.clicked.connect(Options_Page.close)

        self.dublicate_button.clicked.connect(self.Remove_Dublicate_Rows)

        self.open_button.clicked.connect(self.File_Watcher_page)
        self.open_button.clicked.connect(self.Write_On_Describe)
        self.open_button.clicked.connect(Options_Page.close)

        self.exit_button.clicked.connect(Options_Page.close)

    
    # define EmptyRows_Page write method:
    def Write_On_Empty(self):
        newname = self.secret_label.text()
        self.me.secret_empty_label_new.setText(f'{newname}')
    
    def Write_On_WrongFormat(self):
        newname = self.secret_label.text()
        self.we.format_secret_label.setText(f'{newname}')
    
    def Write_On_WrongData(self):
        newname = self.secret_label.text()
        self.you.data_secret_label.setText(f'{newname}')
    
    def Write_On_Describe(self):
        newname = self.secret_label.text()
        self.tommas.silent_label.setText(f'{newname}')
    
    # define method for remove dublicate button:
    def Remove_Dublicate_Rows(self):
        file_name = self.secret_label.text()
        df = pd.read_csv(f'{file_name}')
        Boolean_List = list(df.duplicated())
        Quantity = Boolean_List.count(True)

        if Quantity >= 1:
            df.drop_duplicates(inplace=True)
            self.done_label.setText("Dublicated Rows Have Been Removed Permanently!")
            self.done_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        else:
            self.done_label.setText("File Does Not Contain Any Dublicated Rows!")
            self.done_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        
        df.to_csv(f'{file_name}', index=False)
    
    
# ------------------------------------------------- END --------------------------------------- #

    def retranslateUi(self, Options_Page):
        _translate = QtCore.QCoreApplication.translate
        Options_Page.setWindowTitle(_translate("Options_Page", "MainWindow"))
        self.clean_label.setText(_translate("Options_Page", "Let\'s Clean Data - Choose Option You Want!"))
        self.empty_button.setText(_translate("Options_Page", "Clean Empty Cells"))
        self.wrong_format_button.setText(_translate("Options_Page", "Clean Wrong Format"))
        self.wrong_data_button.setText(_translate("Options_Page", "Clean Wrong Data"))
        self.dublicate_button.setText(_translate("Options_Page", "Remove Dublicates"))
        self.exit_button.setText(_translate("Options_Page", "Save Changes and Exit!"))
        self.open_button.setText(_translate("Options_Page", "Open CSV File"))
        self.secret_label.setText(_translate("Options_Page", ""))
        self.done_label.setText(_translate("Options_Page", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Options_Page = QtWidgets.QMainWindow()
    ui = Ui_Options_Page()
    ui.setupUi(Options_Page)
    Options_Page.show()
    sys.exit(app.exec_())
