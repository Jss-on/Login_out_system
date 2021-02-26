# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registration_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pylightxl as xl 
from os import getcwd

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(331, 154)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 120, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.getInfo)
        self.buttonBox.rejected.connect(self.IfReject) 
        
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 101))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(70, 30, 201, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems([" ","add people here"])
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 60, 201, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems([" ","add group here"])
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 47, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 47, 14))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registration Form"))
        self.groupBox.setTitle(_translate("Dialog", "Please Enter Correct Data"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Group"))

    def getInfo(self):
        
        # printing the form information 
        reg_file = open(r'reg_file.txt', "w+")
        reg_file.write(self.comboBox.currentText()) #name
        reg_file.write("\n")
        reg_file.write(self.comboBox_2.currentText()) #group         
        reg_file.close()
        
        #if clicked cancel 
        
        key_file = open(r'key.txt','w+') 
        key_file.write("true")
        key_file.close()
        
        
        
        
        
        
    def IfReject(self):
        key_file = open(r'key.txt','w+') 
        key_file.write("false")
        key_file.close()
        
        self.close()
        
    # def writeDateToExcel(self):
    #     username = self.comboBox.currentText()
    #     self.updateExcelAddress("E2", username)
        
    #     usergroup = self.comboBox_2.currentText() 
    #     self.updateExcelAddress("G2", usergroup) 
        
    #     DIR = getcwd()
    #     self.updateExcelAddress("A4", DIR)
        
        
    # def updateExcelAddress(self,address: str, val: str):
    #     DIR = getcwd() 
    #     log = xl.readxl(fn=r'{}\logging.xlsm'.format(DIR))
    #     log.ws(ws = "log").update_address(address=address, val = val)
        
    

def DisplayRegistrationForm():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

#DisplayRegistrationForm()
   
