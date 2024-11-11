import gui_window
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6 import QtWidgets, QtCore
import docx2txt
import pdfplumber


class MainWindow(QtWidgets.QMainWindow, gui_window.Ui_MainWindow):
    def __init__(self):
        # Initialize the main window by calling the parent constructor and setting up the UI
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Create a QTimer object to track elapsed time
        self.Timer = QtCore.QTimer()
        # Connect the timer timeout signal to the method that updates the timer display
        self.Timer.timeout.connect(self.update_time)

        # Initialize variables to store elapsed time and word count
        self.elapsed_time_ms = 0  # Time in milliseconds
        self.word_count = 0  # Word count from the loaded text
        self.text = ''  # Text loaded from the file

        # Initially disable the stop timer button since the timer hasn't started
        self.pushButton_Timer_stoppen.setEnabled(False)

        # Connect the buttons to their corresponding handler methods
        self.pushButton_Text_laden.clicked.connect(self.on_pushButton_Text_laden_clicked)  # Load text from file
        self.pushButton_Timer_starten.clicked.connect(self.on_pushButton_Timer_starten_clicked)  # Start the timer
        self.pushButton_Timer_stoppen.clicked.connect(self.on_pushButton_Timer_stoppen_clicked)  # Stop the timer
        self.textEdit_Lesetext.textChanged.connect(
            self.count_words_and_display)  # Count words whenever the text changes

    def on_pushButton_Text_laden_clicked(self):
        """
        Opens a file dialog to load a text file (PDF, TXT, or DOCX).
        Based on the file type, it processes the content and displays it in the text editor.
        """
        # Open a file dialog and get the selected file path
        file_path, _ = QFileDialog.getOpenFileName(self, 'Textdatei öffnen', 'C:\\', "Textdateien (*.pdf *.txt *.docx)")

        # Determine file type based on extension and load its content accordingly
        if file_path.endswith('.pdf'):
            self.textEdit_Lesetext.setText(read_text_from_pdf(file_path))  # Read and display text from a PDF
        elif file_path.endswith('.txt'):
            self.textEdit_Lesetext.setText(read_text_from_txt(file_path))  # Read and display text from a TXT file
        elif file_path.endswith('.docx'):
            self.textEdit_Lesetext.setText(docx2txt.process(file_path))  # Read and display text from a DOCX file
        else:
            self.textEdit_Lesetext.setText(
                'Dateiformat nicht erlaubt!')  # Display an error if the file format is not supported

        # After loading the text, update the word count
        self.count_words_and_display()

    def count_words_and_display(self):
        """
        Counts the number of words in the loaded text and displays the result on the LCD.
        """
        self.text = self.textEdit_Lesetext.toPlainText()  # Get the plain text from the text editor
        self.word_count = len(self.text.split())  # Split the text into words and count them
        self.lcdNumber_Anzahl_Woerter.display(self.word_count)  # Display the word count on the LCD widget

    def on_pushButton_Timer_starten_clicked(self):
        """
        Starts the timer when the start button is clicked.
        Disables the start button and enables the stop button.
        Resets the timer and elapsed time.
        """
        self.pushButton_Timer_starten.setEnabled(False)  # Disable the start button
        self.pushButton_Timer_stoppen.setEnabled(True)  # Enable the stop button
        self.lcdNumber_Timer.display(0)  # Reset the timer display
        self.elapsed_time_ms = 0  # Reset the elapsed time
        self.Timer.start(50)  # Start the timer with a 50ms interval

    def on_pushButton_Timer_stoppen_clicked(self):
        """
        Stops the timer and calculates the reading speed when the stop button is clicked.
        It also disables the stop button and re-enables the start button.
        """
        self.Timer.stop()  # Stop the timer
        self.pushButton_Timer_starten.setEnabled(True)  # Re-enable the start button
        self.pushButton_Timer_stoppen.setEnabled(False)  # Disable the stop button

        # If time has passed, calculate the words per minute
        if self.elapsed_time_ms > 0:
            words_per_ms = round(self.word_count / self.elapsed_time_ms, 5)  # Calculate words per millisecond
            words_per_minute = round(words_per_ms * 1000 * 60)  # Convert words per ms to words per minute

            # If the calculated speed is reasonable, display it, otherwise show "---"
            if words_per_minute < 10000:
                self.lcdNumber_Lesegeschwindigkeit.display(
                    words_per_minute)  # Display reading speed in words per minute
            else:
                self.lcdNumber_Lesegeschwindigkeit.display('---')  # Display '---' if speed is too high
        else:
            self.lcdNumber_Lesegeschwindigkeit.display('---')  # Display '---' if no time was tracked

    def update_time(self):
        """
        Updates the elapsed time by 50 milliseconds every time the timer fires.
        Displays the updated time on the timer LCD widget in seconds.
        """
        self.elapsed_time_ms += 50  # Increment elapsed time by 50ms
        if self.elapsed_time_ms % 1000 == 0:  # Update the display every second
            self.lcdNumber_Timer.display(self.elapsed_time_ms / 1000)  # Display elapsed time in seconds


# Helper function to read text from a PDF file
def read_text_from_pdf(file_path):
    """
    Extracts text from a PDF file using pdfplumber.
    Iterates through all pages and extracts text, concatenating it into a single string.
    """
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:  # Loop through each page in the PDF
            text += page.extract_text()  # Append extracted text from the page
    return text


# Helper function to read text from a TXT file
def read_text_from_txt(file_path):
    """
    Reads the entire content of a plain text file and returns it as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()  # Return the contents of the text file


# Main program entry point
if __name__ == "__main__":
    """
    Entry point of the program. Creates the QApplication, initializes the MainWindow, and starts the event loop.
    """
    app = QApplication(sys.argv)  # Create the Qt application
    window = MainWindow()  # Create the main window
    window.show()  # Show the window
    sys.exit(app.exec())  # Enter the Qt event loop
