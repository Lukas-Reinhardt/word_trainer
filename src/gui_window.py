# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Die Klasse stellt das Hauptfenster der Anwendung dar.
class Ui_MainWindow(object):
    # Setup der Benutzeroberfläche für das Hauptfenster
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(871, 611)  # Fenstergröße auf 871x611 Pixel setzen
        self.centralwidget = QWidget(MainWindow)  # Zentrales Widget erstellen
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)  # Gitterlayout hinzufügen
        self.gridLayout.setObjectName(u"gridLayout")

        # Layout für den Textbereich erstellen
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textEdit_Lesetext = QTextEdit(self.centralwidget)  # Textfeld für den Eingabetext
        self.textEdit_Lesetext.setObjectName(u"textEdit_Lesetext")
        self.verticalLayout_6.addWidget(self.textEdit_Lesetext)  # Textfeld zum Layout hinzufügen

        # Layout für die Buttons und die Anzeige der Wortanzahl
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_Text_laden = QPushButton(self.centralwidget)  # Button zum Laden eines Textes
        self.pushButton_Text_laden.setObjectName(u"pushButton_Text_laden")
        self.horizontalLayout_3.addWidget(self.pushButton_Text_laden)

        # Layout für die Anzeige der Wortanzahl
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.lcdNumber_Anzahl_Woerter = QLCDNumber(self.groupBox)  # LCD-Anzeige für Wortanzahl
        self.lcdNumber_Anzahl_Woerter.setObjectName(u"lcdNumber_Anzahl_Woerter")
        self.lcdNumber_Anzahl_Woerter.setGeometry(QRect(10, 20, 81, 31))  # Position und Größe der Anzeige
        self.lcdNumber_Anzahl_Woerter.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_3.addWidget(self.groupBox)  # GroupBox zur Anzeige der Wortanzahl hinzufügen

        # Layout für Timer und Lesegeschwindigkeitsanzeige
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        # Buttons zum Starten und Stoppen des Timers
        self.pushButton_Timer_starten = QPushButton(self.centralwidget)  # Button zum Starten des Timers
        self.pushButton_Timer_starten.setObjectName(u"pushButton_Timer_starten")
        self.verticalLayout_2.addWidget(self.pushButton_Timer_starten)

        self.pushButton_Timer_stoppen = QPushButton(self.centralwidget)  # Button zum Stoppen des Timers
        self.pushButton_Timer_stoppen.setObjectName(u"pushButton_Timer_stoppen")
        self.verticalLayout_2.addWidget(self.pushButton_Timer_stoppen)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        # GroupBox für den Timer
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.lcdNumber_Timer = QLCDNumber(self.groupBox_2)  # LCD-Anzeige für den Timer
        self.lcdNumber_Timer.setObjectName(u"lcdNumber_Timer")
        self.lcdNumber_Timer.setGeometry(QRect(0, 20, 71, 31))  # Position und Größe der Timer-Anzeige
        self.horizontalLayout.addWidget(self.groupBox_2)  # GroupBox zum Layout hinzufügen

        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        # Layout für die Anzeige der Lesegeschwindigkeit
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        # GroupBox für die Lesegeschwindigkeitsanzeige
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.lcdNumber_Lesegeschwindigkeit = QLCDNumber(self.groupBox_3)  # LCD-Anzeige für Lesegeschwindigkeit
        self.lcdNumber_Lesegeschwindigkeit.setObjectName(u"lcdNumber_Lesegeschwindigkeit")
        self.lcdNumber_Lesegeschwindigkeit.setGeometry(QRect(10, 20, 91, 31))  # Position und Größe der Anzeige
        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        # GridLayout zum zentralen Widget hinzufügen
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        # Hauptfenster als zentrales Widget setzen
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)  # Alle Texte im Fenster übersetzen

        # Verbinden der Slots und Signale
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    # Methode zur Übersetzung der UI-Elemente
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))  # Fenster-Titel setzen
        self.pushButton_Text_laden.setText(QCoreApplication.translate("MainWindow", u"Text laden", None))  # Text des Buttons setzen
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Anzahl W\u00f6rter", None))  # Titel der GroupBox setzen
        self.pushButton_Timer_starten.setText(QCoreApplication.translate("MainWindow", u"Timer starten", None))  # Text des Start-Buttons setzen
        self.pushButton_Timer_stoppen.setText(QCoreApplication.translate("MainWindow", u"Timer stoppen", None))  # Text des Stopp-Buttons setzen
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Timer", None))  # Titel der GroupBox für den Timer setzen
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Lesegeschwindigkeit [W\u00f6rter pro Minute]", None))  # Titel für die Lesegeschwindigkeitsanzeige setzen

    # retranslateUi
