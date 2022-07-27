from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd


class Ui_EmptyRows_Page(object):

    def BackWard(self):
        from Options import Ui_Options_Page

        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Options_Page()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, EmptyRows_Page):
        EmptyRows_Page.setObjectName("EmptyRows_Page")
        EmptyRows_Page.resize(1051, 632)
        self.centralwidget = QtWidgets.QWidget(EmptyRows_Page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.emptyrow_label = QtWidgets.QLabel(self.centralwidget)
        self.emptyrow_label.setGeometry(QtCore.QRect(10, 10, 1031, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.emptyrow_label.setFont(font)
        self.emptyrow_label.setFrameShape(QtWidgets.QFrame.Box)
        self.emptyrow_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.emptyrow_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emptyrow_label.setObjectName("emptyrow_label")

# ------------------------------------------- SECRET LABEL ------------------------------------- #
        self.secret_empty_label_new = QtWidgets.QLabel(self.centralwidget)
        self.secret_empty_label_new.setGeometry(QtCore.QRect(900, 10, 100, 51))
        self.secret_empty_label_new.setStyleSheet("color: rgb(240, 240, 240);")
        self.secret_empty_label_new.setObjectName("secret_empty_label")

# ---------------------------------------------------------------------------------------------- #
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(150, 550, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("background-color: rgb(212, 212, 159);")
        self.back_button.setObjectName("back_button")
        
        self.remove_all_label = QtWidgets.QLabel(self.centralwidget)
        self.remove_all_label.setGeometry(QtCore.QRect(10, 290, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.remove_all_label.setFont(font)
        self.remove_all_label.setFrameShape(QtWidgets.QFrame.Box)
        self.remove_all_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.remove_all_label.setAlignment(QtCore.Qt.AlignCenter)
        self.remove_all_label.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.remove_all_label.setObjectName("remove_all_label")
        
        self.replace_all_label = QtWidgets.QLabel(self.centralwidget)
        self.replace_all_label.setGeometry(QtCore.QRect(10, 350, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.replace_all_label.setFont(font)
        self.replace_all_label.setFrameShape(QtWidgets.QFrame.Box)
        self.replace_all_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.replace_all_label.setAlignment(QtCore.Qt.AlignCenter)
        self.replace_all_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.replace_all_label.setObjectName("replace_all_label")
        
        self.replace_specified_label = QtWidgets.QLabel(self.centralwidget)
        self.replace_specified_label.setGeometry(QtCore.QRect(10, 410, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.replace_specified_label.setFont(font)
        self.replace_specified_label.setFrameShape(QtWidgets.QFrame.Box)
        self.replace_specified_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.replace_specified_label.setAlignment(QtCore.Qt.AlignCenter)
        self.replace_specified_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.replace_specified_label.setObjectName("replace_specified_button")
        
        self.replace_with_label = QtWidgets.QLabel(self.centralwidget)
        self.replace_with_label.setGeometry(QtCore.QRect(10, 470, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.replace_with_label.setFont(font)
        self.replace_with_label.setFrameShape(QtWidgets.QFrame.Box)
        self.replace_with_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.replace_with_label.setAlignment(QtCore.Qt.AlignCenter)
        self.replace_with_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.replace_with_label.setObjectName("replace_with_button")
        
        self.execution_label = QtWidgets.QLabel(self.centralwidget)
        self.execution_label.setGeometry(QtCore.QRect(10, 70, 1031, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.execution_label.setFont(font)
        self.execution_label.setFrameShape(QtWidgets.QFrame.Box)
        self.execution_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.execution_label.setText("")
        self.execution_label.setAlignment(QtCore.Qt.AlignCenter)
        self.execution_label.setWordWrap(True)
        self.execution_label.setObjectName("execution_label")
        
        self.first_line = QtWidgets.QFrame(self.centralwidget)
        self.first_line.setGeometry(QtCore.QRect(10, 330, 1031, 21))
        self.first_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.first_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.first_line.setObjectName("first_line")
        
        self.second_line = QtWidgets.QFrame(self.centralwidget)
        self.second_line.setGeometry(QtCore.QRect(10, 390, 1031, 21))
        self.second_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.second_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.second_line.setObjectName("second_line")
        
        self.third_line = QtWidgets.QFrame(self.centralwidget)
        self.third_line.setGeometry(QtCore.QRect(10, 450, 1031, 21))
        self.third_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.third_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.third_line.setObjectName("third_line")
        
        self.fourth_line = QtWidgets.QFrame(self.centralwidget)
        self.fourth_line.setGeometry(QtCore.QRect(10, 510, 1031, 21))
        self.fourth_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.fourth_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fourth_line.setObjectName("fourth_line")
        
        self.vertival_line_1 = QtWidgets.QFrame(self.centralwidget)
        self.vertival_line_1.setGeometry(QtCore.QRect(450, 240, 21, 281))
        self.vertival_line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertival_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertival_line_1.setObjectName("vertival_line_1")
        self.vertival_line_2 = QtWidgets.QFrame(self.centralwidget)
        self.vertival_line_2.setGeometry(QtCore.QRect(680, 240, 21, 281))
        self.vertival_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertival_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertival_line_2.setObjectName("vertival_line_2")
        
        self.enter_value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_value_1.setGeometry(QtCore.QRect(480, 350, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.enter_value_1.setFont(font)
        self.enter_value_1.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_value_1.setObjectName("enter_value_1")
        self.enter_value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_value_2.setGeometry(QtCore.QRect(480, 410, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.enter_value_2.setFont(font)
        self.enter_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_value_2.setObjectName("enter_value_2")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(480, 470, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.remove_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_all_button.setGeometry(QtCore.QRect(910, 290, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.remove_all_button.setFont(font)
        self.remove_all_button.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.remove_all_button.setObjectName("execute_all_button")
        
        self.execute_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.execute_all_button.setGeometry(QtCore.QRect(910, 350, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.execute_all_button.setFont(font)
        self.execute_all_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.execute_all_button.setObjectName("execute_all_button")
        
        self.execute_specified_button = QtWidgets.QPushButton(self.centralwidget)
        self.execute_specified_button.setGeometry(QtCore.QRect(910, 410, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.execute_specified_button.setFont(font)
        self.execute_specified_button.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.execute_specified_button.setObjectName("execute_specified_button")
        
        self.execute_chosen_button = QtWidgets.QPushButton(self.centralwidget)
        self.execute_chosen_button.setGeometry(QtCore.QRect(910, 470, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.execute_chosen_button.setFont(font)
        self.execute_chosen_button.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.execute_chosen_button.setObjectName("execute_chosen_button")
        
        self.show_column_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_column_button.setGeometry(QtCore.QRect(10, 180, 81, 31))
        self.show_column_button.setStyleSheet("background-color: rgb(95, 191, 142);")
        self.show_column_button.setObjectName("show_column_button")
        
        self.show_columns_label = QtWidgets.QLabel(self.centralwidget)
        self.show_columns_label.setGeometry(QtCore.QRect(100, 170, 941, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.show_columns_label.setFont(font)
        self.show_columns_label.setFrameShape(QtWidgets.QFrame.Box)
        self.show_columns_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.show_columns_label.setText("")
        self.show_columns_label.setWordWrap(True)
        self.show_columns_label.setObjectName("show_columns_label")
        
        self.vertival_line_3 = QtWidgets.QFrame(self.centralwidget)
        self.vertival_line_3.setGeometry(QtCore.QRect(880, 240, 21, 281))
        self.vertival_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertival_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertival_line_3.setObjectName("vertival_line_3")
        
        self.zero_line = QtWidgets.QFrame(self.centralwidget)
        self.zero_line.setGeometry(QtCore.QRect(10, 270, 1031, 21))
        self.zero_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.zero_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.zero_line.setObjectName("zero_line")
        
        self.enter_value_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_value_label.setGeometry(QtCore.QRect(480, 245, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.enter_value_label.setFont(font)
        self.enter_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_value_label.setObjectName("enter_value_label")
        
        self.enter_column_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_column_label.setGeometry(QtCore.QRect(700, 250, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.enter_column_label.setFont(font)
        self.enter_column_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_column_label.setObjectName("enter_column_label")
        
        self.column_line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.column_line_2.setGeometry(QtCore.QRect(700, 410, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.column_line_2.setFont(font)
        self.column_line_2.setAlignment(QtCore.Qt.AlignCenter)
        self.column_line_2.setObjectName("column_line_2")
        
        self.column_line_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.column_line_3.setGeometry(QtCore.QRect(700, 470, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.column_line_3.setFont(font)
        self.column_line_3.setAlignment(QtCore.Qt.AlignCenter)
        self.column_line_3.setObjectName("column_line_3")
        
        self.execute_command_label = QtWidgets.QLabel(self.centralwidget)
        self.execute_command_label.setGeometry(QtCore.QRect(910, 250, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.execute_command_label.setFont(font)
        self.execute_command_label.setAlignment(QtCore.Qt.AlignCenter)
        self.execute_command_label.setObjectName("execute_command_label")
        
        EmptyRows_Page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EmptyRows_Page)
        self.statusbar.setObjectName("statusbar")
        EmptyRows_Page.setStatusBar(self.statusbar)

        self.retranslateUi(EmptyRows_Page)
        QtCore.QMetaObject.connectSlotsByName(EmptyRows_Page)

# ------------------------------------- LOGIC ----------------------------------------- #
        # call methods:
        self.back_button.clicked.connect(self.BackWard)
        self.back_button.clicked.connect(self.Write_Back)
        self.back_button.clicked.connect(EmptyRows_Page.close)
        self.show_column_button.clicked.connect(self.Show_Columns)

        self.remove_all_button.clicked.connect(self.Remove_Nulls)
        self.execute_all_button.clicked.connect(self.Replace_All_NULL)
        self.execute_specified_button.clicked.connect(self.Replace_NULL_Specified)
        self.execute_chosen_button.clicked.connect(self.Replace_NULL_With_Chosen)

    # define method for back button:
    def Write_Back(self):
        file_name = self.secret_empty_label_new.text()
        self.ui.secret_label.setText(f'{file_name}')
        
    # define method for show columns button:
    def Show_Columns(self):
        name = self.secret_empty_label_new.text()
        df = pd.read_csv(f'{name}')
        Column_List = list(df.columns)
        Dictionary_List = {}
        for i in Column_List:
            Dictionary_List[i] = df[f'{i}'].dtype
        self.show_columns_label.setText(f'{Dictionary_List}')

    # define RemoveNull method:
    def Remove_Nulls(self):
        name = self.secret_empty_label_new.text()
        df = pd.read_csv(f'{name}')

        Big = pd.DataFrame(df.notnull())
        if False in Big.values:
            df.dropna(inplace=True)
            df.to_csv(f'{name}', index=False)
            self.execution_label.setText("All Rows Which Contained 'NULL Values' Are Permanently Removed!")
            self.execution_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        else:
            self.execution_label.setText("There is not any NULL value in file!")
            self.execution_label.setStyleSheet("background-color: rgb(170, 255, 255);")

    # define method for Replace All Null button:
    def Replace_All_NULL(self):
        entered_value = self.enter_value_1.text()
        name = self.secret_empty_label_new.text()
        df = pd.read_csv(f'{name}')

        Big = pd.DataFrame(df.notnull())
        if False in Big.values and len(entered_value) > 0:
            df.fillna(entered_value, inplace=True)
            df.to_csv(f'{name}', index=False)
            self.execution_label.setText(f'All NULL values have been replaced with {entered_value}!')
            self.execution_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        elif len(entered_value) == 0:
            self.execution_label.setText("Value Field is EMPTY!")
            self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        else:
            self.execution_label.setText("There is not any NULL value in file!")
            self.execution_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        
    
    # replace method to replace nulls in specified columns:
    def Replace_NULL_Specified(self):
        entered_value = self.enter_value_2.text()
        name = self.secret_empty_label_new.text()

        df = pd.read_csv(f'{name}')
        
        ColumnName = self.column_line_2.text()
        Column_List = list(df.columns)

        if len(ColumnName) > 0 and len(entered_value) > 0 and ColumnName in Column_List:
            Check_List = list(df[f'{ColumnName}'].notnull())
            if False in Check_List:
                df[f'{ColumnName}'].fillna(entered_value, inplace=True)
                df.to_csv(f'{name}', index=False)
                self.execution_label.setText(f'All NULL values In {ColumnName} Column have been replaced with {entered_value}!')
                self.execution_label.setStyleSheet("background-color: rgb(170, 255, 127);")
            else:
                self.execution_label.setText(f"There is not any NULL value in {ColumnName} Column")
                self.execution_label.setStyleSheet("background-color: rgb(170, 255, 255);")

        elif len(entered_value) == 0 and len(ColumnName) > 0 and ColumnName in Column_List:
            self.execution_label.setText("Value Field is EMPTY!")
            self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(entered_value) == 0 and len(ColumnName) > 0 and ColumnName not in Column_List:
            self.execution_label.setText("Value Field is EMPTY and ColumnName is not COTTECT!")
            self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(entered_value) == 0 and len(ColumnName) == 0:
            self.execution_label.setText("Column Name and Value Fields are EMPTY!")
            self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(entered_value) > 0 and len(ColumnName) > 0 and ColumnName not in Column_List:
            self.execution_label.setText("ColumnName is not CORRECT!")
            self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(entered_value) > 0 and len(ColumnName) == 0:
            self.execution_label.setText("ColumnName Field is EMPTY!")
            self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
    
    # define method for replace NULLs in Specified Columns with Median, Mean or Mode:----------------------------------------------------------    
    def Replace_NULL_With_Chosen(self):
        entered_value = self.comboBox.currentText()
        name = self.secret_empty_label_new.text()

        df = pd.read_csv(f'{name}')
        
        ColumnName = self.column_line_3.text()
        Column_List = list(df.columns)

        if len(ColumnName) > 0 and ColumnName in Column_List:
            Column_Data_Type = str(df[f'{ColumnName}'].dtype)
            Check_List = list(df[f'{ColumnName}'].notnull())
            
            if Column_Data_Type[:3] == 'int' or Column_Data_Type[:5] == 'float':
                if False in Check_List:
                    if entered_value == 'Mean':
                        a = df[f'{ColumnName}'].mean()
                    elif entered_value == 'Median':
                        a = df[f'{ColumnName}'].median()
                    elif entered_value == 'Mode':
                        a = df[f'{ColumnName}'].mode()[0]

                    df[f'{ColumnName}'].fillna(a, inplace=True)
                    df.to_csv(f'{name}', index=False)
                    self.execution_label.setText(f"All NULL values In {ColumnName} Column have been replaced with Column's {entered_value}!")
                    self.execution_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                else:
                    self.execution_label.setText(f"There is not any NULL value in {ColumnName} column!")
                    self.execution_label.setStyleSheet("background-color: rgb(170, 255, 255);")
            
            elif Column_Data_Type[:3] != 'int' or Column_Data_Type[:5] != 'float':
                self.execution_label.setText("Data type of Entered ColumnName should be 'int' or 'float'!")
                self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(ColumnName) > 0 and ColumnName not in Column_List:
            self.execution_label.setText("Column Name is not CORRECT, Change it!")
            self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(ColumnName) == 0:
            self.execution_label.setText("Column Name Field is EMPTY, Fill it!")
            self.execution_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        

# -------------------------------------- END ------------------------------------------ #

    def retranslateUi(self, EmptyRows_Page):
        _translate = QtCore.QCoreApplication.translate
        EmptyRows_Page.setWindowTitle(_translate("EmptyRows_Page", "MainWindow"))
        self.emptyrow_label.setText(_translate("EmptyRows_Page", "Let\'s Clean Empty Rows!"))
        self.back_button.setText(_translate("EmptyRows_Page", "Save Changes and Go Back To MainWindow!"))
        self.remove_all_label.setText(_translate("EmptyRows_Page", "Remove All Rows With Empty Values"))
        self.replace_all_label.setText(_translate("EmptyRows_Page", "Replace All Empty Values - In All Columns - with specified value"))
        self.replace_specified_label.setText(_translate("EmptyRows_Page", "Replace All Empty Values - In Specified Column - with specified value"))
        self.replace_with_label.setText(_translate("EmptyRows_Page", "Replace All Empty Values - In Specified Column - with Mean, Median or Mode"))
        self.comboBox.setItemText(0, _translate("EmptyRows_Page", "Mean"))
        self.comboBox.setItemText(1, _translate("EmptyRows_Page", "Median"))
        self.comboBox.setItemText(2, _translate("EmptyRows_Page", "Mode"))
        self.execute_all_button.setText(_translate("EmptyRows_Page", "Replace All NULL"))
        self.execute_specified_button.setText(_translate("EmptyRows_Page", "Replace In Specified"))
        self.execute_chosen_button.setText(_translate("EmptyRows_Page", "Replace With Chosen"))
        self.show_column_button.setText(_translate("EmptyRows_Page", "show columns"))
        self.enter_value_label.setText(_translate("EmptyRows_Page", "Enter Value"))
        self.enter_column_label.setText(_translate("EmptyRows_Page", "Enter Column Name"))
        self.execute_command_label.setText(_translate("EmptyRows_Page", "Execute"))
        self.secret_empty_label_new.setText(_translate("EmptyRows_Page", ""))
        self.remove_all_button.setText(_translate("EmptyRows_Page", "Remove All NULL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmptyRows_Page = QtWidgets.QMainWindow()
    ui = Ui_EmptyRows_Page()
    ui.setupUi(EmptyRows_Page)
    EmptyRows_Page.show()
    sys.exit(app.exec_())
