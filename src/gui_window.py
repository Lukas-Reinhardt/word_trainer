# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(871, 611)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textEdit_Lesetext = QTextEdit(self.centralwidget)
        self.textEdit_Lesetext.setObjectName(u"textEdit_Lesetext")

        self.verticalLayout_6.addWidget(self.textEdit_Lesetext)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_Text_laden = QPushButton(self.centralwidget)
        self.pushButton_Text_laden.setObjectName(u"pushButton_Text_laden")

        self.horizontalLayout_3.addWidget(self.pushButton_Text_laden)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.lcdNumber_Anzahl_Woerter = QLCDNumber(self.groupBox)
        self.lcdNumber_Anzahl_Woerter.setObjectName(u"lcdNumber_Anzahl_Woerter")
        self.lcdNumber_Anzahl_Woerter.setGeometry(QRect(10, 20, 81, 31))
        self.lcdNumber_Anzahl_Woerter.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_Timer_starten = QPushButton(self.centralwidget)
        self.pushButton_Timer_starten.setObjectName(u"pushButton_Timer_starten")

        self.verticalLayout_2.addWidget(self.pushButton_Timer_starten)

        self.pushButton_Timer_stoppen = QPushButton(self.centralwidget)
        self.pushButton_Timer_stoppen.setObjectName(u"pushButton_Timer_stoppen")

        self.verticalLayout_2.addWidget(self.pushButton_Timer_stoppen)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.lcdNumber_Timer = QLCDNumber(self.groupBox_2)
        self.lcdNumber_Timer.setObjectName(u"lcdNumber_Timer")
        self.lcdNumber_Timer.setGeometry(QRect(0, 20, 71, 31))

        self.horizontalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.lcdNumber_Lesegeschwindigkeit = QLCDNumber(self.groupBox_3)
        self.lcdNumber_Lesegeschwindigkeit.setObjectName(u"lcdNumber_Lesegeschwindigkeit")
        self.lcdNumber_Lesegeschwindigkeit.setGeometry(QRect(10, 20, 91, 31))

        self.horizontalLayout_4.addWidget(self.groupBox_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Text_laden.setText(QCoreApplication.translate("MainWindow", u"Text laden", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Anzahl W\u00f6rter", None))
        self.pushButton_Timer_starten.setText(QCoreApplication.translate("MainWindow", u"Timer starten", None))
        self.pushButton_Timer_stoppen.setText(QCoreApplication.translate("MainWindow", u"Timer stoppen", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Lesegeschwindigkeit [W\u00f6rter pro Minute]", None))
    # retranslateUi

