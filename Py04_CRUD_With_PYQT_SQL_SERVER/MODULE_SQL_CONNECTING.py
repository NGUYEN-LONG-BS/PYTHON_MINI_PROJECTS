from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
import xlwings as xw    # Thư viện chuyên dùng để xử lý Excel
from openpyxl import load_workbook, Workbook
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 294)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_CONNECT = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_CONNECT.setGeometry(QtCore.QRect(20, 210, 261, 31))
        self.pushButton_CONNECT.setObjectName("pushButton_CONNECT")
        self.label_SERVERNAME = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_SERVERNAME.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.label_SERVERNAME.setObjectName("label_SERVERNAME")
        self.label_DATABASE_NAME = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_DATABASE_NAME.setGeometry(QtCore.QRect(20, 60, 91, 31))
        self.label_DATABASE_NAME.setObjectName("label_DATABASE_NAME")
        self.label_LOGIN_PASS = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_LOGIN_PASS.setGeometry(QtCore.QRect(20, 160, 91, 31))
        self.label_LOGIN_PASS.setObjectName("label_LOGIN_PASS")
        self.plainTextEdit_SERVER_NAME = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_SERVER_NAME.setGeometry(QtCore.QRect(120, 10, 251, 31))
        self.plainTextEdit_SERVER_NAME.setObjectName("plainTextEdit_SERVER_NAME")
        self.plainTextEdit_DATABASE_NAME = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_DATABASE_NAME.setGeometry(QtCore.QRect(120, 60, 251, 31))
        self.plainTextEdit_DATABASE_NAME.setObjectName("plainTextEdit_DATABASE_NAME")
        self.plainTextEdit_LOGIN_NAME = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_LOGIN_NAME.setGeometry(QtCore.QRect(120, 110, 251, 31))
        self.plainTextEdit_LOGIN_NAME.setObjectName("plainTextEdit_LOGIN_NAME")
        self.plainTextEdit_LOGIN_PASS = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_LOGIN_PASS.setGeometry(QtCore.QRect(120, 160, 251, 31))
        self.plainTextEdit_LOGIN_PASS.setObjectName("plainTextEdit_LOGIN_PASS")
        self.label_LOGIN_NAME = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_LOGIN_NAME.setGeometry(QtCore.QRect(20, 110, 91, 31))
        self.label_LOGIN_NAME.setObjectName("label_LOGIN_NAME")
        self.pushButton_CLOSE = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_CLOSE.setGeometry(QtCore.QRect(290, 210, 81, 31))
        self.pushButton_CLOSE.setObjectName("pushButton_CLOSE")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.pushButton_CLOSE.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton_CONNECT.clicked.connect(self.DF_TO_EXCEL) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.label_SERVERNAME.setText(_translate("MainWindow", "SERVER NAME"))
        self.label_DATABASE_NAME.setText(_translate("MainWindow", "DATABASE NAME"))
        self.label_LOGIN_NAME.setText(_translate("MainWindow", "LOGIN NAME"))
        self.label_LOGIN_PASS.setText(_translate("MainWindow", "LOGIN PASS"))
        
        self.plainTextEdit_SERVER_NAME.setPlainText(_translate("MainWindow", "KSNB3\SQLEXPRESS"))
        self.plainTextEdit_DATABASE_NAME.setPlainText(_translate("MainWindow", "DATABASE_USER_ID"))
        self.plainTextEdit_LOGIN_NAME.setPlainText(_translate("MainWindow", "sa"))
        self.plainTextEdit_LOGIN_PASS.setPlainText(_translate("MainWindow", "123"))
        
        self.pushButton_CONNECT.setText(_translate("MainWindow", "CONNECT"))
        self.pushButton_CLOSE.setText(_translate("MainWindow", "CLOSE"))
        
    def DF_TO_EXCEL(self):
        stringServerName = 'KSNB3\SQLEXPRESS'
        # stringServerName = '103.90.227.154, 1433'
        # stringServerName = self.plainTextEdit_DATABASE_NAME.toPlainText
        # print(stringDatabaseName)
        stringDatabaseName = 'DATABASE_USER_ID'
        stringPort = '1433'
        
        # conn = pyodbc.connect('Server=KSNB3\SQLEXPRESS;Database=DATABASE_USER_ID;Trusted_Connection=True;PORT=1433;DRIVER={SQL Server}')
        conn = pyodbc.connect(
                            'Server=' + stringServerName + ';'
                            'Database=' + stringDatabaseName + ';'
                            'Trusted_Connection=True;PORT=' + stringPort + ';'
                            'DRIVER={SQL Server}'
                            )
        cursor = conn.cursor()
        cursor.execute('Select * from TB_DS_DATABASE')
        rows = cursor.fetchall()
        # print(rows)   # Kiểm tra đã lấy được dữ liệu chưa
        cursor.close()
        conn.close()
        # Load in the workbook
        # Trên Desktop, tạo sẵn 1 file Excel có tên: OUTPUT.xlsx
        df = pd.read_excel(r'C:\Users\ADMIN\Desktop\OUTPUT.xlsx')
        # Convert the fetched rows to a DataFrame
        # File Excel phải đang đóng
        df2 = pd.DataFrame(rows)
        # print(df2)      # Kiểm tra đã lấy được dữ liệu chưa
        df2.to_excel(r'C:\Users\ADMIN\Desktop\OUTPUT.xlsx', index=False)
        msg=QtWidgets.QMessageBox()
        msg.setInformativeText("Đã lấy được dữ liệu và xuất ra Excel")
        msg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
