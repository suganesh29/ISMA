# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import *

from PyQt5 import QtCore, QtGui, QtWidgets

from DEMATMM import Ui_MainWindow
from signup import Ui_Signup
import sqlite3


class Ui_Dialoglogin(object):


    
    def showMessagebox(self,title,message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msgbox.exec_()
#####define the  function to oepn the Mainwindow  if login is sucessfull############
    def LoginWindowShow(self):
        self.ww1 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.ww1)
        self.ww1.show()
#####define the  function to oepn the Sign upwindow############
    def SignupWindowShow(self):
        self.ww2 = QtWidgets.QDialog()
        self.ui2 = Ui_Signup()
        self.ui2.setupUi2(self.ww2)
        self.ww2.show()   
#####define the logincheck function############
    def logincheck(self):

        uname = self.uname_lineedit.text()
        password = self.password_lineedit.text()
        #print("Login Button is Clicked")
    


#################database connection###############
        connection = sqlite3.connect("login.db")
        result = connection.execute ("SELECT * FROM USERS WHERE USERNAME= ? AND PASSWORD = ?",(uname,password))
        if ( len (result.fetchall()) > 0):
           print("User Found!")
           self.LoginWindowShow()
            
            
        else :
            print("User Not Found!")
            self.showMessagebox('Warning!',' Invalid UserName or Password')

        connection.close()  
######################################################
#####define the signupcheck function##################

    def signupcheck(self):
        print("Signup Button is Clicked")
        self.SignupWindowShow()
########################################################
    def on_click(self):
        self.ex1 = Ui_Dialoglogin()

    def setupUi(self, Dialoglogin):
        Dialoglogin.setObjectName("Dialoglogin")
        Dialoglogin.resize(460, 350)
        Dialoglogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialoglogin.setStyleSheet("QDialog {\n"
"background-color: beige;\n"
"}\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}")
        self.username_label = QtWidgets.QLabel(Dialoglogin)
        self.username_label.setGeometry(QtCore.QRect(80, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
       
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialoglogin)
        self.password_label.setGeometry(QtCore.QRect(80, 130, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.uname_lineedit = QtWidgets.QLineEdit(Dialoglogin)
        self.uname_lineedit.setGeometry(QtCore.QRect(220, 110, 113, 20))
        self.uname_lineedit.setObjectName("uname_lineedit")
        self.password_lineedit = QtWidgets.QLineEdit(Dialoglogin)
        self.password_lineedit.setGeometry(QtCore.QRect(220, 150, 113, 20))
        self.password_lineedit.setObjectName("password_lineedit")
        self.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.pushButton = QtWidgets.QPushButton(Dialoglogin)
        self.pushButton.setGeometry(QtCore.QRect(220, 210, 51, 30))

####################################################

        self.pushButton.clicked.connect(self.logincheck)


##################################################
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialoglogin)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 210, 51, 30))

#####################################################
        self.pushButton_2.clicked.connect(self.signupcheck)


##################################################

        font = QtGui.QFont()
        font.setFamily("Bell MT")
        
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialoglogin)
        self.label.setGeometry(QtCore.QRect(90, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialoglogin)
        QtCore.QMetaObject.connectSlotsByName(Dialoglogin)

    def retranslateUi(self, Dialoglogin):
        _translate = QtCore.QCoreApplication.translate
        Dialoglogin.setWindowTitle(_translate("Dialoglogin", "Dialog"))
        self.username_label.setText(_translate("Dialoglogin", "USERNAME:"))
        self.password_label.setText(_translate("Dialoglogin", "PASSWORD:"))
        self.pushButton.setText(_translate("Dialoglogin", "Login"))
        self.pushButton_2.setText(_translate("Dialoglogin", "Sign Up"))
        self.label.setText(_translate("Dialoglogin", "Login Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialoglogin = QtWidgets.QDialog()
    ui = Ui_Dialoglogin()
    ui.setupUi(Dialoglogin)
    Dialoglogin.show()
    sys.exit(app.exec_())
