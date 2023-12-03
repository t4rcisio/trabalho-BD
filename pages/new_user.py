# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\new_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import QDialog, QCalendarWidget

from threads import bdQueryLogin, bdQueryNewUser
from utils import broadcast


class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(609, 762)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.Form)
        self.widget.setStyleSheet("background-color: #ffc600;")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setContentsMargins(50, 9, 50, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setStyleSheet("border:0px")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\../images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(180, 180))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setStyleSheet("QWidget {\n"
"          \n"
"            background-color:#92653c;\n"
"            color: #ffffff;\n"
"            padding: 8px;\n"
"            border-radius:20px;\n"
"        }")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setMinimumSize(QtCore.QSize(0, 47))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 47))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget_27 = QtWidgets.QWidget(self.widget_4)
        self.widget_27.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_27.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_27.setObjectName("widget_27")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_27)
        self.horizontalLayout_22.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_22.setSpacing(3)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.config_label_3 = QtWidgets.QLabel(self.widget_27)
        self.config_label_3.setMinimumSize(QtCore.QSize(100, 35))
        self.config_label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.config_label_3.setStyleSheet("QLabel {\n"
"            background-color:#612d26;\n"
"            font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            padding: 3px;\n"
"            border-radius: 4px;\n"
"        }")
        self.config_label_3.setObjectName("config_label_3")
        self.horizontalLayout_22.addWidget(self.config_label_3)
        self.name = QtWidgets.QLineEdit(self.widget_27)
        self.name.setMinimumSize(QtCore.QSize(300, 35))
        self.name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.name.setStyleSheet("QLineEdit {\n"
"            background-color: #f0f0f0;\n"
"            border: none;\n"
"            padding: 2px;\n"
"            border-radius: 4px;\n"
"            color: #333;\n"
"            font-size:13px\n"
"        }\n"
"\n"
"        QLineEdit:hover {\n"
"            background-color: #e0e0e0;\n"
"        }\n"
"\n"
"        QLineEdit:focus {\n"
"            background-color: #ffffff;\n"
"            border: 2px solid #007bff;\n"
"        }")
        self.name.setObjectName("name")
        self.horizontalLayout_22.addWidget(self.name)
        self.verticalLayout_2.addWidget(self.widget_27)
        self.widget_25 = QtWidgets.QWidget(self.widget_4)
        self.widget_25.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_25.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_25.setObjectName("widget_25")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_25)
        self.horizontalLayout_20.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_20.setSpacing(3)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.config_label = QtWidgets.QLabel(self.widget_25)
        self.config_label.setMinimumSize(QtCore.QSize(100, 35))
        self.config_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.config_label.setStyleSheet("QLabel {\n"
"            background-color:#612d26;\n"
"            font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            padding: 3px;\n"
"            border-radius: 4px;\n"
"        }")
        self.config_label.setObjectName("config_label")
        self.horizontalLayout_20.addWidget(self.config_label)
        self.cpf = QtWidgets.QLineEdit(self.widget_25)
        self.cpf.setMinimumSize(QtCore.QSize(300, 35))
        self.cpf.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cpf.setStyleSheet("QLineEdit {\n"
"            background-color: #f0f0f0;\n"
"            border: none;\n"
"            padding: 2px;\n"
"            border-radius: 4px;\n"
"            color: #333;\n"
"            font-size:13px\n"
"        }\n"
"\n"
"        QLineEdit:hover {\n"
"            background-color: #e0e0e0;\n"
"        }\n"
"\n"
"        QLineEdit:focus {\n"
"            background-color: #ffffff;\n"
"            border: 2px solid #007bff;\n"
"        }")
        self.cpf.setObjectName("cpf")
        self.horizontalLayout_20.addWidget(self.cpf)
        self.verticalLayout_2.addWidget(self.widget_25)
        self.widget_26 = QtWidgets.QWidget(self.widget_4)
        self.widget_26.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_26.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_26)
        self.horizontalLayout_21.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_21.setSpacing(3)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.config_label_2 = QtWidgets.QLabel(self.widget_26)
        self.config_label_2.setMinimumSize(QtCore.QSize(100, 35))
        self.config_label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.config_label_2.setStyleSheet("QLabel {\n"
"            background-color:#612d26;\n"
"            font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            padding: 3px;\n"
"            border-radius: 4px;\n"
"        }")
        self.config_label_2.setObjectName("config_label_2")
        self.horizontalLayout_21.addWidget(self.config_label_2)
        self.nascimento = QtWidgets.QLineEdit(self.widget_26)
        self.nascimento.mousePressEvent = self.showCalendarDialog
        self.nascimento.setMinimumSize(QtCore.QSize(300, 35))
        self.nascimento.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nascimento.setStyleSheet("QLineEdit {\n"
"            background-color: #f0f0f0;\n"
"            border: none;\n"
"            padding: 2px;\n"
"            border-radius: 4px;\n"
"            color: #333;\n"
"            font-size:13px\n"
"        }\n"
"\n"
"        QLineEdit:hover {\n"
"            background-color: #e0e0e0;\n"
"        }\n"
"\n"
"        QLineEdit:focus {\n"
"            background-color: #ffffff;\n"
"            border: 2px solid #007bff;\n"
"        }")
        self.nascimento.setObjectName("nascimento")
        self.horizontalLayout_21.addWidget(self.nascimento)
        self.verticalLayout_2.addWidget(self.widget_26)
        self.widget_28 = QtWidgets.QWidget(self.widget_4)
        self.widget_28.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_28.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.widget_28)
        self.horizontalLayout_23.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.config_label_4 = QtWidgets.QLabel(self.widget_28)
        self.config_label_4.setMinimumSize(QtCore.QSize(100, 35))
        self.config_label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.config_label_4.setStyleSheet("QLabel {\n"
"            background-color:#612d26;\n"
"            font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            padding: 3px;\n"
"            border-radius: 4px;\n"
"        }")
        self.config_label_4.setObjectName("config_label_4")
        self.horizontalLayout_23.addWidget(self.config_label_4)
        self.senha = QtWidgets.QLineEdit(self.widget_28)
        self.senha.setMinimumSize(QtCore.QSize(300, 35))
        self.senha.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.senha.setStyleSheet("QLineEdit {\n"
"            background-color: #f0f0f0;\n"
"            border: none;\n"
"            padding: 2px;\n"
"            border-radius: 4px;\n"
"            color: #333;\n"
"            font-size:13px\n"
"        }\n"
"\n"
"        QLineEdit:hover {\n"
"            background-color: #e0e0e0;\n"
"        }\n"
"\n"
"        QLineEdit:focus {\n"
"            background-color: #ffffff;\n"
"            border: 2px solid #007bff;\n"
"        }")
        self.senha.setObjectName("senha")
        self.horizontalLayout_23.addWidget(self.senha)
        self.verticalLayout_2.addWidget(self.widget_28)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_5.setStyleSheet("QWidget {\n"
"          \n"
"            background-color:#92653c;\n"
"            color: #ffffff;\n"
"            padding: 8px;\n"
"            border-radius:20px;\n"
"        }")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.newuser = QtWidgets.QPushButton(self.widget_6, clicked=lambda : self.createUser())
        self.newuser.setMinimumSize(QtCore.QSize(150, 35))
        self.newuser.setMaximumSize(QtCore.QSize(16777215, 35))
        self.newuser.setStyleSheet("QPushButton {\n"
"            background-color: #612d26;\n"
"            color: #ffffff;\n"
"            padding: 3px;\n"
"            border-radius: 12px;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color: #3a211d;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color: #8a605a;\n"
"        }")
        self.newuser.setObjectName("newuser")
        self.verticalLayout_3.addWidget(self.newuser)
        self.backButton = QtWidgets.QPushButton(self.widget_6, clicked=lambda : self.backHome())
        self.backButton.setMinimumSize(QtCore.QSize(150, 35))
        self.backButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.backButton.setStyleSheet("QPushButton {\n"
"            background-color: #612d26;\n"
"            color: #ffffff;\n"
"            padding: 3px;\n"
"            border-radius: 12px;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color: #3a211d;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color: #8a605a;\n"
"        }")
        self.backButton.setObjectName("backButton")
        self.verticalLayout_3.addWidget(self.backButton)
        self.horizontalLayout_4.addWidget(self.widget_6)
        self.verticalLayout_5.addWidget(self.widget_5, 0, QtCore.Qt.AlignHCenter)
        self.widget_7 = QtWidgets.QWidget(self.widget_2)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5.addWidget(self.widget_7)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.broadcast = broadcast.Broadcast()

        self.movie2 = False
        self.start()
        self.bottonBar.setVisible(False)
        self.pLabel2.setVisible(False)
        self.isRunning = False

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'ADLaM Display\'; font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRAR</span></p></body></html>"))
        self.config_label_3.setText(_translate("Form", "NOME"))
        self.config_label.setText(_translate("Form", "CPF"))
        self.config_label_2.setText(_translate("Form", "NASCIMENTO"))
        self.config_label_4.setText(_translate("Form", "SENHA"))
        self.newuser.setText(_translate("Form", "REGISTRAR-SE"))
        self.backButton.setText(_translate("Form", "VOLTAR"))



    def backHome(self):
        self.Form.close()



    def createUser(self):


        if not self.isRunning:
            self.isRunning = True

            payload = [self.name.text(), self.cpf.text(), self.nascimento.text(), self.senha.text()]


            for item in payload:

                if str(item).replace(" ","") == '':
                    self.msgBox("Preencha todos os campos!")
                    return


            self.broadcast.bdData(payload)

            self.newUserTh = bdQueryNewUser.NewUser()
            self.newUserTh.run(self.start, self.end, self.QLabelInfo)
        else:
            self.msgBox("Aguarde o fim do processo atual")

    def start(self):

        self.isRunning = True

        if self.movie2 == False:

            self.movie2 = QMovie("./images/animation.gif")

            self.movie2.setScaledSize(QSize(60, 60))
            self.pLabel2 = QtWidgets.QLabel()
            self.pLabel2.setMovie(self.movie2)
            self.movie2.start()

            self.bottonBar = QtWidgets.QWidget()
            self.bottonBar.setStyleSheet("QWidget {background-color:#92653c;color: #ffffff;padding: 8px;border-radius:20px;}")
            self.bottonBar.setContentsMargins(20, 0, 0, 0)
            self.bottonLayout = QtWidgets.QHBoxLayout(self.bottonBar)
            self.bottonLayout.setContentsMargins(0, 0, 0, 0)

            self.bottonBar.setFixedHeight(60)

            self.bottonLayout.setAlignment(QtCore.Qt.AlignLeft)

            self.QLabelInfo = QtWidgets.QLabel()
            text = '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#ffffff;">Inicializando recursos</span></p></body></html>'
            self.QLabelInfo.setText(text)

            self.bottonLayout.addWidget(self.pLabel2)
            self.bottonLayout.setSpacing(9)
            self.bottonLayout.addWidget(self.QLabelInfo)

            self.verticalLayout_5.addWidget(self.bottonBar)
        else:
            self.bottonLayout.setAlignment(QtCore.Qt.AlignLeft)
            self.bottonBar.setVisible(True)
            self.pLabel2.setVisible(True)


    def end(self):
        self.bottonLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.bottonBar.setVisible(True)
        self.pLabel2.setVisible(False)
        self.isRunning = False
        self.broadcast.labelinfo("")

    def showCalendarDialog(self, event):
        # Create a QDialog to show the calendar
        dialog = QDialog(self.widget)
        dialog.setWindowTitle('SELECIONE SUA DATA DE NASCIMENTO')

        # Calendar Widget
        calendar = QCalendarWidget(dialog)
        calendar.clicked.connect(lambda: self.showDate(calendar.selectedDate(), dialog))
        dialog.layout = QtWidgets.QVBoxLayout(dialog)
        dialog.layout.addWidget(calendar)

        dialog.exec_()

    def showDate(self, date, dialog):
        selected_date = date.toString("dd-MM-yyyy")
        self.nascimento.setText(str(selected_date))

        dialog.accept()


    def msgBox(self, message, title="AVISO"):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        icon = QIcon('.\\ui\\../images/logo.png')
        messageBox.setWindowIcon(icon)
        messageBox.exec_()