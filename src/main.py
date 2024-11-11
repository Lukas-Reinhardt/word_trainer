import gui_window
import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets
from PySide2 import QtCore
import docx2txt
import pdfplumber


class MainWindow(QtWidgets.QMainWindow, gui_window.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.Timer = QtCore.QTimer()
        self.Timer.timeout.connect(self.update_time)
        self.elapsed_time_ms = 0
        self.word_count = 0
        self.text = ''
        self.pushButton_Timer_stoppen.setEnabled(False)
        self.pushButton_Text_laden.clicked.connect(self.on_pushButton_Text_laden_clicked)
        self.pushButton_Timer_starten.clicked.connect(self.on_pushButton_Timer_starten_clicked)
        self.pushButton_Timer_stoppen.clicked.connect(self.on_pushButton_Timer_stoppen_clicked)
        self.textEdit_Lesetext.textChanged.connect(self.count_words_and_display)

    def on_pushButton_Text_laden_clicked(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Textdatei öffnen', 'C:\\', "Textdateien (*.pdf *.txt *.docx)")[0]
        if file_path.endswith('.pdf'):
            self.textEdit_Lesetext.setText(read_text_from_pdf(file_path))
        elif file_path.endswith('.txt'):
            self.textEdit_Lesetext.setText(read_text_from_txt(file_path))
        elif file_path.endswith('.docx'):
            self.textEdit_Lesetext.setText(docx2txt.process(file_path))
        else:
            self.textEdit_Lesetext.setText('Dateiformat nicht erlaubt!')
        self.count_words_and_display()

    def count_words_and_display(self):
        self.text = self.textEdit_Lesetext.toPlainText()
        self.word_count = len(self.text.split())
        self.lcdNumber_Anzahl_Woerter.display(self.word_count)

    def on_pushButton_Timer_starten_clicked(self):
        self.pushButton_Timer_starten.setEnabled(False)
        self.pushButton_Timer_stoppen.setEnabled(True)
        self.lcdNumber_Timer.display(0)
        self.elapsed_time_ms = 0
        self.Timer.start(50)

    def on_pushButton_Timer_stoppen_clicked(self):
        self.Timer.stop()
        self.pushButton_Timer_starten.setEnabled(True)
        self.pushButton_Timer_stoppen.setEnabled(False)
        if self.elapsed_time_ms > 0:
            words_per_ms = round(self.word_count / self.elapsed_time_ms, 5)
            words_per_minute = round(words_per_ms * 1000 * 60)
            if words_per_minute < 10000:
                self.lcdNumber_Lesegeschwindigkeit.display(words_per_minute)
            else:
                self.lcdNumber_Lesegeschwindigkeit.display('---')
        else:
            self.lcdNumber_Lesegeschwindigkeit.display('---')

    def update_time(self):
        self.elapsed_time_ms += 50
        if self.elapsed_time_ms % 1000 == 0:
            self.lcdNumber_Timer.display(self.elapsed_time_ms/1000)


def read_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text


def read_text_from_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
