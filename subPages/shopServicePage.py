# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\shopServicePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from services import connection_db
from utils import broadcast


class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(975, 726)
                Form.setStyleSheet("background-color: #ffc600;")
                self.verticalLayout = QtWidgets.QVBoxLayout(Form)
                self.verticalLayout.setObjectName("verticalLayout")
                self.widget_2 = QtWidgets.QWidget(Form)
                self.widget_2.setMaximumSize(QtCore.QSize(16777215, 300))
                self.widget_2.setStyleSheet("QWidget {\n"
                "          \n"
                "            background-color:rgb(255, 226, 127);\n"
                "            color: #ffffff;\n"
                "            padding: 8px;\n"
                "            border-radius:20px;\n"
                "        }")
                self.widget_2.setObjectName("widget_2")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.widget_3 = QtWidgets.QWidget(self.widget_2)
                self.widget_3.setObjectName("widget_3")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.label = QtWidgets.QLabel(self.widget_3)
                self.label.setObjectName("label")
                self.verticalLayout_2.addWidget(self.label)
                self.widget_26 = QtWidgets.QWidget(self.widget_3)
                self.widget_26.setMinimumSize(QtCore.QSize(0, 40))
                self.widget_26.setMaximumSize(QtCore.QSize(16777215, 40))
                self.widget_26.setObjectName("widget_26")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_26)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setSpacing(3)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.config_label = QtWidgets.QLabel(self.widget_26)
                self.config_label.setMinimumSize(QtCore.QSize(35, 35))
                self.config_label.setMaximumSize(QtCore.QSize(35, 16777215))
                self.config_label.setStyleSheet("QLabel {\n"
                "            background-color:#612d26;\n"
                "            font-weight: bold;\n"
                "            color: rgb(255, 255, 255);\n"
                "            padding: 3px;\n"
                "            border-radius: 4px;\n"
                "        }")
                self.config_label.setObjectName("config_label")
                self.horizontalLayout_3.addWidget(self.config_label)
                self.idText = QtWidgets.QLineEdit(self.widget_26)
                self.idText.setMinimumSize(QtCore.QSize(50, 35))
                self.idText.setMaximumSize(QtCore.QSize(50, 16777215))
                self.idText.setStyleSheet("QLineEdit {\n"
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
                self.idText.setObjectName("idText")
                self.horizontalLayout_3.addWidget(self.idText)
                self.config_label_2 = QtWidgets.QLabel(self.widget_26)
                self.config_label_2.setMinimumSize(QtCore.QSize(120, 35))
                self.config_label_2.setMaximumSize(QtCore.QSize(100, 16777215))
                self.config_label_2.setStyleSheet("QLabel {\n"
                "            background-color:#612d26;\n"
                "            font-weight: bold;\n"
                "            color: rgb(255, 255, 255);\n"
                "            padding: 3px;\n"
                "            border-radius: 4px;\n"
                "        }")
                self.config_label_2.setObjectName("config_label_2")
                self.horizontalLayout_3.addWidget(self.config_label_2)
                self.serviceName = QtWidgets.QLineEdit(self.widget_26)
                self.serviceName.setMinimumSize(QtCore.QSize(300, 35))
                self.serviceName.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.serviceName.setStyleSheet("QLineEdit {\n"
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
                self.serviceName.setObjectName("serviceName")
                self.horizontalLayout_3.addWidget(self.serviceName)
                self.config_label_3 = QtWidgets.QLabel(self.widget_26)
                self.config_label_3.setMinimumSize(QtCore.QSize(50, 35))
                self.config_label_3.setMaximumSize(QtCore.QSize(50, 16777215))
                self.config_label_3.setStyleSheet("QLabel {\n"
                "            background-color:#612d26;\n"
                "            font-weight: bold;\n"
                "            color: rgb(255, 255, 255);\n"
                "            padding: 3px;\n"
                "            border-radius: 4px;\n"
                "        }")
                self.config_label_3.setObjectName("config_label_3")
                self.horizontalLayout_3.addWidget(self.config_label_3)
                self.priceText = QtWidgets.QLineEdit(self.widget_26)
                self.priceText.setMinimumSize(QtCore.QSize(100, 35))
                self.priceText.setMaximumSize(QtCore.QSize(100, 16777215))
                self.priceText.setStyleSheet("QLineEdit {\n"
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
                self.priceText.setObjectName("priceText")
                self.horizontalLayout_3.addWidget(self.priceText)
                self.verticalLayout_2.addWidget(self.widget_26)
                self.widget_25 = QtWidgets.QWidget(self.widget_3)
                self.widget_25.setMinimumSize(QtCore.QSize(0, 40))
                self.widget_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.widget_25.setObjectName("widget_25")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_25)
                self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_5.setSpacing(0)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.textEdit = QtWidgets.QTextEdit(self.widget_25)
                self.textEdit.setStyleSheet("QTextEdit {\n"
                "            background-color: #f0f0f0;\n"
                "            border: none;\n"
                "            padding: 2px;\n"
                "            border-radius: 4px;\n"
                "            color: #333;\n"
                "            font-size:13px\n"
                "        }")
                self.textEdit.setObjectName("textEdit")
                self.horizontalLayout_5.addWidget(self.textEdit)
                self.verticalLayout_2.addWidget(self.widget_25)
                self.horizontalLayout.addWidget(self.widget_3)
                self.widget_4 = QtWidgets.QWidget(self.widget_2)
                self.widget_4.setObjectName("widget_4")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.widget_8 = QtWidgets.QWidget(self.widget_4)
                self.widget_8.setMaximumSize(QtCore.QSize(200, 120))
                self.widget_8.setStyleSheet("QWidget {\n"
                "          \n"
                "            background-color:#92653c;\n"
                "            color: #ffffff;\n"
                "            padding: 8px;\n"
                "            border-radius:20px;\n"
                "        }")
                self.widget_8.setObjectName("widget_8")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.widget_9 = QtWidgets.QWidget(self.widget_8)
                self.widget_9.setObjectName("widget_9")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_9)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.newService = QtWidgets.QPushButton(self.widget_9, clicked=lambda : self.__ShopNewService())
                self.newService.setMinimumSize(QtCore.QSize(150, 35))
                self.newService.setMaximumSize(QtCore.QSize(16777215, 35))
                self.newService.setStyleSheet("QPushButton {\n"
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
                self.newService.setObjectName("newService")
                self.verticalLayout_3.addWidget(self.newService)
                self.saveService = QtWidgets.QPushButton(self.widget_9, clicked=lambda :self.__ShopSaveEdit())
                self.saveService.setMinimumSize(QtCore.QSize(100, 35))
                self.saveService.setMaximumSize(QtCore.QSize(16777215, 35))
                self.saveService.setStyleSheet("QPushButton {\n"
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
                self.saveService.setObjectName("saveService")
                self.verticalLayout_3.addWidget(self.saveService)
                self.horizontalLayout_4.addWidget(self.widget_9)
                self.horizontalLayout_2.addWidget(self.widget_8)
                self.horizontalLayout.addWidget(self.widget_4)
                self.verticalLayout.addWidget(self.widget_2)
                self.widget = QtWidgets.QWidget(Form)
                self.widget.setObjectName("widget")
                self.verticalLayout.addWidget(self.widget)

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

                self.broadcast = broadcast.Broadcast()
                self.oracleBD = connection_db.Oracle_db()

                self.dyLayout = QtWidgets.QVBoxLayout(self.widget)
                self.dyLayout.setContentsMargins(0,0,0,0)


                self.dynamicWindowApps = QtWidgets.QScrollArea()
                self.dyLayout.addWidget(self.dynamicWindowApps)

                self.__ShopShowServices()

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">GERENCIADOR DE SERVIÇOS</span></p></body></html>"))
                self.config_label.setText(_translate("Form", "ID"))
                self.config_label_2.setText(_translate("Form", "NOME DO SERVIÇO"))
                self.config_label_3.setText(_translate("Form", "Valor"))
                self.newService.setText(_translate("Form", "NOVO"))
                self.saveService.setText(_translate("Form", "SALVAR"))
                self.idText.setReadOnly(True)
                self.idText.setDisabled(True)



        def __ShopNewService(self):

                serviceName = str(self.serviceName.text()).upper()
                serviceText = self.textEdit.toPlainText()
                servicePrice = self.priceText.text()

                cpf = self.broadcast.credentials()["CPF"]

                payload = [cpf, serviceName, serviceText, servicePrice]

                for item in payload:
                        if str(item).replace(" ", "") == "":
                                self.msgBox("Preencha todos os campos")
                                return


                self.broadcast.bdData(payload)


                self.oracleBD.shopNewService()

                self.__ShopShowServices()


        def __ShopShowServices(self):

                self.broadcast.dataTransfer("")

                cpf = self.broadcast.credentials()["CPF"]

                payload = [cpf]

                self.broadcast.bdData(payload)

                self.oracleBD.shopListService()

                response = self.broadcast.dataTransfer()

                if response == False:

                        print("Default page")


                else:

                        self.wQWidget = QtWidgets.QWidget()
                        self.wQLayout = QtWidgets.QVBoxLayout(self.wQWidget)

                        response.reverse()

                        for item in response:

                                itemWidget = QtWidgets.QWidget()
                                itemWidget.setStyleSheet(self.__getWidgetStyle())
                                itemWidget.setFixedHeight(50)
                                itemLayout = QtWidgets.QHBoxLayout(itemWidget)
                                itemWidget.setContentsMargins(0,0,0,0)

                                idText = QtWidgets.QLineEdit()
                                idText.setFixedHeight(30)
                                idText.setFixedWidth(50)
                                idText.setText(str(item[0]))
                                idText.setDisabled(True)
                                idText.setStyleSheet(self.__getLineStyle())

                                serviceText = QtWidgets.QLineEdit()
                                serviceText.setFixedHeight(30)
                                serviceText.setText(item[2])
                                serviceText.setDisabled(True)
                                serviceText.setStyleSheet(self.__getLineStyle())

                                priceText = QtWidgets.QLineEdit()
                                priceText.setFixedHeight(30)
                                priceText.setFixedWidth(80)
                                priceText.setText("R$: "+str(item[4]))
                                priceText.setDisabled(True)
                                priceText.setStyleSheet(self.__getLineStyle())

                                editButton = QtWidgets.QPushButton()
                                editButton.setFixedHeight(30)
                                editButton.setText('EDITAR')
                                editButton.setStyleSheet(self.__getButtonStyle())
                                editButton.clicked.connect(lambda state, payload=item: self.__toEdid(payload))


                                dropButton = QtWidgets.QPushButton()
                                dropButton.setFixedHeight(30)
                                dropButton.setText('DELETAR')
                                dropButton.setStyleSheet(self.__getButtonStyle())
                                dropButton.clicked.connect(lambda state, payload=item[0]: self.__toDelete(payload))

                                itemLayout.addWidget(idText)
                                itemLayout.addWidget(serviceText)
                                itemLayout.addWidget(priceText)
                                itemLayout.addWidget(editButton)
                                itemLayout.addWidget(dropButton)

                                self.wQLayout.addWidget(itemWidget)




                        self.dynamicWindowApps.setStyleSheet("border:0px")
                        #self.dynamicWindowApps.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                        # dynamicWindowApps.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                        self.dynamicWindowApps.setWidgetResizable(True)
                        self.dynamicWindowApps.setWidget(self.wQWidget)



        def __toEdid(self, payload):

                self.idText.setText(str(payload[0]))
                self.serviceName.setText(str(payload[2]))
                self.textEdit.setText(str(payload[3]))
                self.priceText.setText(str(payload[4]))




        def __ShopSaveEdit(self):

                serviceId  = self.idText.text()
                serviceName = str(self.serviceName.text()).upper()
                serviceText = self.textEdit.toPlainText()
                servicePrice = self.priceText.text()

                if serviceId == "":
                        self.msgBox("Selecione um serviço para editar")
                        return


                payload = [serviceName, serviceText, servicePrice, int(serviceId)]


                for item in payload:
                        if str(item).replace(" ", "") == "":
                                self.msgBox("Preencha todos os campos")
                                return

                self.broadcast.bdData(payload)

                self.oracleBD.shopUpdateService()

                self.__ShopShowServices()



        def __toDelete(self, id):

                reply = QMessageBox.question(self.widget, 'ATENÇÃO', 'Você realmente deseja deletar esse serviço?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                        serviceId = id
                        payload = [serviceId]
                        self.broadcast.bdData(payload)
                        self.oracleBD.shopDeleteService()
                        self.__ShopShowServices()
                        self.msgBox("Serviço deletado da prateleira")

                else:
                        self.msgBox("Ok. Nada foi apagado")

        def msgBox(self, message, title="AVISO"):
                messageBox = QtWidgets.QMessageBox()
                messageBox.setWindowTitle(title)
                messageBox.setText(message)
                icon = QIcon('.\\ui\\../images/logo.png')
                messageBox.setWindowIcon(icon)
                messageBox.exec_()



        def __getLineStyle(self):

                return '''QLineEdit {
            background-color: #f0f0f0;
            border: none;
            padding: 2px;
            border-radius: 4px;
            color: #333;
			font-size:13px
        }

        QLineEdit:hover {
            background-color: #e0e0e0;
        }

        QLineEdit:focus {
            background-color: #ffffff;
            border: 2px solid #007bff;
        }'''


        def __getButtonStyle(self):

                return  '''QPushButton {
                            background-color: #612d26;
                            color: #ffffff;
                            padding: 3px;
                            border-radius: 12px;
                        }
        
                        QPushButton:hover {
                            background-color: #3a211d;
                        }
                
                        QPushButton:pressed {
                            background-color: #8a605a;
                        }'''


        def __getWidgetStyle(self):

                return '''QWidget {
          
			background-color:rgb(255, 226, 127);
            color: #ffffff;
            padding: 8px;
            border-radius:20px;
        }'''