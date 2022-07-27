from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd

class Ui_WrongFormat_page(object):

    def ComeBack(self):
        from Options import Ui_Options_Page

        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Options_Page()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, WrongFormat_page):
        WrongFormat_page.setObjectName("WrongFormat_page")
        WrongFormat_page.resize(882, 581)
        self.centralwidget = QtWidgets.QWidget(WrongFormat_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.wrongFormat_label = QtWidgets.QLabel(self.centralwidget)
        self.wrongFormat_label.setGeometry(QtCore.QRect(10, 10, 861, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wrongFormat_label.setFont(font)
        self.wrongFormat_label.setFrameShape(QtWidgets.QFrame.Box)
        self.wrongFormat_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wrongFormat_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wrongFormat_label.setObjectName("wrongFormat_label")
# ------------------------------------------ secret label -------------------------------------- #
        self.format_secret_label = QtWidgets.QLabel(self.centralwidget)
        self.format_secret_label.setGeometry(QtCore.QRect(760, 10, 100, 51))
        self.format_secret_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.format_secret_label.setObjectName("format_secret_label")
# ---------------------------------------------------------------------------------------------- #
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(100, 510, 681, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.return_button.setFont(font)
        self.return_button.setStyleSheet("background-color: rgb(212, 212, 159);")
        self.return_button.setObjectName("return_button")

        self.informative_label = QtWidgets.QLabel(self.centralwidget)
        self.informative_label.setGeometry(QtCore.QRect(10, 70, 861, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.informative_label.setFont(font)
        self.informative_label.setFrameShape(QtWidgets.QFrame.Box)
        self.informative_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.informative_label.setText("")
        self.informative_label.setAlignment(QtCore.Qt.AlignCenter)
        self.informative_label.setWordWrap(True)
        self.informative_label.setObjectName("informative_label")
        
        self.showCol_button = QtWidgets.QPushButton(self.centralwidget)
        self.showCol_button.setGeometry(QtCore.QRect(10, 190, 91, 51))
        self.showCol_button.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.showCol_button.setObjectName("showCol_button")
        
        self.csv_column_label = QtWidgets.QLabel(self.centralwidget)
        self.csv_column_label.setGeometry(QtCore.QRect(110, 190, 761, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.csv_column_label.setFont(font)
        self.csv_column_label.setFrameShape(QtWidgets.QFrame.Box)
        self.csv_column_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.csv_column_label.setText("")
        self.csv_column_label.setWordWrap(True)
        self.csv_column_label.setObjectName("csv_column_label")
        
        self.H_line_1 = QtWidgets.QFrame(self.centralwidget)
        self.H_line_1.setGeometry(QtCore.QRect(10, 250, 861, 21))
        self.H_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.H_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.H_line_1.setObjectName("H_line_1")
        
        self.H_line_2 = QtWidgets.QFrame(self.centralwidget)
        self.H_line_2.setGeometry(QtCore.QRect(10, 370, 861, 21))
        self.H_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.H_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.H_line_2.setObjectName("H_line_2")
        
        self.H_line_3 = QtWidgets.QFrame(self.centralwidget)
        self.H_line_3.setGeometry(QtCore.QRect(10, 480, 861, 21))
        self.H_line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.H_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.H_line_3.setObjectName("H_line_3")
        
        self.write_column_label = QtWidgets.QLabel(self.centralwidget)
        self.write_column_label.setGeometry(QtCore.QRect(16, 270, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.write_column_label.setFont(font)
        self.write_column_label.setAlignment(QtCore.Qt.AlignCenter)
        self.write_column_label.setObjectName("write_column_label")
        
        self.line_edit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_1.setGeometry(QtCore.QRect(30, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_edit_1.setFont(font)
        self.line_edit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_1.setObjectName("line_edit_1")
        
        self.line_edit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_2.setGeometry(QtCore.QRect(30, 420, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_edit_2.setFont(font)
        self.line_edit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_2.setObjectName("line_edit_2")
        
        self.V_line_1 = QtWidgets.QFrame(self.centralwidget)
        self.V_line_1.setGeometry(QtCore.QRect(230, 260, 21, 231))
        self.V_line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.V_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V_line_1.setObjectName("V_line_1")
        
        self.V_line_2 = QtWidgets.QFrame(self.centralwidget)
        self.V_line_2.setGeometry(QtCore.QRect(630, 260, 21, 231))
        self.V_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.V_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V_line_2.setObjectName("V_line_2")
        
        self.enter_datatype_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_datatype_label.setGeometry(QtCore.QRect(300, 270, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.enter_datatype_label.setFont(font)
        self.enter_datatype_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_datatype_label.setObjectName("enter_datatype_label")
        
        self.data_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.data_combo_box.setGeometry(QtCore.QRect(328, 310, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_combo_box.setFont(font)
        self.data_combo_box.setObjectName("data_combo_box")
        self.data_combo_box.addItem("")
        self.data_combo_box.addItem("")
        self.data_combo_box.addItem("")
        self.data_combo_box.addItem("")

        self.DateTime_label = QtWidgets.QLabel(self.centralwidget)
        self.DateTime_label.setGeometry(QtCore.QRect(330, 420, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateTime_label.setFont(font)
        self.DateTime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.DateTime_label.setFrameShape(QtWidgets.QFrame.Box)
        self.DateTime_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DateTime_label.setText("")
        self.DateTime_label.setObjectName("DateTime_label")
        
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(670, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convert_button.setFont(font)
        self.convert_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.convert_button.setObjectName("convert_button")
        
        self.convert_date_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_date_button.setGeometry(QtCore.QRect(670, 420, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convert_date_button.setFont(font)
        self.convert_date_button.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.convert_date_button.setObjectName("convert_date_button")
        
        self.transform_label = QtWidgets.QLabel(self.centralwidget)
        self.transform_label.setGeometry(QtCore.QRect(650, 270, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.transform_label.setFont(font)
        self.transform_label.setAlignment(QtCore.Qt.AlignCenter)
        self.transform_label.setObjectName("transform_label")
        
        WrongFormat_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WrongFormat_page)
        self.statusbar.setObjectName("statusbar")
        WrongFormat_page.setStatusBar(self.statusbar)

        self.retranslateUi(WrongFormat_page)
        QtCore.QMetaObject.connectSlotsByName(WrongFormat_page)

# --------------------------------------- LOGIC ------------------------------------- #
        # call methods:
        self.return_button.clicked.connect(self.ComeBack)
        self.return_button.clicked.connect(self.Write_On_Options)
        self.return_button.clicked.connect(WrongFormat_page.close)
        self.showCol_button.clicked.connect(self.Show_File_Columns)
        self.convert_button.clicked.connect(self.Convert_AsType)
        self.convert_date_button.clicked.connect(self.Convert_Datetime)

    
    # define write back method for return button:
    def Write_On_Options(self):
        file_name = self.format_secret_label.text()
        self.ui.secret_label.setText(f'{file_name}')
        
    # define method for showCol button:
    def Show_File_Columns(self):
        name = self.format_secret_label.text()
        
        df = pd.read_csv(f'{name}')
        Column_List = list(df.columns)
        Dictionary_List = {}
        for i in Column_List:
            Dictionary_List[i] = df[f'{i}'].dtype
        self.csv_column_label.setText(f'{Dictionary_List}')

    
    # define method for convert button:
    def Convert_AsType(self):
        file_name = self.format_secret_label.text()
        Column_Name = self.line_edit_1.text()
        Wanted_Data_Type = self.data_combo_box.currentText()

        df = pd.read_csv(f'{file_name}')

        Column_List = list(df.columns)
        if len(Column_Name) > 0 and Column_Name in Column_List:
            try:
                if Wanted_Data_Type == 'int':
                    df[f'{Column_Name}'].fillna(0, inplace=True)
                    df[f'{Column_Name}'] = df[f'{Column_Name}'].astype(f'{Wanted_Data_Type}')
                else:
                    df[f'{Column_Name}'] = df[f'{Column_Name}'].astype(f'{Wanted_Data_Type}')

                df.to_csv(f'{file_name}', index=False)
                self.informative_label.setText(f"{Column_Name} Has Been Converted Into {Wanted_Data_Type} Data Type! Now {Column_Name}'s Data_Type is: {df[f'{Column_Name}'].dtype}")
                self.informative_label.setStyleSheet("background-color: rgb(170, 255, 127);")
            except:
                self.informative_label.setText(f"{Column_Name} column can not be converted into {Wanted_Data_Type} data type!")
                self.informative_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(Column_Name) == 0:
            self.informative_label.setText("Column Name field is EMPTY, fill it!")
            self.informative_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(Column_Name) > 0 and Column_Name not in Column_List:
            self.informative_label.setText("Column Name is WRONG, check 'Show Columns' button!")
            self.informative_label.setStyleSheet("background-color: rgb(255, 80, 83);")
    
    # define method to convert column into DateTime data type:
    def Convert_Datetime(self):
        file_name = self.format_secret_label.text()
        Column_Name = self.line_edit_2.text()

        df = pd.read_csv(f'{file_name}')

        Column_List = list(df.columns)
        if len(Column_Name) > 0 and Column_Name in Column_List:
            try:
                df[f'{Column_Name}'] = pd.to_datetime(df[f'{Column_Name}'])
                df.to_csv(f'{file_name}', index=False)
                self.informative_label.setText(f"{Column_Name}'s Data type has been converted into Datetime Format!")
                self.informative_label.setStyleSheet("background-color: rgb(170, 255, 127);")
            except ValueError:
                Problem_Column = pd.Series(df[f'{Column_Name}'])
                Length = len(Problem_Column)
                for i in range(Length):
                    try:
                        Problem_Column[i] = pd.to_datetime(Problem_Column[i])
                    except ValueError:
                        Problem_Column[i] = ''
                df[f'{Column_Name}'] = Problem_Column
                df.to_csv(f'{file_name}', index=False)
                self.informative_label.setText(f"{Column_Name}'s Data type has been converted into Datetime Format, Successfully!")
                self.informative_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        elif len(Column_Name) == 0:
            self.informative_label.setText("Column Name field is EMPTY, fill it!")
            self.informative_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(Column_Name) > 0 and Column_Name not in Column_List:
            self.informative_label.setText("Column Name is WRONG, check 'Show Columns' button!")
            self.informative_label.setStyleSheet("background-color: rgb(255, 80, 83);")  
           


# ---------------------------------------- END -------------------------------------- #

    def retranslateUi(self, WrongFormat_page):
        _translate = QtCore.QCoreApplication.translate
        WrongFormat_page.setWindowTitle(_translate("WrongFormat_page", "MainWindow"))
        self.wrongFormat_label.setText(_translate("WrongFormat_page", "Let\'s Clean Wrong Format Data!"))
        self.return_button.setText(_translate("WrongFormat_page", "Save Changes and Go Back To MainWindow!"))
        self.showCol_button.setText(_translate("WrongFormat_page", "Show Columns"))
        self.write_column_label.setText(_translate("WrongFormat_page", "Enter Column Name"))
        self.enter_datatype_label.setText(_translate("WrongFormat_page", "Enter Wanted Data Type"))
        self.data_combo_box.setItemText(0, _translate("WrongFormat_page", "str"))
        self.data_combo_box.setItemText(1, _translate("WrongFormat_page", "int"))
        self.data_combo_box.setItemText(2, _translate("WrongFormat_page", "float"))
        self.data_combo_box.setItemText(3, _translate("WrongFormat_page", "bool"))
        self.convert_button.setText(_translate("WrongFormat_page", "Convert"))
        self.convert_date_button.setText(_translate("WrongFormat_page", "Convert Into Date"))
        self.transform_label.setText(_translate("WrongFormat_page", "Transform"))
        self.format_secret_label.setText(_translate("WrongFormat_page", ""))
        self.DateTime_label.setText(_translate("WrongFormat_page", "Converts Into Datetime Format"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WrongFormat_page = QtWidgets.QMainWindow()
    ui = Ui_WrongFormat_page()
    ui.setupUi(WrongFormat_page)
    WrongFormat_page.show()
    sys.exit(app.exec_())
