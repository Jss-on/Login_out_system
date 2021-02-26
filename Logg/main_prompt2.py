# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_prompt_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date	
# from datetime import datetime	
import time	
import os, os.path
import win32com.client



done_save_log = False


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 343)
        doneLogin = self.isLogInDone() 
        haveTicket = self.haveLogOutTicket()
        
        self.pushButton = QtWidgets.QPushButton(Form)
        if doneLogin:
            self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Qualy")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        if (not doneLogin) or (not haveTicket):
                self.pushButton_2.setEnabled(False)
            
        else:
            self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 230, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Qualy")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 301, 121))
        self.groupBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 320, 151, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 320, 81, 21))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 301, 51))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 281, 21))
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 80, 301, 41))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 15, 281, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 120, 301, 81))
        self.groupBox_4.setObjectName("groupBox_4")
        
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 261, 18))
        self.checkBox.setObjectName("checkBox")
        self.groupBox_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.checkBox.raise_()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        
        
        
        #fetch data from reg_file.txt 
        reg_file_content = open(r'reg_file.txt','r')
        content = reg_file_content.read()
        reg_file_content.close()
        split_content = content.split("\n")
        user_name = split_content[0] 
        user_group = split_content[1]
        
        #get date and time
        todays_date = date.today()
        weekday = todays_date.strftime("%a")
        
        #login done save variable
        # self.done_save_log = False 
        
        #initilize current running time 
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Log Prompt "))
        self.pushButton.setText(_translate("Form", "LOG IN"))
        self.pushButton.clicked.connect(self.LOGINButtonPress)
        self.pushButton_2.setText(_translate("Form", "LOG OUT"))
        self.pushButton_2.clicked.connect(self.LOGOUTButtonPress)
        self.groupBox_2.setTitle(_translate("Form", "Press to Log"))
        self.label.setText(_translate("Form", "{Name}".format(Name = user_name))) 
        self.label_2.setText(_translate("Form", "{Group}".format(Group = user_group)))
        self.groupBox.setTitle(_translate("Form", "Display"))
        self.label_3.setText(_translate("Form", ""))
        self.groupBox_3.setTitle(_translate("Form", "Date"))
        self.label_4.setText(_translate("Form", "{Date}   {wk}".format(Date = todays_date,
                                                                     wk = weekday)))
        self.groupBox_4.setTitle(_translate("Form", "Time"))
        self.checkBox.setText(_translate("Form", "Automatic Send"))
        # self.label_5.setText(_translate("Form", "TextLabel"))
        self.checkBox.isChecked() 
      
        self.runTimer()
        
    def runTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showTime) 
        self.timer.start(1000)
        
        
        
    def showTime(self):
        global done_save_log
        if done_save_log:
            return 
        # getting current time 
        current_time = QtCore.QTime.currentTime() 
  
        # converting QTime object to string 
        label_time = current_time.toString('h:m:s ap') 
        # print("ses")
        # showing it to the label
        self.label_5.setText("{Time}".format(Time = label_time))
        #self.label.setText(label_time)
       
            
        
    def getCurrentTime(self):
        t = time.localtime() 
        current_time = time.strftime("%X", t)
        return current_time
        
    def OneSecondDelay(self):
        while True:
            time.sleep(1)
          
    
    def LOGINButtonPress(self):
        
        global done_save_log #used to stop the time running
        
        # done_save_log = False
        
        self.label_3.setText("Processing")
        
        #get current time
        current_time = self.getCurrentTime()
        current_date = date.today()
        self.label_5.setText("{Time}   saved".format(Time = current_time))
        done_save_log = True
        #get week number 
        
        week_number = current_date.isocalendar()[1]
        ADI_ww = week_number + 109 
        
        
        #delay fow a second
        self.label_4.setText("{Time}".format(Time = current_time))
        time.sleep(1)
        
        #get username, group, work week, login time
    
        user_data = open("reg_file.txt",'r')     
        
        userEm = user_data.read().split("\n")[0].split(" ")
        fn = userEm[0]
        ls = userEm[1]
        user_email = "{fn}.{ls}@analog.com".format(fn = fn, ls = ls) 
        
        user_data.close()
        
        
        user_data = open("reg_file.txt",'r')
        
        
        data_file = open("today_login_data.txt",'w')
        
        for content in user_data:
            data_file.write(content)
        
        data_file.write("\n")
        data_file.write(user_email)
        data_file.write("\n")
        data_file.write(str(current_date))
        data_file.write("\n")
        data_file.write(str(current_time))
        data_file.write("\n") 
        data_file.write(str(ADI_ww))
        if self.checkBox.isChecked():
            data_file.write("\n") 
            data_file.write("yes") #authorization send automatically 
        else:
            data_file.write("\n") 
            data_file.write("no")
        # path = os.getcwd()
        # data_file.write("\n") 
        # data_file.write(path)
        data_file.close() 
        user_data.close()
        
        #data content: name, group, current date, current time, current wwk
        #processing
        self.runLogInMacro()
        
        self.label_3.setText("Your LOGIN is successfull")
        
        self.pushButton.setEnabled(False)
    
    def runLogInMacro(self):
        if os.path.exists("Logging.xlsm"):
            xl=win32com.client.Dispatch("Excel.Application")
            xl.Workbooks.Open(os.path.abspath("Logging.xlsm"), ReadOnly=1)
            xl.Application.Run("Logging.xlsm!Transport.MainLoginProcess")
            #xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
            xl.Application.Quit() # Comment this out if your excel script closes
            del xl
            
    def isLogInDone(self) ->bool:
        try:
            Dir = os.getcwd()
            date_to_check = open(r'{}\today_login_data.txt'.format(Dir),'r').read()
            prev_date = date_to_check.split("\n")[3] 
            date_today = date.today()
            print(prev_date,type(prev_date))
            print(date_today,type(date_today))
            if prev_date == str(date_today): 
                return True 
            else:
                logOutTicket = open("ticket.txt","w")
                logOutTicket.write(str(1))
                logOutTicket.close()
                return False 
        except FileNotFoundError:
            return False
        
    def LOGOUTButtonPress(self):
        global done_save_log
        
        # done_save_log = False
        
        self.label_3.setText("Processing")
        
        #get current time
        current_time = self.getCurrentTime()
        current_date = date.today()
        self.label_5.setText("{Time}   saved".format(Time = current_time))
        done_save_log = True
        #get week number 
        

        #data content: name, group, current date, current time, current wwk
        #processing
        self.runLogOutMacro()
        
        self.label_3.setText("Your LOGOUT is successfull")
        
        #set logout ticket to 0
        t = open(r'ticket.txt','w+')
        t.write(str(0))
        t.close()
        
        self.pushButton_2.setEnabled(False)
        
        
    
    def runLogOutMacro(self):
        if os.path.exists("Logging.xlsm"):
            xl=win32com.client.Dispatch("Excel.Application")
            xl.Workbooks.Open(os.path.abspath("Logging.xlsm"), ReadOnly=1)
            xl.Application.Run("Logging.xlsm!Transport.SendEmailLogOut")
            #xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
            xl.Application.Quit() # Comment this out if your excel script closes
            del xl 
            
    def haveLogOutTicket(self):
        try:
             fetch_ticket = open('ticket.txt','r')
             ticket = fetch_ticket.read()
             fetch_ticket.close()
             
             if ticket == "1":
                 return True 
             else:
                 return False 
        except FileNotFoundError:
            return True
        
def mainPrompt():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


