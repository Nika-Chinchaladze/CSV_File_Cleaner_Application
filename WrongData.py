from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_WrongData_page(object):

    def ReturnBack(self):
        from Options import Ui_Options_Page

        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Options_Page()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, WrongData_page):
        WrongData_page.setObjectName("WrongData_page")
        WrongData_page.resize(1150, 573)
        self.centralwidget = QtWidgets.QWidget(WrongData_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.wrong_label = QtWidgets.QLabel(self.centralwidget)
        self.wrong_label.setGeometry(QtCore.QRect(10, 10, 1129, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wrong_label.setFont(font)
        self.wrong_label.setFrameShape(QtWidgets.QFrame.Box)
        self.wrong_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wrong_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wrong_label.setObjectName("wrong_label")
# --------------------------------------- secret label ----------------------------------------- #
        self.data_secret_label = QtWidgets.QLabel(self.centralwidget)
        self.data_secret_label.setGeometry(QtCore.QRect(1000, 10, 100, 51))
        self.data_secret_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.data_secret_label.setObjectName("data_secret_label")
# ---------------------------------------------------------------------------------------------- #
        
        self.comeback_button = QtWidgets.QPushButton(self.centralwidget)
        self.comeback_button.setGeometry(QtCore.QRect(100, 500, 949, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comeback_button.setFont(font)
        self.comeback_button.setStyleSheet("background-color: rgb(212, 212, 159);")
        self.comeback_button.setObjectName("comeback_button")
        
        self.command_label = QtWidgets.QLabel(self.centralwidget)
        self.command_label.setGeometry(QtCore.QRect(10, 70, 1129, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.command_label.setFont(font)
        self.command_label.setFrameShape(QtWidgets.QFrame.Box)
        self.command_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.command_label.setText("")
        self.command_label.setAlignment(QtCore.Qt.AlignCenter)
        self.command_label.setWordWrap(True)
        self.command_label.setObjectName("command_label")
        
        self.remove_label = QtWidgets.QLabel(self.centralwidget)
        self.remove_label.setGeometry(QtCore.QRect(10, 300, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_label.setFont(font)
        self.remove_label.setFrameShape(QtWidgets.QFrame.Box)
        self.remove_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.remove_label.setText("")
        self.remove_label.setAlignment(QtCore.Qt.AlignCenter)
        self.remove_label.setWordWrap(True)
        self.remove_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.remove_label.setObjectName("remove_label")
        
        self.replace_label = QtWidgets.QLabel(self.centralwidget)
        self.replace_label.setGeometry(QtCore.QRect(10, 400, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.replace_label.setFont(font)
        self.replace_label.setFrameShape(QtWidgets.QFrame.Box)
        self.replace_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.replace_label.setText("")
        self.replace_label.setAlignment(QtCore.Qt.AlignCenter)
        self.replace_label.setWordWrap(True)
        self.replace_label.setStyleSheet("background-color: rgb(147, 220, 220);")
        self.replace_label.setObjectName("remove_label")
        
        self.show_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_button.setGeometry(QtCore.QRect(10, 190, 91, 41))
        self.show_button.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.show_button.setObjectName("show_button")
        
        self.column_label = QtWidgets.QLabel(self.centralwidget)
        self.column_label.setGeometry(QtCore.QRect(110, 190, 1029, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.column_label.setFont(font)
        self.column_label.setFrameShape(QtWidgets.QFrame.Box)
        self.column_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.column_label.setText("")
        self.column_label.setWordWrap(True)
        self.column_label.setObjectName("column_label")
        
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(10, 270, 1129, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 380, 1129, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 480, 1129, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.vertical_line_0 = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line_0.setGeometry(QtCore.QRect(477, 246, 20, 241))
        self.vertical_line_0.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_0.setObjectName("vertical_line_0")
        
        self.vertical_line_1 = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line_1.setGeometry(QtCore.QRect(330, 246, 20, 241))
        self.vertical_line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_1.setObjectName("vertical_line_1")
        
        self.vertical_line_2 = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line_2.setGeometry(QtCore.QRect(624, 246, 21, 241))
        self.vertical_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_2.setObjectName("vertical_line_2")
        
        self.vertical_line_3 = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line_3.setGeometry(QtCore.QRect(773, 246, 21, 241))
        self.vertical_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_3.setObjectName("vertical_line_3")

        self.vertical_line_4 = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line_4.setGeometry(QtCore.QRect(965, 246, 21, 241))
        self.vertical_line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_4.setObjectName("vertical_line_4")

        self.vertical_line_5 = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line_5.setGeometry(QtCore.QRect(1128, 246, 21, 241))
        self.vertical_line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_5.setObjectName("vertical_line_5")

        self.operation_label = QtWidgets.QLabel(self.centralwidget)
        self.operation_label.setGeometry(QtCore.QRect(493, 242, 130, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.operation_label.setFont(font)
        self.operation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.operation_label.setObjectName("operation_label")

        self.control_label = QtWidgets.QLabel(self.centralwidget)
        self.control_label.setGeometry(QtCore.QRect(348, 242, 130, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.control_label.setFont(font)
        self.control_label.setAlignment(QtCore.Qt.AlignCenter)
        self.control_label.setObjectName("control_label")

        self.control_value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.control_value_1.setGeometry(QtCore.QRect(348, 320, 130, 31))
        self.control_value_1.setAlignment(QtCore.Qt.AlignCenter)
        self.control_value_1.setObjectName("control_value_1")

        self.control_value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.control_value_2.setGeometry(QtCore.QRect(348, 420, 130, 31))
        self.control_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.control_value_2.setObjectName("control_value_2")
        
        self.value_label = QtWidgets.QLabel(self.centralwidget)
        self.value_label.setGeometry(QtCore.QRect(657, 242, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.value_label.setFont(font)
        self.value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.value_label.setObjectName("value_label")
        
        self.EnterColumn_label = QtWidgets.QLabel(self.centralwidget)
        self.EnterColumn_label.setGeometry(QtCore.QRect(805, 240, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EnterColumn_label.setFont(font)
        self.EnterColumn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.EnterColumn_label.setObjectName("EnterColumn_label")
       
        self.do_it_label = QtWidgets.QLabel(self.centralwidget)
        self.do_it_label.setGeometry(QtCore.QRect(985, 240, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.do_it_label.setFont(font)
        self.do_it_label.setAlignment(QtCore.Qt.AlignCenter)
        self.do_it_label.setObjectName("do_it_label")
        
        self.edit_column_name_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_column_name_1.setGeometry(QtCore.QRect(793, 320, 171, 31))
        self.edit_column_name_1.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_column_name_1.setObjectName("edit_column_name_1")
        
        self.edit_column_name_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_column_name_2.setGeometry(QtCore.QRect(793, 420, 171, 31))
        self.edit_column_name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_column_name_2.setObjectName("edit_column_name_2")
        
        self.edit_value = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_value.setGeometry(QtCore.QRect(643, 420, 130, 31))
        self.edit_value.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_value.setObjectName("edit_value")

        self.op_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.op_combo_box.setGeometry(QtCore.QRect(510, 319, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.op_combo_box.setFont(font)
        self.op_combo_box.setObjectName("op_combo_box")
        self.op_combo_box.addItem("")
        self.op_combo_box.addItem("")
        self.op_combo_box.addItem("")
        self.op_combo_box.addItem("")
        self.op_combo_box.addItem("")

        self.down_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.down_combo_box.setGeometry(QtCore.QRect(510, 420, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.down_combo_box.setFont(font)
        self.down_combo_box.setObjectName("op_combo_box")
        self.down_combo_box.addItem("")
        self.down_combo_box.addItem("")
        self.down_combo_box.addItem("")
        self.down_combo_box.addItem("")
        self.down_combo_box.addItem("")
        
        self.execute_remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.execute_remove_button.setGeometry(QtCore.QRect(985, 320, 141, 31))
        self.execute_remove_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.execute_remove_button.setObjectName("execute_remove_button")
        
        self.execute_replace_button = QtWidgets.QPushButton(self.centralwidget)
        self.execute_replace_button.setGeometry(QtCore.QRect(985, 420, 141, 31))
        self.execute_replace_button.setStyleSheet("background-color: rgb(147, 220, 220);")
        self.execute_replace_button.setObjectName("execute_replace_button")
        
        WrongData_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WrongData_page)
        self.statusbar.setObjectName("statusbar")
        WrongData_page.setStatusBar(self.statusbar)

        self.retranslateUi(WrongData_page)
        QtCore.QMetaObject.connectSlotsByName(WrongData_page)

# ---------------------------------------- LOGIC -------------------------------------------- #
        # call methods:
        self.comeback_button.clicked.connect(self.ReturnBack)
        self.comeback_button.clicked.connect(self.WriteBack_On_Options)
        self.comeback_button.clicked.connect(WrongData_page.close)
        self.show_button.clicked.connect(self.ShowCSV_File_Columns)
        self.execute_remove_button.clicked.connect(self.Execute_Remove_Function)
        self.execute_replace_button.clicked.connect(self.Execute_Replace_Function)

    # define write back method for return button:
    def WriteBack_On_Options(self):
        file_name = self.data_secret_label.text()
        self.ui.secret_label.setText(f'{file_name}')
    
    # define method for showCol button:
    def ShowCSV_File_Columns(self):
        name = self.data_secret_label.text()
        df = pd.read_csv(f'{name}')
        Column_List = list(df.columns)
        Dictionary_List = {}
        for i in Column_List:
            Dictionary_List[i] = df[f'{i}'].dtype
        self.column_label.setText(f'{Dictionary_List}')
    
    # define method for execute remove button:
    def Execute_Remove_Function(self):
        remove_str = self.control_value_1.text()
        comparison_sign = self.op_combo_box.currentText()
        column_name = self.edit_column_name_1.text()
        control_value = self.control_value_1.text()
        
        file_name = self.data_secret_label.text()
        df = pd.read_csv(f'{file_name}')

        if len(control_value) > 0 and len(column_name) > 0:
            try:
                control_value = float(self.control_value_1.text())

                if column_name in list(df.columns) and df[column_name].dtype != 'O':
                    if comparison_sign == '==':
                        for i in df.index:
                            if df.loc[i, column_name] == control_value:
                                df.drop(i, inplace=True)
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values Equal To {control_value} Have Been Deleted!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                    elif comparison_sign == '>':
                        for i in df.index:
                            if df.loc[i, column_name] > control_value:
                                df.drop(i, inplace=True)
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values More Than {control_value} Have Been Deleted!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                    elif comparison_sign == '<':
                        for i in df.index:
                            if df.loc[i, column_name] < control_value:
                                df.drop(i, inplace=True)
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values Less Than {control_value} Have Been Deleted!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                    elif comparison_sign == '>=':
                        for i in df.index:
                            if df.loc[i, column_name] >= control_value:
                                df.drop(i, inplace=True)
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values Equal To or More Than {control_value} Have Been Deleted!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                    elif comparison_sign == '<=':
                        for i in df.index:
                            if df.loc[i, column_name] <= control_value:
                                df.drop(i, inplace=True)
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values Equal To or Less Than {control_value} Have Been Deleted!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                elif column_name not in list(df.columns):
                    self.command_label.setText("Entered Column Name is not CORRECT, check 'Show Columns' button!")
                    self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
            except ValueError:
                if df[column_name].dtype == 'O' and comparison_sign == '==':
                    for i in df.index:
                        if df.loc[i, column_name] == remove_str:
                            df.drop(i, inplace=True)
                    self.command_label.setText(f"Values Equal To {remove_str} Have Been Deleted Permanently!")
                    self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                else:
                    self.command_label.setText("Control Value is not Numeric, 'It can not be converted into float or int' - So it is useless for Comparison Purposes! Write Only Numbers Here!")
                    self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(control_value) == 0 and len(column_name) > 0:
            self.command_label.setText("Control Value Field is EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(control_value) > 0 and len(column_name) == 0:
            self.command_label.setText("Column Name Field is EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(control_value) == 0 and len(column_name) == 0:
            self.command_label.setText("Control Value and Column Name Fields are EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        df.to_csv(f'{file_name}', index=False)
    
    # define method for execute remove button:
    def Execute_Replace_Function(self):
        replace_str = self.control_value_2.text()
        new_str = self.edit_value.text()
        comparison_sign = self.down_combo_box.currentText()
        column_name = self.edit_column_name_2.text()
        control_value = self.control_value_2.text()
        new_value = self.edit_value.text()
        
        file_name = self.data_secret_label.text()
        df = pd.read_csv(f'{file_name}')

        if len(control_value) > 0 and len(new_value) > 0 and len(column_name) > 0:
            try:
                control_value = float(self.control_value_2.text())
                new_value = float(self.edit_value.text())

                if column_name in list(df.columns) and df[column_name].dtype != 'O':
                    if comparison_sign == '==':
                        for i in df.index:
                            if df.loc[i, column_name] == control_value:
                                df.loc[i, column_name] = new_value
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values Equal To {control_value} Have Been Changed with {new_value}!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                    elif comparison_sign == '>':
                        for i in df.index:
                            if df.loc[i, column_name] > control_value:
                                df.loc[i, column_name] = new_value
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values More Than {control_value} Have Been Changed with {new_value}!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                    elif comparison_sign == '<':
                        for i in df.index:
                            if df.loc[i, column_name] < control_value:
                                df.loc[i, column_name] = new_value
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values Less Than {control_value} Have Been Changed with {new_value}!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                    elif comparison_sign == '>=':
                        for i in df.index:
                            if df.loc[i, column_name] >= control_value:
                                df.loc[i, column_name] = new_value
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values Equal To or More Than {control_value} Have Been Changed with {new_value}!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                    elif comparison_sign == '<=':
                        for i in df.index:
                            if df.loc[i, column_name] <= control_value:
                                df.loc[i, column_name] = new_value
                        self.command_label.setText(f'Operation Has Been Completed Successfully! Values Equal To or Less Than {control_value} Have Been Changed with {new_value}!')
                        self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                elif column_name not in list(df.columns):
                    self.command_label.setText("Entered Column Name is not CORRECT, check 'Show Columns' button!")
                    self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
            except ValueError:
                if df[column_name].dtype == 'O' and comparison_sign == '==':
                    for i in df.index:
                        if df.loc[i, column_name] == replace_str:
                            df.loc[i, column_name] = new_str
                    self.command_label.setText(f"Values Equal To {replace_str} Have Been Replaced with {new_str}!")
                    self.command_label.setStyleSheet("background-color: rgb(170, 255, 127);")
                else:
                    self.command_label.setText("Control Value or New Value is not Numeric, 'They can not be converted into float or int' - So they are useless for Comparison Purposes! Write Only Numbers Here!")
                    self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(control_value) == 0 and len(new_value) > 0 and len(column_name) > 0:
            self.command_label.setText("Control Value Field is EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(control_value) > 0 and len(new_value) == 0 and len(column_name) > 0:
            self.command_label.setText("New Value Field is EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(control_value) > 0 and len(new_value) > 0 and len(column_name) == 0:
            self.command_label.setText("Column Name Field is EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(control_value) == 0 and len(new_value) == 0 and len(column_name) > 0:
            self.command_label.setText("Control Value and New Value Fields are EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(control_value) == 0 and len(new_value) > 0 and len(column_name) == 0:
            self.command_label.setText("Control Value and Column Name Fields are EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        elif len(control_value) > 0 and len(new_value) == 0 and len(column_name) == 0:
            self.command_label.setText("New Value and Column Name Fields are EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        elif len(control_value) == 0 and len(new_value) == 0 and len(column_name) == 0:
            self.command_label.setText("Necessary Fields are EMPTY!")
            self.command_label.setStyleSheet("background-color: rgb(255, 80, 83);")
        
        
        df.to_csv(f'{file_name}', index=False)

# ----------------------------------------- END --------------------------------------------- #

    def retranslateUi(self, WrongData_page):
        _translate = QtCore.QCoreApplication.translate
        WrongData_page.setWindowTitle(_translate("WrongData_page", "MainWindow"))
        self.wrong_label.setText(_translate("WrongData_page", "Let\'s Clean Wrong Data!"))
        self.remove_label.setText(_translate("WrongData_page", "Remove Wrong Data, Fill All Necessary Fields"))
        self.replace_label.setText(_translate("WrongData_page", "Replace Wrong Data, Fill All Necessary Fields"))
        self.comeback_button.setText(_translate("WrongData_page", "Save Changes and Go Back To MainWindow!"))
        self.show_button.setText(_translate("WrongData_page", "Show Columns"))
        self.value_label.setText(_translate("WrongData_page", "New Value"))
        self.EnterColumn_label.setText(_translate("WrongData_page", "Enter Column Name"))
        self.do_it_label.setText(_translate("WrongData_page", "Execute"))
        self.execute_remove_button.setText(_translate("WrongData_page", "Remove"))
        self.execute_replace_button.setText(_translate("WrongData_page", "Replace"))
        self.data_secret_label.setText(_translate("WrongData_page", ""))
        self.operation_label.setText(_translate("WrongData_page", "Comparison"))
        self.op_combo_box.setItemText(0, _translate("WrongFormat_page", "=="))
        self.op_combo_box.setItemText(1, _translate("WrongFormat_page", ">"))
        self.op_combo_box.setItemText(2, _translate("WrongFormat_page", "<"))
        self.op_combo_box.setItemText(3, _translate("WrongFormat_page", ">="))
        self.op_combo_box.setItemText(4, _translate("WrongFormat_page", "<="))
        self.down_combo_box.setItemText(0, _translate("WrongFormat_page", "=="))
        self.down_combo_box.setItemText(1, _translate("WrongFormat_page", ">"))
        self.down_combo_box.setItemText(2, _translate("WrongFormat_page", "<"))
        self.down_combo_box.setItemText(3, _translate("WrongFormat_page", ">="))
        self.down_combo_box.setItemText(4, _translate("WrongFormat_page", "<="))
        self.control_label.setText(_translate("WrongData_page", "Control Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WrongData_page = QtWidgets.QMainWindow()
    ui = Ui_WrongData_page()
    ui.setupUi(WrongData_page)
    WrongData_page.show()
    sys.exit(app.exec_())
