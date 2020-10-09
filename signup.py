# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Signup(object):



    def insertData(self):
        username = self.uname_lineedit2.text()
        email = self.email_lineedit2.text()
        password = self.password_lineedit_2.text()
        
        connection = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES (?,?,?)", (username,email,password))
        connection.commit()
        connection.close()



    def setupUi2(self, Dialogsignup):
        Dialogsignup.setObjectName("Dialogsignup")
        Dialogsignup.resize(704, 442)
        Dialogsignup.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialogsignup)
        self.label.setGeometry(QtCore.QRect(130, 50, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialogsignup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 110, 141, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.username_label2.setFont(font)
        self.username_label2.setObjectName("username_label2")
        self.verticalLayout.addWidget(self.username_label2)
        self.password_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.password_label_2.setFont(font)
        self.password_label_2.setObjectName("password_label_2")
        self.verticalLayout.addWidget(self.password_label_2)
        self.email_label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.email_label2.setFont(font)
        self.email_label2.setObjectName("email_label2")
        self.verticalLayout.addWidget(self.email_label2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialogsignup)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 110, 251, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.email_lineedit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.email_lineedit2.setObjectName("email_lineedit2")
        self.verticalLayout_2.addWidget(self.email_lineedit2)
        self.password_lineedit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.password_lineedit_2.setObjectName("password_lineedit_2")
        self.verticalLayout_2.addWidget(self.password_lineedit_2)
        self.uname_lineedit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.uname_lineedit2.setObjectName("uname_lineedit2")
        self.verticalLayout_2.addWidget(self.uname_lineedit2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialogsignup)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 250, 251, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)

###########################################################################
        self.pushButton.clicked.connect(self.insertData)
###########################################################################



        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.retranslateUi(Dialogsignup)
        QtCore.QMetaObject.connectSlotsByName(Dialogsignup)

    def retranslateUi(self, Dialogsignup):
        _translate = QtCore.QCoreApplication.translate
        Dialogsignup.setWindowTitle(_translate("Dialogsignup", "Dialog"))
        self.label.setText(_translate("Dialogsignup", "Create account"))
        self.username_label2.setText(_translate("Dialogsignup", "USERNAME:"))
        self.password_label_2.setText(_translate("Dialogsignup", "PASSWORD:"))
        self.email_label2.setText(_translate("Dialogsignup", "EMAIL ID:"))
        self.pushButton.setText(_translate("Dialogsignup", "Sign Up"))
        self.pushButton_2.setText(_translate("Dialogsignup", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialogsignup = QtWidgets.QDialog()
    ui = Ui_Dialogsignup()
    ui.setupUi2(Dialogsignup)
    Dialogsignup.show()
    sys.exit(app.exec_())
